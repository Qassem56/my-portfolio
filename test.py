import streamlit as st

about_me_html = """
<div style='padding: 25px 30px; background-color: rgba(255, 255, 255, 0.05); border-radius: 12px; margin-bottom: 30px;'>
    <h2 style='margin-bottom: 25px;'>👤 About Me</h2>

    <div style='font-size: 1.15rem; line-height: 2;'>
        <p>👋 Hi, I'm <strong>Kassem</strong>, a 24-year-old recent graduate from the Faculty of Specific Education, Cairo University (Class of 2024).</p>
        <p>🎨 I started my career in design, mastering tools like <strong>Photoshop</strong> and <strong>Illustrator</strong>. In early 2025, I transitioned into <strong>Data Analysis</strong>.</p>
        <p>📚 I’ve completed the following professional certificates:</p>
        <ul style='padding-left: 20px; line-height: 1.8; margin-top: 10px;'>
            <li>📘 Google Data Analytics Professional Certificate</li>
            <li>📗 IBM Data Analyst Professional Certificate</li>
            <li>📊 Excel for Data Analysis (Edraak)</li>
        </ul>
        <p>🧠 I’m self-taught in <strong>Python</strong>, and skilled in data cleaning, EDA, and insight generation. Currently learning <strong>SQL</strong>, <strong>Power BI</strong>, and <strong>Tableau</strong>.</p>
        <p>⚙️ Daily tools: <strong>Excel</strong>, <strong>Python</strong>, <strong>Pandas</strong>, <strong>Plotly</strong>, <strong>Streamlit</strong>, and <strong>Jupyter</strong> Notebooks.<br>
        🤖 I also use all the <strong>AI tools</strong> to enhance productivity and outcomes.</p>
    </div>
</div>
"""

st.markdown(about_me_html, unsafe_allow_html=True)