import streamlit as st
import os
import json
from PIL import Image

# ---- PROJECT CONFIG ----
PROJECTS = {
    "Global Trendz Dashboard": {
        "folder": "project1_global_trendz",
        "title": "💼 Global Trendz Sales Dashboard",
        "link": "https://gbntjiwvxz5dndwaokcmuj.streamlit.app/",
        "skills": ["Python", "Excel", "Pandas", "Plotly", "Data Cleaning", "EDA"]
    },
    # Add more projects here
}

# ---- PAGE CONFIG ----
st.set_page_config(page_title="📁 Portfolio", layout="wide")

# ---- MAIN TITLE ----
st.markdown("""
    <h1 style='text-align: center; font-size: 3rem; margin-bottom: 0;'>👋 Welcome to Kassem's Portfolio</h1>
    <hr style='margin-top: 10px; margin-bottom: 30px; border: 1px solid #444;'>
""", unsafe_allow_html=True)

# ---- SIDEBAR ----
st.sidebar.header("📜 Sections")
section = st.sidebar.selectbox("Go to section", ["About Me"] + list(PROJECTS.keys()))

# ---- ABOUT ME SECTION ----
st.markdown("## 👤 About Me")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style='font-size: 1.15rem; line-height: 2.2;'>
        👋 Hi, I'm <strong>Kassem</strong>, a 24-year-old recent graduate from the Faculty of Specific Education, Cairo University (Class of 2024).<br><br>
        🎨 I started my career in design, mastering tools like <strong>Photoshop</strong> and <strong>Illustrator</strong>. In early 2025, I transitioned into <strong>Data Analysis</strong>.<br><br>
        📚 I’ve completed the following professional certificates:
        <ul style='padding-left: 20px; margin-top: 10px;'>
            <li>📘 Google Data Analytics Professional Certificate</li>
            <li>📗 IBM Data Analyst Professional Certificate</li>
            <li>📈 Excel for Data Analysis (Edraak)</li>
        </ul>
        🧠 I'm self-taught in <strong>Python</strong>, and skilled in data cleaning, EDA, and insight generation.<br>
        📈 Currently learning <strong>SQL</strong>, <strong>Power BI</strong>, and <strong>Tableau</strong>.<br><br>
        ⚙️ Daily tools: <strong>Excel</strong>, <strong>Python</strong>, <strong>Pandas</strong>, <strong>Plotly</strong>, <strong>Streamlit</strong>, and <strong>Jupyter Notebooks</strong>.<br>
        🤖 I use all available <strong>AI tools</strong> to boost productivity and outcomes.
    </div>
    """, unsafe_allow_html=True)

with col2:
    image_path = os.path.join("projects", "project1_global_trendz", "assets", "me.jpeg")
    if os.path.exists(image_path):
        st.image(Image.open(image_path), width=240, caption="👤 Kassem")
    else:
        st.warning("⚠️ Personal photo not found. Make sure 'me.jpeg' exists in the assets folder.")

st.markdown("<hr class='project-divider'>", unsafe_allow_html=True)

# ---- PROJECT SECTIONS ----
for project_key, project_info in PROJECTS.items():
    project_path = os.path.join("projects", project_info["folder"])
    slides_path = os.path.join(os.path.dirname(__file__), project_path, "slides.json")

    if os.path.exists(slides_path):
        with open(slides_path, encoding="utf-8") as f:
            slides = json.load(f)

        st.header(project_info["title"])

        if "link" in project_info and project_info["link"]:
            st.markdown(
                f"<div class='project-link'>🔗 <a href='{project_info['link']}' target='_blank'>View Full Project</a></div>",
                unsafe_allow_html=True,
            )

        if "skills" in project_info:
            st.markdown("""
            <div style='margin: 10px 0;'>
            """ +
            "".join([f"<span style='display: inline-block; background-color: #222; color: #fff; padding: 5px 10px; margin: 4px; border-radius: 8px;'>#{skill}</span>" for skill in project_info["skills"]]) +
            """</div>
            """, unsafe_allow_html=True)

        # Slideshow
        if f"index_{project_key}" not in st.session_state:
            st.session_state[f"index_{project_key}"] = 0

        current_index = st.session_state[f"index_{project_key}"]
        current_slide = slides[current_index]
        img_col, txt_col = st.columns([6, 6])

        with img_col:
            image_path = os.path.join(os.path.dirname(__file__), current_slide["image"])
            st.image(image_path, use_container_width=True)

        with txt_col:
            st.subheader(f"📌 {current_slide['title']}" if "title" in current_slide else "")
            st.markdown(f"<div class='description-text'>{current_slide['description']}</div>", unsafe_allow_html=True)

        col1, _, col3 = st.columns([1, 10, 1])
        with col1:
            if st.button("⬅", key=f"left_{project_key}"):
                st.session_state[f"index_{project_key}"] = (current_index - 1) % len(slides)
        with col3:
            if st.button("➡", key=f"right_{project_key}"):
                st.session_state[f"index_{project_key}"] = (current_index + 1) % len(slides)

        st.markdown("""
        <div class='description-text'>
        🧠 <strong>What I Learned:</strong><br>
        • How to automate Excel workflows with Python<br>
        • Building interactive charts with Plotly<br>
        • Organizing data for stakeholder-ready dashboards
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr class='project-divider'>", unsafe_allow_html=True)

# ---- CUSTOM STYLING ----
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
        color: #f0f0f0;
        background-color: #0e1117;
        min-height: 100vh;
    }

    .description-text {
        font-size: 1.3rem;
        color: #f0f0f0;
        line-height: 2.2;
        padding: 15px;
        border-radius: 12px;
        background-color: rgba(50, 50, 50, 0.4);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
        margin-top: 15px;
    }
    .project-link {
        text-align: center;
        margin-top: 20px;
    }
    .project-link a {
        color: #00c4ff;
        font-size: 1.2rem;
        text-decoration: none;
    }
    .project-divider {
        border: none;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        margin: 60px 0 40px;
    }
</style>
""", unsafe_allow_html=True)
