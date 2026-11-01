
import streamlit as st
from html import escape
from utils import inject_css

# ==================================================
# VAZHI - MY DASHBOARD
# ==================================================

st.set_page_config(
    page_title="My Dashboard | VAZHI",
    page_icon="📊",
    layout="wide"
)

inject_css()

# ==================================================
# CUSTOM DESIGN
# ==================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: #f7f9f5;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    section[data-testid="stSidebar"] {
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

    .hero {
        background: linear-gradient(120deg, #105b43, #168363);
        padding: 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 22px;
    }

    .hero h1 {
        color: white;
        font-size: 34px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #f2f8f3;
        font-size: 16px;
    }

    .section-title {
        color: #155c45;
        font-size: 23px;
        font-weight: 700;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    .info-card {
        background: white;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #e3e9e1;
        min-height: 135px;
        box-shadow: 0 3px 12px rgba(0,0,0,0.04);
    }

    .info-card h3 {
        color: #155c45;
        font-size: 19px;
    }

    .info-card p {
        color: #5b655f;
        font-size: 14px;
    }

    .metric-card {
        background: white;
        border-left: 5px solid #168363;
        border-radius: 12px;
        padding: 17px;
        min-height: 105px;
        box-shadow: 0 2px 9px rgba(0,0,0,0.04);
    }

    .metric-label {
        color: #68736c;
        font-size: 14px;
    }

    .metric-value {
        color: #155c45;
        font-size: 24px;
        font-weight: 750;
        margin-top: 8px;
        overflow-wrap: anywhere;
    }

    .quote-card {
        background: #fff4d6;
        border: 1px solid #f0d58b;
        border-radius: 15px;
        padding: 24px;
        color: #594619;
        text-align: center;
        margin-top: 22px;
    }

    .bar-track {
        background: #e6eee7;
        border-radius: 10px;
        height: 14px;
        width: 100%;
        overflow: hidden;
    }

    .bar-fill {
        background: linear-gradient(90deg, #168363, #72b85a);
        height: 14px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==================================================
# SESSION DATA
# ==================================================

if "vazhi_dashboard_tasks" not in st.session_state:
    st.session_state.vazhi_dashboard_tasks = {
        "Update my resume": False,
        "Explore scholarships": False,
        "Find an internship": False,
        "Practise a technical skill": False,
        "Complete a learning module": False,
        "Plan my career goal": False
    }

if "vazhi_dashboard_reviewed" not in st.session_state:
    st.session_state.vazhi_dashboard_reviewed = []

if "vazhi_dashboard_education" not in st.session_state:
    st.session_state.vazhi_dashboard_education = "Postgraduate"

if "vazhi_dashboard_goal" not in st.session_state:
    st.session_state.vazhi_dashboard_goal = "Get a job"

if "vazhi_dashboard_interests" not in st.session_state:
    st.session_state.vazhi_dashboard_interests = [
        "Programming",
        "Web Development"
    ]

# ==================================================
# HEADER
# ==================================================

user = st.session_state.get("vazhi_user")

if isinstance(user, dict):
    student_name = (
        user.get("name")
        or user.get("full_name")
        or "Student"
    )
else:
    student_name = "Student"

student_name = escape(str(student_name))

st.markdown(
    f"""
    <div class="hero">
        <h1>📊 My Dashboard</h1>
        <p>Welcome, {student_name}!</p>
        <p>
            Track your goals, discover opportunities,
            and take one step closer to your future.
        </p>
        <p>🌱 VAZHI — Opportunity for Everyone</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.caption(
    "Explore opportunities without logging in. "
    "Your dashboard selections are temporary and are not "
    "permanently saved to your account."
)

# ==================================================
# STUDENT PROFILE
# ==================================================

st.markdown(
    '<div class="section-title">👤 My Learning Profile</div>',
    unsafe_allow_html=True
)

profile_col1, profile_col2 = st.columns(2)

with profile_col1:
    education = st.selectbox(
        "Current education",
        [
            "School Student",
            "Diploma Student",
            "Undergraduate",
            "Postgraduate",
            "Graduate",
            "Working Professional"
        ],
        key="vazhi_dashboard_education"
    )

with profile_col2:
    goal = st.selectbox(
        "My main goal",
        [
            "Get a job",
            "Find an internship",
            "Apply for scholarships",
            "Prepare for government exams",
            "Improve technical skills",
            "Explore career options",
            "Start a business"
        ],
        key="vazhi_dashboard_goal"
    )

interests = st.multiselect(
    "Choose your interests",
    [
        "Programming",
        "Web Development",
        "Data Analytics",
        "Artificial Intelligence",
        "Cybersecurity",
        "UI/UX Design",
        "Government Exams",
        "Business and Marketing",
        "Communication and Leadership",
        "Cloud Computing"
    ],
    key="vazhi_dashboard_interests"
)

if st.button("💾 Save My Choices", type="primary"):
    st.success(
        "Your choices are available for this session. "
        "Permanent database saving is not configured."
    )

# ==================================================
# DASHBOARD METRICS
# ==================================================

st.markdown(
    '<div class="section-title">✨ My Overview</div>',
    unsafe_allow_html=True
)

tasks = st.session_state.vazhi_dashboard_tasks
completed_count = sum(tasks.values())
total_tasks = len(tasks)

progress_percentage = (
    int(completed_count / total_tasks * 100)
    if total_tasks else 0
)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">🎓 Education</div>
            <div class="metric-value">{escape(education)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m2:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">🎯 Main Goal</div>
            <div class="metric-value">{escape(goal)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m3:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">💡 Interests</div>
            <div class="metric-value">{len(interests)}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with m4:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">✅ Tasks Completed</div>
            <div class="metric-value">{completed_count}/{total_tasks}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ==================================================
# INTEREST CHART - NO NUMPY OR PANDAS
# ==================================================

st.markdown(
    '<div class="section-title">📈 My Interest Chart</div>',
    unsafe_allow_html=True
)

if interests:
    st.write("Your selected learning areas:")

    for interest in interests:
        safe_interest = escape(interest)

        st.markdown(
            f"""
            <div style="margin-bottom:16px;">
                <div style="display:flex; justify-content:space-between;
                            margin-bottom:5px;">
                    <span style="font-weight:600;">{safe_interest}</span>
                    <span style="color:#168363;">Selected</span>
                </div>
                <div class="bar-track">
                    <div class="bar-fill" style="width:100%;"></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.caption(
        "These bars show selected interests, not your skill level."
    )
else:
    st.info(
        "Choose your interests in the profile section "
        "to see them displayed here."
    )

# ==================================================
# OPPORTUNITY CARDS
# ==================================================

st.markdown(
    '<div class="section-title">🚀 Explore Opportunities</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="info-card">
            <h3>🎓 Scholarships</h3>
            <p>
                Discover scholarship resources and financial
                support for your education.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/2_Scholarships.py",
        label="Explore Scholarships",
        icon="🎓",
        use_container_width=True
    )

with c2:
    st.markdown(
        """
        <div class="info-card">
            <h3>🏛️ Government Jobs</h3>
            <p>
                Explore official recruitment websites and
                government career opportunities.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/3_Government_Jobs.py",
        label="Explore Government Jobs",
        icon="🏛️",
        use_container_width=True
    )

with c3:
    st.markdown(
        """
        <div class="info-card">
            <h3>💼 Internships</h3>
            <p>
                Explore internship platforms and gain
                practical experience.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/4_Internships.py",
        label="Explore Internships",
        icon="💼",
        use_container_width=True
    )

# ==================================================
# CAREER GUIDANCE
# ==================================================

st.markdown(
    '<div class="section-title">🧭 Plan Your Career</div>',
    unsafe_allow_html=True
)

career_col1, career_col2 = st.columns([2, 1])

with career_col1:
    st.markdown(
        """
        <div class="info-card">
            <h3>🌟 Build Your Future</h3>
            <p>
                Discover career paths, learn useful skills,
                explore project ideas, and plan your next step.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with career_col2:
    st.write("")
    st.write("")
    st.page_link(
        "pages/6_Career_Guidance.py",
        label="Career Guidance",
        icon="🧭",
        use_container_width=True
    )

# ==================================================
# TASK TRACKER
# ==================================================

st.markdown(
    '<div class="section-title">✅ My Progress Tracker</div>',
    unsafe_allow_html=True
)

st.write("Tick a task when you complete it.")

for task in list(tasks.keys()):
    current_value = tasks[task]

    new_value = st.checkbox(
        task,
        value=current_value,
        key=f"vazhi_task_{task}"
    )

    if new_value != tasks[task]:
        tasks[task] = new_value
        st.rerun()

completed_count = sum(tasks.values())

progress_percentage = (
    int(completed_count / total_tasks * 100)
    if total_tasks else 0
)

st.progress(
    progress_percentage,
    text=f"Your progress: {progress_percentage}%"
)

if progress_percentage == 100:
    st.success("🎉 Excellent! You completed every task.")
elif progress_percentage >= 50:
    st.info("👏 Great progress! Keep moving towards your goal.")
else:
    st.caption("Every small step counts. Keep going!")

# ==================================================
# WEEKLY LEARNING PLAN
# ==================================================

st.markdown(
    '<div class="section-title">📅 My Weekly Learning Plan</div>',
    unsafe_allow_html=True
)

weekly_plan = {
    "Monday": "🐍 Practise programming fundamentals",
    "Tuesday": "🌐 Learn web development",
    "Wednesday": "🗄️ Revise databases and SQL",
    "Thursday": "🧠 Explore data analytics or AI",
    "Friday": "📄 Improve your resume",
    "Saturday": "💼 Explore internships and jobs",
    "Sunday": "🎯 Review your weekly progress"
}

selected_day = st.selectbox(
    "Choose a day",
    list(weekly_plan.keys()),
    key="vazhi_learning_day"
)

st.markdown(
    f"""
    <div class="info-card">
        <h3>{escape(selected_day)}'s Learning Goal</h3>
        <p>{escape(weekly_plan[selected_day])}</p>
    </div>
    """,
    unsafe_allow_html=True
)

if selected_day in st.session_state.vazhi_dashboard_reviewed:
    st.success("You have reviewed this day's learning plan.")
else:
    if st.button("☑️ Mark Plan as Reviewed"):
        st.session_state.vazhi_dashboard_reviewed.append(
            selected_day
        )
        st.rerun()

# ==================================================
# QUICK NAVIGATION
# ==================================================

st.markdown(
    '<div class="section-title">⚡ Quick Access</div>',
    unsafe_allow_html=True
)

q1, q2, q3 = st.columns(3)

with q1:
    st.page_link(
        "app.py",
        label="🏠 Home",
        use_container_width=True
    )

with q2:
    st.page_link(
        "pages/1_Student_Login.py",
        label="🔐 Student Login",
        use_container_width=True
    )

with q3:
    st.page_link(
        "pages/7_About_VAZHI.py",
        label="🌱 About VAZHI",
        use_container_width=True
    )

# ==================================================
# FOOTER
# ==================================================

st.markdown(
    """
    <div class="quote-card">
        <h3>🌱 Believe in Your Journey</h3>
        <p style="font-size:18px;">
            "Your village is your origin, not your limitation."
        </p>
        <p>
            Learn something today. Build something tomorrow.
            Create your future with VAZHI.
        </p>
        <strong>VAZHI | Opportunity for Everyone</strong>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")
st.caption("VAZHI · Learn • Explore • Grow")
