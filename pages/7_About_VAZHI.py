
import streamlit as st
from utils import inject_css

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="About VAZHI",
    page_icon="🌱",
    layout="wide"
)

inject_css()


# =========================================================
# VAZHI THEME AND SIDEBAR
# =========================================================

st.markdown("""
<style>
.stApp {
    background-color: #f7f8ef;
    color: #183b2b;
}

.stApp h1,
.stApp h2,
.stApp h3 {
    color: #176b45 !important;
}

.stApp p,
.stApp label,
.stApp li {
    color: #263b30;
    line-height: 1.7;
}

section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div {
    background-color: #20232d !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] a,
section[data-testid="stSidebar"] label {
    color: #f5f5f0 !important;
}

section[data-testid="stSidebar"] a:hover {
    color: #f7c75e !important;
}

section[data-testid="stSidebar"] a[aria-current="page"] {
    background-color: #454956 !important;
    border-radius: 8px !important;
}

section[data-testid="stSidebar"] a[aria-current="page"] p {
    color: #ffffff !important;
    font-weight: 700 !important;
}

.about-hero {
    background: linear-gradient(135deg, #00634e, #008568);
    border-radius: 24px;
    padding: 38px 32px;
    margin-bottom: 22px;
}

.about-hero h1 {
    color: #f7c75e !important;
    font-size: 43px;
    font-family: Georgia, serif;
}

.about-hero p {
    color: #ffffff !important;
    font-size: 18px;
}

.about-card {
    background: #ffffff;
    border: 1px solid #e4e8d8;
    border-radius: 16px;
    padding: 22px;
    min-height: 175px;
}

.about-card h3 {
    color: #176b45 !important;
    margin-top: 0;
}

.about-quote {
    background: #e8f2e7;
    border-left: 5px solid #d9a92e;
    border-radius: 10px;
    padding: 22px;
    color: #164d37;
    font-family: Georgia, serif;
    font-size: 21px;
    font-style: italic;
}

div[data-testid="stAlert"] p {
    color: #263b30 !important;
}

div.stButton > button,
div.stLinkButton > a {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO SECTION
# =========================================================

st.markdown("""
<div class="about-hero">
    <h1>🌱 About VAZHI</h1>
    <p>
        Every dream deserves an opportunity.
        Every student deserves a path to a brighter future.
    </p>
    <p>
        VAZHI — Opportunity for Everyone
    </p>
</div>
""", unsafe_allow_html=True)


# =========================================================
# INTRODUCTION
# =========================================================

st.header("What is VAZHI?")

st.write("""
VAZHI is an opportunity-discovery platform designed to help students
explore educational and career resources in one place.

Students can discover scholarship resources, government recruitment
portals, internships and career guidance without needing to create
an account or log in.
""")

st.write("""
The goal is to make useful information easier to discover, especially
for students who may not know where to begin their career journey.
""")

st.divider()


# =========================================================
# MISSION AND VISION
# =========================================================

st.header("🎯 Our Mission and Vision")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="about-card">
        <h3>🎯 Our Mission</h3>
        <p>
            To make educational and career opportunity information
            easier to discover and understand, helping students take
            practical steps towards their goals.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <h3>🌍 Our Vision</h3>
        <p>
            A future where a student's background or location does not
            prevent them from exploring opportunities and building
            their own path.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# =========================================================
# WHAT STUDENTS CAN EXPLORE
# =========================================================

st.header("🚀 What Can You Find on VAZHI?")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
    <div class="about-card">
        <h3>🎓 Scholarship Resources</h3>
        <p>
            Explore government portals and scholarship-search resources.
            Check each scheme's official eligibility requirements and dates.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-card">
        <h3>💼 Internship Opportunities</h3>
        <p>
            Discover internship platforms where you can explore practical
            experience and opportunities to develop your skills.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="about-card">
        <h3>🏛️ Government Jobs</h3>
        <p>
            Find starting points for government recruitment information
            and visit official portals for notifications and applications.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-card">
        <h3>🧭 Career Guidance</h3>
        <p>
            Explore career paths, identify skills to learn and discover
            beginner project ideas to support your career preparation.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.divider()


# =========================================================
# OUR VALUES
# =========================================================

st.header("💚 What VAZHI Stands For")

values = [
    (
        "Accessibility",
        "Make opportunity information easier for students to explore."
    ),
    (
        "Awareness",
        "Help students discover resources they may not know about."
    ),
    (
        "Growth",
        "Encourage learning, practical experience and continuous improvement."
    ),
    (
        "Independence",
        "Let students explore the platform without a mandatory account."
    )
]

for title, description in values:
    with st.expander(f"✨ {title}"):
        st.write(description)

st.divider()


# =========================================================
# MOTIVATIONAL MESSAGE
# =========================================================

st.markdown("""
<div class="about-quote">
    "Your village is your origin, not your limitation."
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("""
Your journey does not have to be defined by where you start.
Explore, learn, prepare and take one step at a time.
""")

st.divider()


# =========================================================
# IMPORTANT INFORMATION
# =========================================================

st.header("📌 A Note to Our Students")

st.write("""
VAZHI helps you discover resources; it does not guarantee scholarships,
jobs or internships. Always verify eligibility, deadlines, fees and
application instructions through the relevant official website.
""")

st.warning(
    "Be careful with anyone who promises guaranteed scholarships, "
    "government jobs or internships in exchange for money."
)


# =========================================================
# NAVIGATION
# =========================================================

st.header("🌱 Start Exploring")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "pages/2_Scholarships.py",
        label="🎓 Explore Scholarships",
        use_container_width=True
    )

with col2:
    st.page_link(
        "pages/3_Government_Jobs.py",
        label="🏛️ Explore Government Jobs",
        use_container_width=True
    )

with col3:
    st.page_link(
        "pages/4_Internships.py",
        label="💼 Explore Internships",
        use_container_width=True
    )

st.page_link(
    "app.py",
    label="🏠 Back to Home",
    icon="🏠"
)
