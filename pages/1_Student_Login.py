import streamlit as st
import streamlit.components.v1 as components

from utils import init_db, register_student, login_student


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Student Access | VAZHI",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

init_db()


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* Remove Streamlit default elements */
    #MainMenu,
    footer,
    header,
    [data-testid="stSidebar"],
    [data-testid="stHeader"] {
        display: none !important;
    }

    /* Main page background */
    .stApp {
        background: #FBFAF4;
    }

    [data-testid="stAppViewContainer"] > .main {
        background: #FBFAF4;
    }

    .block-container {
        max-width: 1450px !important;
        padding: 20px 35px 25px 35px !important;
    }

    /* Brand */
    .vazhi-brand {
        display: flex;
        align-items: center;
        gap: 14px;
        margin: 0 0 45px 0;
    }

    .vazhi-logo {
        font-size: 43px;
        line-height: 1;
    }

    .vazhi-name {
        color: #075642;
        font-size: 35px;
        font-weight: 800;
        letter-spacing: 2px;
        line-height: 1.1;
    }

    .vazhi-tagline {
        color: #8C7651;
        font-size: 10px;
        letter-spacing: 4px;
        margin-top: 6px;
    }

    /* Welcome panel */
    .welcome-panel {
        background: linear-gradient(
            145deg,
            #008568 0%,
            #00634E 55%,
            #075642 100%
        );

        border-radius: 30px;
        padding: 24px;
        min-height: 650px;
        box-shadow: 0 18px 45px rgba(0, 75, 56, 0.13);
        box-sizing: border-box;
    }

    .welcome-inner {
        background: linear-gradient(
            160deg,
            #004D3F 0%,
            #003D32 100%
        );

        border-radius: 23px;
        padding: 36px 32px;
        min-height: 600px;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .welcome-cap {
        font-size: 76px;
        text-align: center;
        margin-bottom: 15px;
        line-height: 1.2;
    }

    .welcome-heading {
        color: #F7C75E;
        font-family: Georgia, serif;
        font-size: 36px;
        font-weight: bold;
        line-height: 1.2;
        margin: 0 0 25px 0;
    }

    .welcome-description {
        color: #FFFFFF;
        font-family: Georgia, serif;
        font-size: 19px;
        line-height: 1.8;
        margin-bottom: 20px;
    }

    .welcome-extra {
        color: #F7F5EC;
        font-family: Georgia, serif;
        font-size: 18px;
        line-height: 1.8;
        margin-bottom: 28px;
    }

    .welcome-quote {
        border-left: 5px solid #F6C453;
        padding: 8px 0 8px 22px;
        color: #FFFFFF;
        font-family: Georgia, serif;
        font-size: 20px;
        font-style: italic;
        line-height: 1.6;
    }

    /* Right-side heading */
    .access-heading {
        color: #064F40;
        font-family: Georgia, serif;
        font-size: 48px;
        font-weight: bold;
        line-height: 1.2;
        margin-top: 60px;
        margin-bottom: 12px;
    }

    .access-subtitle {
        color: #566A67;
        font-size: 17px;
        line-height: 1.7;
        margin-bottom: 28px;
    }

    /* Form labels */
    [data-testid="stWidgetLabel"] p {
        color: #064F40 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }

    /* Input fields */
    div[data-baseweb="input"] input {
        background-color: #FFFFFF !important;
        color: #163D35 !important;
        border-radius: 10px !important;
    }

    div[data-baseweb="input"] {
        border-radius: 10px !important;
    }

    div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border-radius: 10px !important;
    }

    /* Input container borders */
    div[data-baseweb="input"]:focus-within {
        border-color: #008568 !important;
    }

    /* Buttons */
    div.stButton > button,
    div.stFormSubmitButton > button {
        background: linear-gradient(
            100deg,
            #00654F,
            #008568
        ) !important;

        color: white !important;
        border: none !important;
        border-radius: 11px !important;
        min-height: 48px !important;
        font-weight: 700 !important;
        transition: 0.2s ease;
    }

    div.stButton > button:hover,
    div.stFormSubmitButton > button:hover {
        background: #004F3F !important;
        color: white !important;
        border: none !important;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        color: #075642 !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }

    button[data-baseweb="tab"][aria-selected="true"] {
        color: #075642 !important;
        border-bottom-color: #F4B942 !important;
    }

    /* Footer */
    .vazhi-footer {
        text-align: center;
        margin-top: 38px;
        padding: 20px 10px;
        color: #6F817A;
        font-size: 12px;
        line-height: 1.9;
        border-top: 1px solid #E8E3D7;
    }

    /* Mobile and smaller screens */
    @media screen and (max-width: 900px) {

        .block-container {
            padding: 15px !important;
        }

        .welcome-panel {
            min-height: auto;
            padding: 15px;
        }

        .welcome-inner {
            min-height: auto;
            padding: 30px 24px;
        }

        .welcome-heading {
            font-size: 29px;
        }

        .welcome-description,
        .welcome-extra {
            font-size: 16px;
        }

        .access-heading {
            margin-top: 15px;
            font-size: 36px;
        }

        .vazhi-brand {
            margin-bottom: 25px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# BRAND HEADER
# =========================================================

st.markdown(
    """
    <div class="vazhi-brand">
        <div class="vazhi-logo">🌱</div>
        <div>
            <div class="vazhi-name">VAZHI</div>
            <div class="vazhi-tagline">
                OPPORTUNITY FOR EVERYONE
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# PAGE LAYOUT
# =========================================================

left_column, right_column = st.columns(
    [0.85, 1.45],
    gap="large",
    vertical_alignment="center"
)


# =========================================================
# LEFT WELCOME PANEL
# =========================================================


with left_column:

    st.html("""
    <style>
    .welcome-panel {
        background: linear-gradient(145deg, #008568, #00634E, #075642);
        border-radius: 30px;
        padding: 24px;
        min-height: 600px;
        box-shadow: 0 18px 45px rgba(0, 75, 56, 0.13);
        box-sizing: border-box;
        display: flex;
        align-items: stretch;
    }

    .welcome-inner {
        background: linear-gradient(160deg, #004D3F, #003D32);
        border-radius: 23px;
        padding: 35px 30px;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-sizing: border-box;
    }

    .welcome-cap {
        font-size: 76px;
        text-align: center;
        margin-bottom: 18px;
    }

    .welcome-heading {
        color: #F7C75E;
        font-family: Georgia, serif;
        font-size: 34px;
        font-weight: bold;
        line-height: 1.25;
        margin-bottom: 22px;
    }

    .welcome-description {
        color: #FFFFFF;
        font-family: Georgia, serif;
        font-size: 18px;
        line-height: 1.7;
        margin-bottom: 22px;
    }

    .welcome-extra {
        color: #F7F5EC;
        font-family: Georgia, serif;
        font-size: 18px;
        line-height: 1.7;
        margin-bottom: 25px;
    }

    .welcome-quote {
        border-left: 5px solid #F6C453;
        padding: 8px 0 8px 18px;
        color: #FFFFFF;
        font-family: Georgia, serif;
        font-size: 19px;
        font-style: italic;
        line-height: 1.6;
    }

    @media (max-width: 900px) {
        .welcome-panel {
            min-height: auto;
            padding: 15px;
        }

        .welcome-inner {
            padding: 28px 22px;
        }

        .welcome-heading {
            font-size: 28px;
        }

        .welcome-description,
        .welcome-extra {
            font-size: 16px;
        }
    }
    </style>

    <div class="welcome-panel">
        <div class="welcome-inner">

            <div class="welcome-cap">🎓</div>

            <div class="welcome-heading">
                Your future starts here.
            </div>

            <div class="welcome-description">
                Welcome to VAZHI – your personal destination
                for discovering scholarships, government jobs,
                internships and career opportunities.
            </div>

            <div class="welcome-extra">
                Create your free account to keep track of
                opportunities and take the next step towards
                your dreams.
            </div>

            <div class="welcome-quote">
                "Your village is your origin,<br>
                not your limitation."
            </div>

        </div>
    </div>
    """)
# =========================================================
# RIGHT LOGIN AND REGISTRATION SECTION
# =========================================================

with right_column:

    st.markdown(
        """
        <div class="access-heading">
            Student Access
        </div>

        <div class="access-subtitle">
            Sign in to continue your journey or create your
            free student account.
        </div>
        """,
        unsafe_allow_html=True
    )

    login_tab, register_tab = st.tabs(
        ["🔐 Student Login", "✨ Create Account"]
    )


    # -----------------------------------------------------
    # STUDENT LOGIN
    # -----------------------------------------------------

    with login_tab:

        with st.form("login_form", clear_on_submit=False):

            email = st.text_input(
                "Email address",
                placeholder="Enter your registered email",
                key="login_email"
            )

            password = st.text_input(
                "Password",
                placeholder="Enter your password",
                type="password",
                key="login_password"
            )

            submitted = st.form_submit_button(
                "Log in to VAZHI →",
                use_container_width=True
            )

        if submitted:

            if not email.strip() or not password:
                st.warning(
                    "Please enter your email address and password."
                )

            else:
                user = login_student(
                    email.strip(),
                    password
                )

                if user:

                    st.session_state["vazhi_user"] = user

                    st.success(
                        f"Welcome back, {user['name']}!"
                    )

                    st.switch_page("app.py")

                else:
                    st.error(
                        "Email or password is incorrect. "
                        "If you are a new student, please create an account."
                    )


    # -----------------------------------------------------
    # CREATE STUDENT ACCOUNT
    # -----------------------------------------------------

    with register_tab:

        with st.form("register_form", clear_on_submit=False):

            name = st.text_input(
                "Full name",
                placeholder="Enter your full name",
                key="register_name"
            )

            email = st.text_input(
                "Email address",
                placeholder="Enter your email address",
                key="register_email"
            )

            password = st.text_input(
                "Create password",
                placeholder="At least 6 characters",
                type="password",
                key="register_password"
            )

            district = st.text_input(
                "District / Village",
                placeholder="Enter your district or village",
                key="register_district"
            )

            education = st.selectbox(
                "Current education",
                [
                    "School student",
                    "Higher Secondary",
                    "Diploma",
                    "Undergraduate",
                    "Postgraduate",
                    "Graduate / Job seeker",
                    "Other"
                ],
                key="register_education"
            )

            submitted = st.form_submit_button(
                "Create My Free Account →",
                use_container_width=True
            )

        if submitted:

            if (
                not name.strip()
                or not email.strip()
                or not password
            ):
                st.warning(
                    "Please fill in your name, email and password."
                )

            elif len(password) < 6:
                st.warning(
                    "Your password must contain at least 6 characters."
                )

            elif "@" not in email or "." not in email.split("@")[-1]:
                st.warning(
                    "Please enter a valid email address."
                )

            else:

                ok, message = register_student(
                    name.strip(),
                    email.strip(),
                    password,
                    district.strip(),
                    education
                )

                if ok:
                    st.success(message)
                    st.info(
                        "Your account has been created. "
                        "Open the Student Login tab to sign in."
                    )

                else:
                    st.error(message)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="vazhi-footer">
        <strong>VAZHI · Opportunity for Everyone</strong><br>
        Discover scholarships, government jobs, internships
        and career opportunities.<br>
        Always verify opportunities on their official websites
        before applying.
    </div>
    """,
    unsafe_allow_html=True
)