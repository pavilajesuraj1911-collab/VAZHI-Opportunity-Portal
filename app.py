from pathlib import Path
import base64
import streamlit as st

st.set_page_config(
    page_title="VAZHI | Opportunity for Everyone",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PHOTO_PATH = Path(__file__).parent / "assets" / "pavi.jpeg"

def image_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    ext = path.suffix.lower()
    mime = "image/png" if ext == ".png" else "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("utf-8")

pavi_photo = image_data_uri(PHOTO_PATH)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
  --green:#07513f; --deep:#063d31; --gold:#e9b94f; --cream:#fffaf0;
  --ink:#103d34; --muted:#49665e; --mint:#eaf5ef; --palegold:#fbf5e5;
}
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { background:#fff; color:var(--ink); }
[data-testid="stHeader"], [data-testid="stToolbar"], #MainMenu, footer { visibility:hidden; height:0; }
section[data-testid="stSidebar"] { display:none; }
.block-container { max-width:100%!important; padding:0!important; }
div[data-testid="stVerticalBlock"] { gap:.55rem; }
div[data-testid="stHorizontalBlock"] { gap:14px; }
h1,h2,h3,p { overflow-wrap:break-word; }

.topbar {
  width:100%; box-sizing:border-box; display:flex; align-items:center; justify-content:space-between;
  padding:12px clamp(22px,5.5vw,100px); background:#fff; border-bottom:1px solid #e9eee8;
}
.brand { display:flex; align-items:center; gap:12px; }
.brand-leaf { font-size:39px; line-height:1; }
.brand-name { font-size:29px; line-height:1; font-weight:800; letter-spacing:2px; color:var(--green); }
.brand-tag { font-size:9px; letter-spacing:3px; color:#7a8981; margin-top:6px; }

.hero {
  position:relative; isolation:isolate; box-sizing:border-box; width:100%; min-height:300px;
  padding:36px clamp(24px,5.6vw,100px); display:flex; align-items:center; overflow:hidden; color:#fff;
  background-image:linear-gradient(90deg,rgba(2,53,42,.97) 0%,rgba(4,66,51,.84) 40%,rgba(5,56,43,.20) 100%),
  url('https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=2400&q=90');
  background-size:cover; background-position:center 54%;
}
.hero-content { position:relative; z-index:2; width:min(790px,66%); }
.eyebrow { font-size:12px; font-weight:800; letter-spacing:4px; color:#f4c95f; margin-bottom:12px; }
.hero h1 { font:700 clamp(38px,3.25vw,58px)/1.06 'Playfair Display',serif; color:#fff; margin:0 0 12px; }
.hero h1 span { color:#f3c86e; }
.hero-copy { max-width:720px; font-size:17px; line-height:1.55; color:#fff; margin:0; }
.quote {
  position:absolute; right:clamp(28px,24vw,420px); top:25%; z-index:2; max-width:320px;
  box-sizing:border-box; padding:18px 22px; border-left:5px solid var(--gold); border-radius:10px;
  color:#183a32; background:rgba(255,255,255,.78); box-shadow:0 10px 32px #002b201a;
  font:italic 600 20px/1.4 'Playfair Display',serif;
}
.feature-area { padding:16px clamp(22px,5.5vw,100px) 12px; }
.feature-card { min-height:128px; box-sizing:border-box; display:flex; align-items:flex-start; gap:16px; padding:19px 20px; border:1px solid #e6e9de; border-radius:15px; box-shadow:0 7px 20px #193d2d0a; }
.feature-card.mint { background:linear-gradient(135deg,#edf7f1,#e5f2eb); }
.feature-card.gold { background:linear-gradient(135deg,#fffaf0,#f8f2df); }
.feature-icon { width:58px; height:58px; min-width:58px; display:flex; align-items:center; justify-content:center; border-radius:50%; color:#fff; background:var(--green); font-size:27px; }
.feature-card.gold .feature-icon { background:#eac36a; color:#34280b; }
.feature-card h3 { font:700 21px 'Playfair Display',serif; color:var(--deep); margin:2px 0 5px; }
.feature-card p { font-size:14px; line-height:1.45; color:#31594e; margin:0; }

.stats { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); padding:15px clamp(22px,5.5vw,100px); background:#f5f8f3; border-block:1px solid #edf0e8; }
.stat { display:flex; align-items:center; justify-content:center; gap:15px; padding:5px 12px; border-right:1px solid #d9e1d8; }
.stat:last-child { border-right:0; }
.stat-icon { font-size:31px; }
.stat strong { display:block; color:var(--deep); font-size:27px; line-height:1.1; }
.stat span { font-size:13px; color:#31574f; }

.lower { padding:24px clamp(22px,5.5vw,100px) 16px; }
.kicker { font-size:10px; letter-spacing:3px; color:#b3842c; font-weight:800; margin-bottom:7px; }
.section-title { font:700 clamp(25px,2vw,32px) 'Playfair Display',serif; color:var(--deep); margin:0 0 10px; }
.copy { font-size:15px; line-height:1.65; color:#35574f; margin:0; }
.benefits { display:flex; justify-content:space-between; gap:14px; margin-top:18px; }
.benefit { display:flex; align-items:center; gap:10px; font-size:14px; font-weight:700; color:#173f36; }
.benefit span { font-size:29px; }
.creator-head { padding:0 0 12px; }
.creator-row { display:flex; align-items:center; gap:16px; width:100%; }
.creator-photo,.photo-placeholder { display:block; flex:0 0 150px; width:150px; height:155px; object-fit:cover; object-position:center 25%; border-radius:15px; border:1px solid #dfe5df; box-shadow:0 5px 18px #0001; }
.creator-note-wrap { flex:1 1 auto; min-width:0; }
.creator-row .note { width:100%; box-sizing:border-box; }
.creator-section { padding:24px clamp(22px,5.5vw,100px) 0; }
.creator-section-inner { display:flex; align-items:flex-start; gap:24px; }
.creator-intro { flex:0 0 45%; min-width:0; }
.creator-story { flex:1 1 55%; min-width:0; }
.creator-intro .lower { padding:0; }
.creator-cta-spacer { height:24px; }
.photo-placeholder { display:flex; align-items:center; justify-content:center; background:var(--mint); color:var(--green); font-size:48px; }
.note { background:linear-gradient(135deg,#fffdf7,#fffaf0); border:1px solid #efe8d8; border-left:5px solid #e9c36c; border-radius:12px; padding:17px 21px; }
.note h3 { font:700 21px 'Playfair Display',serif; color:var(--deep); margin:0 0 8px; }
.note p { font-size:13px; line-height:1.55; color:#35574f; margin:0 0 8px; }
.signature { font:italic 17px 'Playfair Display',serif; color:#8c7958; }

.cta { margin:38px clamp(22px,5.5vw,100px) 0; padding:16px 22px; border-radius:13px; color:#fff; background:linear-gradient(105deg,#07503d,#0c674d); display:flex; align-items:center; justify-content:space-between; gap:18px; box-shadow:0 8px 24px #064b3b20; }
.cta strong { font-size:17px; }
.cta small { display:block; color:#e5f0e9; font-size:13px; margin-top:3px; }
.footer { padding:14px 24px 18px; text-align:center; color:#718078; font-size:11px; }

div[data-testid="stPageLink"] a {
  background:var(--green)!important; color:#fff!important; border:1px solid var(--green)!important;
  border-radius:9px!important; padding:10px 14px!important; min-height:38px!important;
  display:flex!important; align-items:center!important; justify-content:center!important;
  font-size:12px!important; font-weight:700!important; white-space:normal!important;
  text-align:center!important; transition:all .18s ease!important;
}
div[data-testid="stPageLink"] a:hover { background:#0d6a50!important; border-color:#0d6a50!important; transform:translateY(-1px); }
/* The four feature-card links should look like compact buttons, not full-width bars. */
div[data-testid="stHorizontalBlock"]:has(> div[data-testid="stColumn"]:nth-child(4)) div[data-testid="stPageLink"] a {
  width:fit-content!important; display:inline-flex!important; padding:9px 15px!important;
}
@media(max-width:1050px) {
  .hero { min-height:320px; }
  .hero-content { width:72%; }
  .quote { right:25px; max-width:260px; font-size:17px; }
  .feature-card { min-height:150px; padding:15px; gap:11px; }
  .feature-icon { width:48px; height:48px; min-width:48px; font-size:23px; }
}
@media(max-width:760px) {
  .topbar { padding:12px 18px; }
  .brand-name { font-size:25px; }
  .hero { min-height:390px; align-items:flex-start; padding:34px 22px; }
  .hero-content { width:100%; }
  .hero-copy { font-size:15px; }
  .quote { position:relative; top:auto; right:auto; margin:18px 0 0; max-width:100%; font-size:17px; }
  .stats { grid-template-columns:repeat(2,minmax(0,1fr)); }
  .stat:nth-child(2) { border-right:0; }
  .creator-section-inner { flex-direction:column; gap:20px; }
  .creator-intro,.creator-story { flex:1 1 auto; width:100%; }
  .creator-row { gap:12px; }
  .creator-photo,.photo-placeholder { flex-basis:120px; width:120px; height:135px; }
  .benefits { flex-wrap:wrap; justify-content:flex-start; }
}
@media(max-width:480px) {
  .stats { grid-template-columns:1fr; }
  .stat { border-right:0; border-bottom:1px solid #d9e1d8; justify-content:flex-start; padding:12px 20px; }
  .stat:last-child { border-bottom:0; }
  .feature-card { min-height:unset; }
}
</style>
""", unsafe_allow_html=True)

# Brand
st.markdown("""
<div class="topbar">
  <div class="brand">
    <div class="brand-leaf">🌱</div>
    <div><div class="brand-name">VAZHI</div><div class="brand-tag">OPPORTUNITY FOR EVERYONE</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# Navigation
nav_cols = st.columns([.72, 1.05, 1.3, .95, 1.12, 1.15, 1.05, 1.05], gap="small")
nav_items = [
    ("🏠 Home", "app.py"), ("🎓 Scholarships", "pages/2_Scholarships.py"),
    ("🏛️ Government Jobs", "pages/3_Government_Jobs.py"), ("💼 Internships", "pages/4_Internships.py"),
    ("📊 My Dashboard", "pages/5_My_Dashboard.py"), ("📖 Career Guidance", "pages/6_Career_Guidance.py"),
    ("ⓘ About VAZHI", "pages/7_About_VAZHI.py"), ("🔐 Student Login", "pages/1_Student_Login.py"),
]
for column, (label, page) in zip(nav_cols, nav_items):
    with column:
        st.page_link(page, label=label, use_container_width=True)

# Hero banner
st.markdown("""
<section class="hero">
  <div class="hero-content">
    <div class="eyebrow">YOUR FUTURE STARTS HERE</div>
    <h1>Big Dreams.<br><span>Boundless Possibilities.</span></h1>
    <p class="hero-copy">Scholarships, government jobs, internships and career guidance — all in one student-friendly place. Discover opportunities and take your next step with confidence.</p>
  </div>
  <div class="quote">“Your village is your origin,<br> not your limitation.”</div>
</section>
""", unsafe_allow_html=True)

# Opportunity cards
feature_cols = st.columns(4, gap="medium")
feature_items = [
    ("🎓", "Scholarships", "Find financial support for your education.", "pages/2_Scholarships.py", "mint", "Explore Scholarships →"),
    ("🏛️", "Government Jobs", "Explore official recruitment and exam resources.", "pages/3_Government_Jobs.py", "gold", "Explore Government Jobs →"),
    ("💼", "Internships", "Discover internships to build practical skills.", "pages/4_Internships.py", "mint", "Explore Internships →"),
    ("📖", "Career Guidance", "Tips, roadmaps and resources for your future.", "pages/6_Career_Guidance.py", "gold", "Get Guidance →"),
]
for column, (icon, title, description, page, tone, button_label) in zip(feature_cols, feature_items):
    with column:
        st.markdown(
            f"<div class='feature-area'><div class='feature-card {tone}'><div class='feature-icon'>{icon}</div><div><h3>{title}</h3><p>{description}</p></div></div></div>",
            unsafe_allow_html=True,
        )
        st.page_link(page, label=button_label, use_container_width=False)

# Quick stats
st.markdown("""
<div class="stats">
  <div class="stat"><div class="stat-icon">👥</div><div><strong>10,000+</strong><span>Students Supported</span></div></div>
  <div class="stat"><div class="stat-icon">🎓</div><div><strong>500+</strong><span>Scholarship Resources</span></div></div>
  <div class="stat"><div class="stat-icon">📄</div><div><strong>1,000+</strong><span>Government Job Updates</span></div></div>
  <div class="stat"><div class="stat-icon">💼</div><div><strong>800+</strong><span>Internship Opportunities</span></div></div>
</div>
""", unsafe_allow_html=True)

# Intro + creator note — use one HTML flex row to keep the creator photo beside the note
photo_html = (
    f'<img class="creator-photo" src="{pavi_photo}" alt="Pavi, creator of VAZHI">'
    if pavi_photo else '<div class="photo-placeholder">🌱</div>'
)
st.markdown(f"""
<div class="creator-section">
  <div class="creator-section-inner">
    <div class="creator-intro">
      <div class="lower">
        <div class="kicker">A NEW BEGINNING</div>
        <h2 class="section-title">Your dreams deserve a direction.</h2>
        <p class="copy">Finding opportunities should not be difficult because of where you live. VAZHI brings useful education and career resources together, so students can explore what is possible and plan what comes next.</p>
        <div class="benefits">
          <div class="benefit"><span>🎯</span><div>Discover<br>Opportunities</div></div>
          <div class="benefit"><span>📈</span><div>Build<br>Your Skills</div></div>
          <div class="benefit"><span>👨‍👩‍👧</span><div>Create a<br>Brighter Future</div></div>
        </div>
      </div>
    </div>
    <div class="creator-story">
      <div class="creator-head">
        <div class="kicker">THE HEART BEHIND VAZHI</div>
        <h2 class="section-title">A Note from the Creator</h2>
      </div>
      <div class="creator-row">
        {photo_html}
        <div class="creator-note-wrap">
          <div class="note">
            <div class="kicker">FOUNDER'S NOTE</div>
            <h3>Hi, I’m Pavi — the creator of VAZHI.</h3>
            <p>I created VAZHI with one simple thought: a student's future should not be limited by a lack of information.</p>
            <p>Many students, especially from villages and first-generation learner families, may not know where to find scholarships, internships or government job notifications. VAZHI aims to make these opportunities easier to discover in one welcoming place.</p>
            <div class="signature">Pavi <span style="font:normal 12px 'DM Sans',sans-serif">· Creator of VAZHI</span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cta">
  <div><strong>🌱 &nbsp; Ready to start your journey?</strong><small>Join students who are exploring new opportunities with VAZHI.</small></div>
</div>
""", unsafe_allow_html=True)
st.markdown("<div class='creator-cta-spacer'></div>", unsafe_allow_html=True)
cta_cols = st.columns([3, 2, 3])
with cta_cols[1]:
    st.markdown("<div style='padding-top:8px'></div>", unsafe_allow_html=True)
    st.page_link("pages/1_Student_Login.py", label="Create Your Free Account →", use_container_width=True)

st.markdown(
    "<div class='footer'>VAZHI · Opportunity for Everyone · Verify every opportunity on its official website before applying.</div>",
    unsafe_allow_html=True,
)
