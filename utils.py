import sqlite3
import hashlib
import base64
from pathlib import Path
import streamlit as st


# =========================================================
# DATABASE CONFIGURATION
# =========================================================

# Store the database inside the project directory.
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "vazhi.db"


def get_db_connection():
    """
    Create a database connection.

    Ensures that the database directory exists before connecting.
    """
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(
        str(DB_PATH),
        timeout=10
    )

    connection.row_factory = sqlite3.Row

    return connection


# =========================================================
# DATABASE INITIALIZATION
# =========================================================

def init_db():
    """
    Create the students table if it does not already exist.
    """
    with get_db_connection() as con:

        con.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                district TEXT DEFAULT '',
                education TEXT DEFAULT '',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        con.commit()


# =========================================================
# PASSWORD HASHING
# =========================================================

def hash_password(password):
    """
    Hash a password using SHA-256.

    Compatibility note:
    This preserves the hashing format used by your existing
    database so previously registered users can still log in.
    """
    if not isinstance(password, str):
        raise ValueError("Password must be a string.")

    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


# =========================================================
# EMAIL VALIDATION
# =========================================================

def validate_email(email):
    """
    Basic email validation.
    """
    if not email:
        return False

    email = email.strip()

    if email.count("@") != 1:
        return False

    local_part, domain = email.split("@")

    if not local_part or not domain:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    if " " in email:
        return False

    return True


# =========================================================
# REGISTER STUDENT
# =========================================================

def register_student(
    name,
    email,
    password,
    district="",
    education=""
):
    """
    Register a new student.

    Returns:
        (True, success_message) when registration succeeds.
        (False, error_message) when registration fails.
    """

    # Normalize input
    name = (name or "").strip()
    email = (email or "").strip().lower()
    password = password or ""
    district = (district or "").strip()
    education = (education or "").strip()

    # Validate required fields
    if not name:
        return False, "Please enter your full name."

    if not email:
        return False, "Please enter your email address."

    if not password:
        return False, "Please create a password."

    if not validate_email(email):
        return False, "Please enter a valid email address."

    if len(password) < 6:
        return False, (
            "Your password must contain at least 6 characters."
        )

    try:

        with get_db_connection() as con:

            # Check whether the email already exists
            existing_student = con.execute(
                """
                SELECT id
                FROM students
                WHERE email = ?
                """,
                (email,)
            ).fetchone()

            if existing_student:
                return False, (
                    "This email is already registered. "
                    "Please log in instead."
                )

            # Insert the new student
            con.execute(
                """
                INSERT INTO students (
                    name,
                    email,
                    password_hash,
                    district,
                    education
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    name,
                    email,
                    hash_password(password),
                    district,
                    education
                )
            )

            con.commit()

        return True, (
            "Registration successful! "
            "Your account has been created. "
            "Please log in using your email and password."
        )

    except sqlite3.IntegrityError:

        # Handles duplicate emails if two registrations
        # happen at approximately the same time.
        return False, (
            "This email is already registered. "
            "Please log in instead."
        )

    except sqlite3.Error as error:

        print(f"Database registration error: {error}")

        return False, (
            "We could not create your account because of "
            "a database error. Please try again."
        )


# =========================================================
# STUDENT LOGIN
# =========================================================

def login_student(email, password):
    """
    Verify student credentials.

    Returns:
        A dictionary containing student information
        when login succeeds.

        None when the credentials are incorrect.
    """

    email = (email or "").strip().lower()
    password = password or ""

    if not email or not password:
        return None

    try:

        with get_db_connection() as con:

            student = con.execute(
                """
                SELECT
                    id,
                    name,
                    email,
                    district,
                    education
                FROM students
                WHERE email = ?
                AND password_hash = ?
                """,
                (
                    email,
                    hash_password(password)
                )
            ).fetchone()

        if student:
            return dict(student)

        return None

    except sqlite3.Error as error:

        print(f"Database login error: {error}")

        return None


# =========================================================
# CURRENT LOGGED-IN USER
# =========================================================

def get_logged_in_user():
    """
    Return the logged-in student from Streamlit session state.
    """
    return st.session_state.get("vazhi_user")


# =========================================================
# LOGOUT STUDENT
# =========================================================

def logout_student():
    """
    Remove the logged-in student from the session.
    """
    st.session_state.pop("vazhi_user", None)

    st.session_state["registration_notice"] = None


# =========================================================
# REQUIRE LOGIN
# =========================================================

def require_login():
    """
    Prevent access to protected pages when the student
    has not logged in.
    """
    user = get_logged_in_user()

    if not user:

        st.warning(
            "Please log in to access your student dashboard."
        )

        st.page_link(
            "pages/1_Student_Login.py",
            label="Go to Student Login →"
        )

        st.stop()

    return user


# =========================================================
# CUSTOM CSS
# =========================================================

def inject_css():

    st.markdown(
        """
        <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap'
        );

        :root {
            --green: #123f32;
            --green2: #22664e;
            --gold: #c9a85c;
            --cream: #f7f8f1;
            --ink: #173b32;
        }

        /* Main application */

        .stApp {
            background: var(--cream);
            color: var(--ink);
            font-family: 'DM Sans', sans-serif;
        }

        .block-container {
            max-width: 1180px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Headings */

        h1, h2, h3 {
            color: var(--ink);
        }

        /* Brand */

        .brand {
            font-size: 2rem;
            font-weight: 800;
            letter-spacing: 3px;
            color: var(--green);
        }

        .tagline {
            font-size: .68rem;
            letter-spacing: 3px;
            color: #777;
            margin-left: 48px;
            margin-top: -4px;
        }

        /* Section labels */

        .eyebrow,
        .section-kicker {
            color: #ad842d;
            font-size: .72rem;
            letter-spacing: 3px;
            font-weight: 800;
            margin: 1.2rem 0 .7rem;
        }

        /* Homepage hero */

        .hero-title {
            font-family: 'Playfair Display', serif;
            font-size: 3.4rem;
            line-height: 1.1;
            margin: .4rem 0 1rem;
        }

        .hero-copy {
            font-size: 1.08rem;
            line-height: 1.8;
            max-width: 620px;
        }

        .quote {
            margin: 1.4rem 0;
            padding: 1rem 1.2rem;
            background: #eaf0e4;
            border-left: 4px solid var(--gold);
            border-radius: 8px;
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-size: 1.15rem;
        }

        /* Hero illustration */

        .hero-art {
            height: 390px;
            border-radius: 28px;
            background: linear-gradient(
                145deg,
                #103c30,
                #2d7053
            );
            position: relative;
            overflow: hidden;
            box-shadow: 0 18px 50px #153f3020;
        }

        .sun {
            position: absolute;
            right: 65px;
            top: 45px;
            width: 85px;
            height: 85px;
            border-radius: 50%;
            background: #eacb79;
        }

        .hill {
            position: absolute;
            bottom: -80px;
            width: 120%;
            height: 230px;
            border-radius: 50% 50% 0 0;
        }

        .hill1 {
            left: -30%;
            background: #568967;
            transform: rotate(-8deg);
        }

        .hill2 {
            left: 25%;
            bottom: -105px;
            background: #8caf7b;
            transform: rotate(8deg);
        }

        .art-card {
            position: absolute;
            top: 115px;
            left: 13%;
            width: 70%;
            background: #fffdf4;
            border-radius: 18px;
            padding: 24px;
            box-shadow: 0 12px 30px #09291e55;
            display: flex;
            flex-direction: column;
            gap: 7px;
        }

        .art-card span {
            font-size: 2.2rem;
        }

        .art-card b {
            font-size: 1.15rem;
        }

        .art-card small {
            color: #66766c;
        }

        /* Floating labels */

        .floating {
            position: absolute;
            background: white;
            padding: 10px 14px;
            border-radius: 12px;
            box-shadow: 0 5px 20px #0002;
            font-size: .85rem;
            font-weight: 700;
        }

        .f1 {
            top: 30px;
            left: 20px;
        }

        .f2 {
            right: 15px;
            bottom: 60px;
        }

        .f3 {
            left: 20px;
            bottom: 35px;
        }

        /* Feature cards */

        .feature-card {
            min-height: 170px;
            padding: 24px;
            border-radius: 18px;
            background: white;
            border: 1px solid #e8e8dc;
            box-shadow: 0 8px 24px #1a45300b;
        }

        .feature-icon {
            font-size: 2rem;
        }

        .feature-card h3 {
            margin: .7rem 0 .3rem;
        }

        .feature-card p {
            color: #63736b;
            line-height: 1.6;
        }

        /* Creator photo */

        .creator-photo {
            width: 100%;
            max-height: 380px;
            object-fit: cover;
            object-position: center 25%;
            border-radius: 22px;
            border: 5px solid white;
            box-shadow: 0 10px 30px #123f3220;
        }

        .photo-placeholder {
            min-height: 260px;
            border: 2px dashed #c9a85c;
            border-radius: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            background: #fff;
        }

        .creator-note {
            background: white;
            padding: 28px 32px;
            border-radius: 20px;
            border: 1px solid #e8e8dc;
            line-height: 1.8;
        }

        .creator-note h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.65rem;
        }

        .signature {
            color: #6d786f;
            margin-top: 1rem;
            font-family: 'Playfair Display', serif;
            font-style: italic;
        }

        /* Footer */

        .footer {
            border-top: 1px solid #e2e6dc;
            margin-top: 3rem;
            padding-top: 1.2rem;
            color: #6d786f;
            font-size: .8rem;
            text-align: center;
        }

        /* Opportunity cards */

        .opportunity {
            background: white;
            padding: 20px 22px;
            border-radius: 16px;
            border: 1px solid #e5e8de;
            margin-bottom: 14px;
        }

        .pill {
            display: inline-block;
            background: #edf3e8;
            color: #22664e;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: .75rem;
            font-weight: 700;
        }

        /* Buttons */

        div.stButton > button,
        div.stLinkButton > a {
            border-radius: 10px;
            font-weight: 700;
        }

        div.stButton > button {
            background: var(--green2);
            color: white;
            border: none;
        }

        div.stButton > button:hover {
            background: var(--green);
            color: white;
            border: none;
        }

        /* Form controls */

        div[data-testid="stForm"] {
            border: none;
        }

        div[data-testid="stTextInput"] input {
            border-radius: 9px;
        }

        /* Responsive design */

        @media (max-width: 768px) {

            .block-container {
                padding: 1rem 5% 2rem;
            }

            .hero-title {
                font-size: 2.3rem;
            }

            .hero-art {
                height: 300px;
            }

            .creator-note {
                padding: 20px;
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# IMAGE TO BASE64
# =========================================================

def image_as_base64(relative_path):
    """
    Convert an image file to a Base64 string.

    Accepts an absolute path or a path relative to the
    project directory.
    """
    path = Path(relative_path)

    if not path.is_absolute():
        path = BASE_DIR / path

    if not path.exists() or not path.is_file():
        return None

    try:
        return base64.b64encode(
            path.read_bytes()
        ).decode("utf-8")

    except OSError as error:

        print(f"Unable to read image: {error}")

        return None