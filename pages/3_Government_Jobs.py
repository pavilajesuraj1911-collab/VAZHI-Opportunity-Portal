
import streamlit as st
from utils import inject_css

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Government Jobs | VAZHI",
    page_icon="🏛️",
    layout="wide"
)

# Apply the existing VAZHI theme
inject_css()


# =========================================================
# PAGE STYLING
# =========================================================

st.markdown("""
<style>
/* Main page */
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
}

div[data-testid="stCaptionContainer"] p {
    color: #55745f !important;
}

div[data-testid="stAlert"] {
    background-color: #fff4cc !important;
    border-radius: 10px !important;
}

div[data-testid="stAlert"] p {
    color: #263b30 !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px;
}

/* Sidebar */
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

section[data-testid="stSidebar"] a {
    text-decoration: none !important;
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

/* Search inputs and dropdowns */
div[data-baseweb="input"],
div[data-baseweb="select"] {
    border-radius: 10px !important;
}

/* Buttons */
div.stButton > button,
div.stLinkButton > a {
    border-radius: 10px !important;
}

/* Sidebar expand/collapse icons */
[data-testid="stSidebarCollapseButton"] button,
[data-testid="stSidebarCollapsedControl"] button {
    color: #f7c75e !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER — NO LOGIN REQUIRED
# =========================================================

st.title("🏛️ Government Jobs")

st.markdown("### Find your path to a government career")

user = st.session_state.get("vazhi_user")

if user:
    st.write(
        f"Welcome, {user.get('name', 'Student')}! 👋 "
        "Explore recruitment resources and plan your career."
    )
else:
    st.write(
        "Welcome to VAZHI! 👋 Explore government job opportunities "
        "without logging in or creating an account."
    )

st.info(
    "Explore official recruitment portals below. Check each official "
    "notification for current vacancies, eligibility, application "
    "deadlines and examination details."
)

st.divider()


# =========================================================
# GOVERNMENT JOB RESOURCES
# =========================================================

jobs = [
    {
        "title": "Union Public Service Commission (UPSC)",
        "category": "Central Government",
        "qualification": "Degree and other post-specific qualifications",
        "description": (
            "Explore Civil Services examinations and other Union "
            "Public Service Commission recruitment notifications."
        ),
        "eligibility": (
            "Age limits, educational qualifications, number of attempts "
            "and other requirements depend on the examination and post."
        ),
        "url": "https://upsc.gov.in/",
        "icon": "🇮🇳",
        "keywords": "civil services IAS IPS officer graduate degree"
    },
    {
        "title": "Staff Selection Commission (SSC)",
        "category": "Central Government",
        "qualification": "10th, 12th, degree and post-specific qualifications",
        "description": (
            "Explore SSC recruitment examinations for eligible central "
            "government positions."
        ),
        "eligibility": (
            "Requirements vary across examinations such as CGL, CHSL, "
            "MTS and other recruitment categories. Read each notification."
        ),
        "url": "https://ssc.gov.in/",
        "icon": "📋",
        "keywords": "SSC CGL CHSL MTS clerk assistant 10th 12th degree"
    },
    {
        "title": "Tamil Nadu Public Service Commission (TNPSC)",
        "category": "Tamil Nadu Government",
        "qualification": "Varies by group and post",
        "description": (
            "Find Tamil Nadu government recruitment notifications, "
            "examination schedules and results."
        ),
        "eligibility": (
            "Educational qualifications, age limits, Tamil-language "
            "requirements and other conditions vary by notification."
        ),
        "url": "https://www.tnpsc.gov.in/",
        "icon": "🏛️",
        "keywords": "TNPSC group 1 group 2 group 4 Tamil Nadu state"
    },
    {
        "title": "National Career Service (NCS)",
        "category": "Job Search",
        "qualification": "Opportunities for different education levels",
        "description": (
            "Explore job-search services and career resources through "
            "the Government of India's National Career Service portal."
        ),
        "eligibility": (
            "Requirements depend on each advertised position. Verify "
            "the employer, qualifications and application conditions."
        ),
        "url": "https://www.ncs.gov.in/",
        "icon": "💼",
        "keywords": "employment jobs career job seeker private public"
    },
    {
        "title": "Indian Railways Recruitment",
        "category": "Railway Recruitment",
        "qualification": "Varies by railway post",
        "description": (
            "Visit the official Indian Railways website to find railway "
            "information and locate relevant recruitment portals."
        ),
        "eligibility": (
            "Qualifications, age limits and selection stages depend "
            "on the railway post and its recruitment notification."
        ),
        "url": "https://indianrailways.gov.in/",
        "icon": "🚆",
        "keywords": "railway RRB technician assistant loco pilot"
    },
    {
        "title": "Employment News",
        "category": "Job Search",
        "qualification": "Varies by advertised position",
        "description": (
            "Explore government job advertisements and recruitment "
            "announcements published through Employment News."
        ),
        "eligibility": (
            "Read the original recruitment notification for required "
            "qualifications, application dates and instructions."
        ),
        "url": "https://employmentnews.gov.in/",
        "icon": "📰",
        "keywords": "employment news vacancies recruitment notification"
    }
]


# =========================================================
# SEARCH AND FILTERS
# =========================================================

st.subheader("🔎 Find Government Job Resources")

search = st.text_input(
    "Search by department, qualification or keyword",
    placeholder="Example: TNPSC, degree, railway, SSC..."
)

categories = ["All Categories"] + sorted(
    {job["category"] for job in jobs}
)

selected_category = st.selectbox(
    "📂 Filter by category",
    categories
)

qualifications = [
    "All Qualifications",
    "10th",
    "12th",
    "Degree"
]

selected_qualification = st.selectbox(
    "🎓 Filter by qualification",
    qualifications
)


# =========================================================
# FILTER JOB RESOURCES
# =========================================================

filtered_jobs = []
keyword = search.strip().lower()

for job in jobs:

    searchable_text = " ".join([
        job["title"],
        job["category"],
        job["qualification"],
        job["description"],
        job["eligibility"],
        job["keywords"]
    ]).lower()

    matches_search = keyword in searchable_text

    matches_category = (
        selected_category == "All Categories"
        or job["category"] == selected_category
    )

    # Preliminary keyword filtering only.
    # This does not determine actual eligibility.
    qualification_text = job["qualification"].lower()

    if selected_qualification == "All Qualifications":
        matches_qualification = True

    elif selected_qualification == "Degree":
        matches_qualification = (
            "degree" in qualification_text
            or "varies" in qualification_text
            or "post-specific" in qualification_text
            or "different education" in qualification_text
        )

    elif selected_qualification == "12th":
        matches_qualification = (
            "12th" in qualification_text
            or "varies" in qualification_text
            or "post-specific" in qualification_text
            or "different education" in qualification_text
        )

    else:
        matches_qualification = (
            "10th" in qualification_text
            or "varies" in qualification_text
            or "post-specific" in qualification_text
            or "different education" in qualification_text
        )

    if (
        matches_search
        and matches_category
        and matches_qualification
    ):
        filtered_jobs.append(job)


# =========================================================
# DISPLAY JOB CARDS
# =========================================================

st.divider()
st.subheader("🌟 Explore Recruitment Portals")

st.caption(
    f"{len(filtered_jobs)} recruitment resource(s) found."
)

if filtered_jobs:

    columns = st.columns(2)

    for index, job in enumerate(filtered_jobs):

        with columns[index % 2]:

            with st.container(border=True):

                st.markdown(
                    f"### {job['icon']} {job['title']}"
                )

                st.caption(job["category"])

                st.write(job["description"])

                st.markdown(
                    f"**Qualification:** {job['qualification']}"
                )

                with st.expander("📋 View Eligibility and Details"):
                    st.write(job["eligibility"])

                st.link_button(
                    "Visit Official Website ↗",
                    job["url"],
                    use_container_width=True
                )

else:
    st.info(
        "No resources match your search. Try a different keyword "
        "or select All Categories."
    )


# =========================================================
# APPLICATION GUIDANCE
# =========================================================

st.divider()

st.subheader("✅ Before Applying")

st.markdown("""
- Read the complete official recruitment notification.
- Verify educational qualifications and age limits.
- Check the application deadline and examination fees.
- Apply through the official portal specified in the notification.
- Never pay an agent who guarantees a government job.
""")

st.warning(
    "VAZHI currently lists recruitment starting points, not live vacancy "
    "data. Verify vacancy availability and deadlines on official websites."
)


# =========================================================
# BACK TO HOME
# =========================================================

st.page_link(
    "app.py",
    label="🏠 Back to Home",
    icon="🏠"
)
