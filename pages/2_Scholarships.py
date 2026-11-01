
import streamlit as st
from utils import inject_css

st.set_page_config(
    page_title="Scholarships | VAZHI",
    page_icon="🎓",
    layout="wide"
)

# Apply the existing VAZHI design
inject_css()

# Fix main page and sidebar visibility
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
    color: #183b2b !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 14px;
}

/* SIDEBAR: keep it dark, make text readable */
section[data-testid="stSidebar"] {
    background-color: #20232d !important;
}

section[data-testid="stSidebar"] > div {
    background-color: #20232d !important;
}

/* Sidebar navigation text */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] a,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #f5f5f0 !important;
}

/* Sidebar links */
section[data-testid="stSidebar"] a {
    color: #f5f5f0 !important;
    text-decoration: none !important;
}

/* Hover effect */
section[data-testid="stSidebar"] a:hover {
    color: #f7c75e !important;
}

/* Selected page */
section[data-testid="stSidebar"] a[aria-current="page"] {
    background-color: #454956 !important;
    border-radius: 8px !important;
}

section[data-testid="stSidebar"] a[aria-current="page"] p,
section[data-testid="stSidebar"] a[aria-current="page"] span {
    color: #ffffff !important;
    font-weight: 700 !important;
}

/* Sidebar collapse/expand controls */
[data-testid="stSidebarCollapseButton"] button,
[data-testid="stSidebarCollapsedControl"] button {
    color: #f7c75e !important;
}

[data-testid="stSidebarCollapseButton"] svg,
[data-testid="stSidebarCollapsedControl"] svg {
    fill: #f7c75e !important;
    color: #f7c75e !important;
}
</style>
""", unsafe_allow_html=True)

# Optional login — never block access to scholarships
user = st.session_state.get("vazhi_user")

st.title("🎓 Scholarship Finder")

if user:
    st.write(
        f"Hello {user.get('name', 'Student')}! 👋 "
        "Explore scholarship opportunities for your education."
    )
else:
    st.write(
        "Welcome to VAZHI! 👋 "
        "Explore scholarship opportunities without creating an account."
    )

    with st.expander("🔐 Student Login (Optional)"):
        st.page_link(
            "pages/1_Student_Login.py",
            label="Open Student Login"
        )

st.markdown(
    "Discover scholarship resources from government portals and other "
    "organisations. Always verify the latest eligibility requirements "
    "and application deadlines."
)

st.divider()

# Search scholarships
search = st.text_input(
    "🔍 Search Scholarships",
    placeholder="Search by name or keyword..."
)

# Scholarship resources
items = [
    {
        "title": "National Scholarship Portal (NSP)",
        "category": "Government",
        "description": (
            "Explore central government scholarship schemes and "
            "participating state scholarship opportunities."
        ),
        "eligibility": (
            "Eligibility depends on the individual scheme, educational "
            "level, income criteria and other conditions."
        ),
        "url": "https://scholarships.gov.in/",
        "icon": "🇮🇳"
    },
    {
        "title": "Tamil Nadu Government Resources",
        "category": "State Government",
        "description": (
            "Explore official government announcements and "
            "education-related welfare information."
        ),
        "eligibility": (
            "Requirements vary according to the relevant department "
            "and scholarship scheme."
        ),
        "url": "https://www.tn.gov.in/",
        "icon": "🏛️"
    },
    {
        "title": "AICTE Scholarship Schemes",
        "category": "Technical Education",
        "description": (
            "Explore scholarship and student-development scheme "
            "information for eligible technical education students."
        ),
        "eligibility": (
            "Check the current scheme notification for eligible courses, "
            "student requirements and application conditions."
        ),
        "url": "https://www.aicte-india.org/",
        "icon": "💻"
    },
    {
        "title": "Buddy4Study",
        "category": "Scholarship Search",
        "description": (
            "Search for scholarships offered by different organisations "
            "and review their application requirements."
        ),
        "eligibility": (
            "Eligibility, required documents and deadlines depend "
            "on the individual scholarship."
        ),
        "url": "https://www.buddy4study.com/",
        "icon": "📚"
    }
]

# Category filter
categories = ["All Resources"] + sorted(
    {item["category"] for item in items}
)

selected_category = st.selectbox(
    "📂 Filter by Category",
    categories
)

# Filter resources
filtered_items = []
keyword = search.strip().lower()

for item in items:
    matches_search = (
        keyword in item["title"].lower()
        or keyword in item["description"].lower()
        or keyword in item["category"].lower()
    )

    matches_category = (
        selected_category == "All Resources"
        or selected_category == item["category"]
    )

    if matches_search and matches_category:
        filtered_items.append(item)

st.divider()
st.subheader("🌟 Explore Scholarship Resources")

if filtered_items:
    columns = st.columns(2)

    for index, item in enumerate(filtered_items):
        with columns[index % 2]:
            with st.container(border=True):
                st.markdown(f"### {item['icon']} {item['title']}")
                st.caption(item["category"])
                st.write(item["description"])

                with st.expander("📋 View Eligibility Information"):
                    st.write(item["eligibility"])

                st.link_button(
                    "Visit Website ↗",
                    item["url"],
                    use_container_width=True
                )
else:
    st.info(
        "No resources found. Try another search keyword or category."
    )

st.divider()

st.warning(
    "⚠️ Verify eligibility, deadlines and required documents on the "
    "relevant scheme's official website. Never pay an agent who "
    "guarantees a scholarship."
)

st.page_link(
    "app.py",
    label="🏠 Back to Home",
    icon="🏠"
)
