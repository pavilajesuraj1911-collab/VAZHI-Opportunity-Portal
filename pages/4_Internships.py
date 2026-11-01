
import streamlit as st
from utils import inject_css

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Internships | VAZHI",
    page_icon="💼",
    layout="wide"
)

inject_css()


# =========================================================
# PAGE STYLING
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

[data-testid="stSidebarCollapseButton"] button,
[data-testid="stSidebarCollapsedControl"] button {
    color: #f7c75e !important;
}

div[data-baseweb="input"],
div[data-baseweb="select"] {
    border-radius: 10px !important;
}

div.stLinkButton > a {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER — NO LOGIN REQUIRED
# =========================================================

st.title("💼 Internship Finder")

st.markdown("### Learn, gain experience, and grow your career")

user = st.session_state.get("vazhi_user")

if user:
    st.write(
        f"Welcome, {user.get('name', 'Student')}! 👋 "
        "Explore internships and build your professional skills."
    )
else:
    st.write(
        "Welcome to VAZHI! 👋 Discover internship resources "
        "without logging in or creating an account."
    )

st.info(
    "Explore internship platforms below. Check each opportunity's "
    "eligibility, location, stipend, duration and deadline before applying."
)

st.divider()


# =========================================================
# INTERNSHIP RESOURCES
# =========================================================

internships = [
    {
        "title": "AICTE Internship Portal",
        "category": "Government",
        "field": "Multiple Fields",
        "mode": "Varies by opportunity",
        "description": (
            "Explore internship opportunities and programmes "
            "listed through the AICTE internship portal."
        ),
        "eligibility": (
            "Requirements, eligible courses, duration and selection "
            "process vary by internship listing."
        ),
        "url": "https://internship.aicte-india.org/",
        "icon": "🏛️",
        "keywords": "AICTE engineering college students government"
    },
    {
        "title": "National Career Service",
        "category": "Government",
        "field": "Multiple Fields",
        "mode": "Varies by opportunity",
        "description": (
            "Explore career services and search for employment "
            "and related opportunities through the government portal."
        ),
        "eligibility": (
            "Check the individual listing for eligibility, employer "
            "details, location and application requirements."
        ),
        "url": "https://www.ncs.gov.in/",
        "icon": "🇮🇳",
        "keywords": "NCS career employment opportunities"
    },
    {
        "title": "Internshala",
        "category": "Private Platform",
        "field": "Multiple Fields",
        "mode": "Online and on-site options may be available",
        "description": (
            "Search internship listings across areas such as "
            "software development, marketing, data and design."
        ),
        "eligibility": (
            "Requirements, stipend, work mode and duration depend "
            "on the individual employer's listing."
        ),
        "url": "https://internshala.com/",
        "icon": "💻",
        "keywords": "software Python web development data science marketing design"
    },
    {
        "title": "AICTE Internship and Student Opportunities",
        "category": "Technical",
        "field": "Technology",
        "mode": "Varies by opportunity",
        "description": (
            "Explore technical internship and learning opportunities "
            "relevant to students in eligible technical disciplines."
        ),
        "eligibility": (
            "Review the specific opportunity's current requirements "
            "before applying."
        ),
        "url": "https://internship.aicte-india.org/",
        "icon": "⚙️",
        "keywords": "technology technical engineering IT"
    },
    {
        "title": "LinkedIn Jobs",
        "category": "Private Platform",
        "field": "Multiple Fields",
        "mode": "Varies by opportunity",
        "description": (
            "Search for internships posted by companies and "
            "organisations across different industries."
        ),
        "eligibility": (
            "Check the employer's requirements, location, duration, "
            "stipend and application instructions."
        ),
        "url": "https://www.linkedin.com/jobs/",
        "icon": "🌐",
        "keywords": "company corporate business internship"
    },
    {
        "title": "Wellfound",
        "category": "Private Platform",
        "field": "Startups and Technology",
        "mode": "Varies by opportunity",
        "description": (
            "Explore startup career opportunities and check for "
            "internship listings suitable for your interests."
        ),
        "eligibility": (
            "Availability and requirements vary by startup and listing. "
            "Verify that the role is an internship before applying."
        ),
        "url": "https://wellfound.com/jobs",
        "icon": "🚀",
        "keywords": "startup software technology business"
    }
]


# =========================================================
# SEARCH AND FILTERS
# =========================================================

st.subheader("🔎 Find Your Internship")

search = st.text_input(
    "Search by skill, field or platform",
    placeholder="Example: Python, web development, data analysis..."
)

categories = ["All Categories"] + sorted(
    {item["category"] for item in internships}
)

selected_category = st.selectbox(
    "📂 Internship category",
    categories
)

fields = ["All Fields"] + sorted(
    {item["field"] for item in internships}
)

selected_field = st.selectbox(
    "🎯 Area of interest",
    fields
)


# =========================================================
# FILTER INTERNSHIPS
# =========================================================

keyword = search.strip().lower()
filtered_internships = []

for item in internships:

    searchable_text = " ".join([
        item["title"],
        item["category"],
        item["field"],
        item["mode"],
        item["description"],
        item["eligibility"],
        item["keywords"]
    ]).lower()

    matches_search = keyword in searchable_text

    matches_category = (
        selected_category == "All Categories"
        or item["category"] == selected_category
    )

    matches_field = (
        selected_field == "All Fields"
        or item["field"] == selected_field
    )

    if matches_search and matches_category and matches_field:
        filtered_internships.append(item)


# =========================================================
# DISPLAY INTERNSHIP CARDS
# =========================================================

st.divider()
st.subheader("🌟 Explore Internship Opportunities")

st.caption(
    f"{len(filtered_internships)} resource(s) match your filters."
)

if filtered_internships:

    columns = st.columns(2)

    for index, item in enumerate(filtered_internships):

        with columns[index % 2]:

            with st.container(border=True):

                st.markdown(
                    f"### {item['icon']} {item['title']}"
                )

                st.caption(item["category"])

                st.write(item["description"])

                st.markdown(f"**Field:** {item['field']}")

                st.markdown(f"**Work mode:** {item['mode']}")

                with st.expander("📋 Eligibility and details"):
                    st.write(item["eligibility"])

                st.link_button(
                    "Explore Opportunities ↗",
                    item["url"],
                    use_container_width=True
                )

else:
    st.info(
        "No resources match your search. Try another keyword "
        "or choose All Categories."
    )


# =========================================================
# APPLICATION SAFETY
# =========================================================

st.divider()

st.subheader("✅ Before Applying")

st.markdown("""
- Read the complete internship description.
- Check whether the role is paid or unpaid.
- Verify the duration, work mode and location.
- Check eligibility and application deadlines.
- Research the organisation before sharing personal information.
- Never pay a recruiter who guarantees an internship.
""")

st.warning(
    "VAZHI provides internship search starting points, not a live "
    "verified vacancy feed. Confirm current listings and application "
    "details on each platform."
)


# =========================================================
# BACK TO HOME
# =========================================================

st.page_link(
    "app.py",
    label="🏠 Back to Home",
    icon="🏠"
)
