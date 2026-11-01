
import streamlit as st
from utils import inject_css

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Career Guidance | VAZHI",
    page_icon="🧭",
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

div[data-testid="stLinkButton"] a {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER — ACCESSIBLE WITHOUT LOGIN
# =========================================================

st.title("🧭 Career Guidance")

st.markdown(
    "### Discover your strengths. Explore your possibilities."
)

user = st.session_state.get("vazhi_user")

if user:
    st.write(
        f"Welcome, {user.get('name', 'Student')}! 👋 "
        "Let's explore career paths and skills for your future."
    )
else:
    st.write(
        "Welcome to VAZHI! 👋 Explore career paths and learning "
        "resources without logging in or creating an account."
    )

st.info(
    "Use this guide to explore possible career paths. Your results "
    "are suggestions to help you plan, not a professional assessment "
    "or a guarantee of employment."
)

st.divider()


# =========================================================
# CAREER EXPLORER
# =========================================================

st.subheader("🎯 Explore Career Paths")

career_options = {
    "Software Developer": {
        "icon": "💻",
        "description": (
            "Design, develop, test and maintain websites, applications "
            "and software systems."
        ),
        "skills": [
            "Python, Java or JavaScript",
            "Data structures and algorithms",
            "SQL and databases",
            "Git and debugging",
            "Problem-solving"
        ],
        "projects": [
            "Student management system",
            "Personal portfolio website",
            "Expense tracker"
        ],
        "url": "https://developer.mozilla.org/"
    },
    "Data Analyst": {
        "icon": "📊",
        "description": (
            "Analyse data, identify patterns and communicate findings "
            "to help organisations make decisions."
        ),
        "skills": [
            "Excel",
            "SQL",
            "Python and pandas",
            "Data visualisation",
            "Statistics fundamentals"
        ],
        "projects": [
            "Student performance analysis",
            "Sales dashboard",
            "Public dataset analysis"
        ],
        "url": "https://learn.microsoft.com/training/"
    },
    "AI / Machine Learning Engineer": {
        "icon": "🤖",
        "description": (
            "Build software that uses data, machine learning models "
            "and artificial intelligence techniques."
        ),
        "skills": [
            "Python programming",
            "Mathematics and statistics",
            "Machine learning fundamentals",
            "Data preparation",
            "Model evaluation"
        ],
        "projects": [
            "Spam message classifier",
            "Image classification demo",
            "Simple recommendation system"
        ],
        "url": "https://www.tensorflow.org/learn"
    },
    "Cybersecurity Analyst": {
        "icon": "🔐",
        "description": (
            "Help protect computer systems, networks and information "
            "from security threats."
        ),
        "skills": [
            "Networking fundamentals",
            "Operating systems",
            "Security principles",
            "Log analysis",
            "Basic scripting"
        ],
        "projects": [
            "Security awareness guide",
            "Sample log analysis dashboard",
            "Password strength checker"
        ],
        "url": "https://www.cisa.gov/cybersecurity"
    },
    "Web Developer": {
        "icon": "🌐",
        "description": (
            "Create websites and web applications for users, businesses "
            "and organisations."
        ),
        "skills": [
            "HTML and CSS",
            "JavaScript",
            "Responsive design",
            "React or another framework",
            "APIs and databases"
        ],
        "projects": [
            "Responsive portfolio",
            "Opportunity listing website",
            "Online event registration page"
        ],
        "url": "https://developer.mozilla.org/"
    },
    "UI / UX Designer": {
        "icon": "🎨",
        "description": (
            "Design useful, accessible and visually clear digital "
            "experiences for websites and applications."
        ),
        "skills": [
            "User research",
            "Wireframing",
            "Prototyping",
            "Visual design principles",
            "Usability testing"
        ],
        "projects": [
            "Redesign a college website",
            "Create an app prototype",
            "Conduct a simple usability study"
        ],
        "url": "https://www.figma.com/resource-library/"
    },
    "Government Career Aspirant": {
        "icon": "🏛️",
        "description": (
            "Prepare for eligible public-sector recruitment examinations "
            "based on your education and career interests."
        ),
        "skills": [
            "General awareness",
            "Reasoning and aptitude",
            "Language skills",
            "Time management",
            "Regular mock-test practice"
        ],
        "projects": [
            "Create a weekly study timetable",
            "Track mock-test scores",
            "Maintain a current-affairs notebook"
        ],
        "url": "https://www.tnpsc.gov.in/"
    },
    "Digital Marketing Specialist": {
        "icon": "📱",
        "description": (
            "Help organisations reach audiences through digital "
            "content, campaigns and performance analysis."
        ),
        "skills": [
            "Content writing",
            "SEO fundamentals",
            "Social media strategy",
            "Analytics",
            "Campaign planning"
        ],
        "projects": [
            "Create a sample content calendar",
            "Build a mock campaign plan",
            "Analyse sample website traffic"
        ],
        "url": "https://skillshop.withgoogle.com/"
    }
}

selected_career = st.selectbox(
    "Choose a career that interests you",
    list(career_options.keys())
)

career = career_options[selected_career]

with st.container(border=True):
    st.markdown(f"## {career['icon']} {selected_career}")
    st.write(career["description"])

    st.markdown("### 🛠️ Skills to Learn")

    for skill in career["skills"]:
        st.markdown(f"- {skill}")

    st.markdown("### 🚀 Beginner Project Ideas")

    for project in career["projects"]:
        st.markdown(f"- {project}")

    st.link_button(
        "Explore Learning Resources ↗",
        career["url"],
        use_container_width=True
    )


# =========================================================
# STUDENT INTERESTS
# =========================================================

st.divider()
st.subheader("✨ Find a Direction That Interests You")

interests = st.multiselect(
    "Which areas would you like to explore?",
    [
        "Programming",
        "Data and Analytics",
        "Artificial Intelligence",
        "Cybersecurity",
        "Design and Creativity",
        "Government Jobs",
        "Business and Marketing",
        "Communication and Leadership"
    ],
    placeholder="Select one or more interests"
)

if st.button("Suggest Career Paths", use_container_width=True):

    suggestions = []

    interest_map = {
        "Programming": [
            "Software Developer",
            "Web Developer"
        ],
        "Data and Analytics": [
            "Data Analyst",
            "AI / Machine Learning Engineer"
        ],
        "Artificial Intelligence": [
            "AI / Machine Learning Engineer",
            "Data Analyst"
        ],
        "Cybersecurity": [
            "Cybersecurity Analyst"
        ],
        "Design and Creativity": [
            "UI / UX Designer",
            "Web Developer"
        ],
        "Government Jobs": [
            "Government Career Aspirant"
        ],
        "Business and Marketing": [
            "Digital Marketing Specialist",
            "Data Analyst"
        ],
        "Communication and Leadership": [
            "Digital Marketing Specialist",
            "Government Career Aspirant"
        ]
    }

    for interest in interests:
        for suggestion in interest_map[interest]:
            if suggestion not in suggestions:
                suggestions.append(suggestion)

    if suggestions:
        st.success("Here are some career paths you could explore:")

        for suggestion in suggestions:
            st.markdown(f"- **{suggestion}**")

        st.caption(
            "These suggestions are based on your selected interests. "
            "Explore the careers above to learn about their skills "
            "and beginner projects."
        )
    else:
        st.info("Select at least one interest to receive suggestions.")


# =========================================================
# CAREER PREPARATION CHECKLIST
# =========================================================

st.divider()
st.subheader("📝 Your Career Preparation Checklist")

st.write("Use this checklist to plan your next steps.")

st.checkbox("Choose one career path to explore")
st.checkbox("Identify the skills required for that career")
st.checkbox("Complete a beginner-level project")
st.checkbox("Prepare a resume and portfolio")
st.checkbox("Search for relevant internships or job opportunities")
st.checkbox("Practise interview questions regularly")


# =========================================================
# HELPFUL REMINDERS
# =========================================================

st.divider()

st.subheader("💡 Remember")

st.markdown("""
- Start with the fundamentals before moving to advanced topics.
- Build practical projects to demonstrate your skills.
- Use free learning resources whenever possible.
- Review job descriptions to understand employers' requirements.
- Choose a path that fits your interests, strengths and circumstances.
""")

st.page_link(
    "app.py",
    label="🏠 Back to Home",
    icon="🏠"
)
