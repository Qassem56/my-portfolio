import streamlit as st

# Define list of projects
projects = [
    {
        "title": "Global Trendz Sales Dashboard",
        "image": "project1_img.png",  # replace with actual image
        "description": """
        This dashboard was developed for **Global Trendz**, a regional retail company operating in the **Gulf & Egypt**.

        ✅ Tracks total sales, orders, top-performing products and countries.
        ✅ Allows filtering by product, country, and date range.
        ✅ Features dynamic KPIs and interactive visualizations (bar, pie, line).
        ✅ Export filtered results as CSV/Excel.
        ✅ Built with Streamlit and Plotly.
        
        🔗 [Open App](https://gbntjiwvxz5dndwaokcmuj.streamlit.app)
        
        📁 [View Code](https://github.com/your_username/global-trendz-dashboard)
        📄 [Download Summary PDF](global_trendz_summary.pdf)
        """
    },
    # Add more projects here later
]

# Page config
st.set_page_config(page_title="📁 Portfolio - Data Projects", layout="wide")
st.title("💼 My Data Projects Portfolio")

# Sidebar to choose project
project_titles = [p["title"] for p in projects]
selected_title = st.sidebar.radio("🧭 Select a project:", project_titles)

# Get selected project info
selected_project = next(p for p in projects if p["title"] == selected_title)

# Layout
col1, col2 = st.columns([1, 2])
with col1:
    st.image(selected_project["image"], use_column_width=True)

with col2:
    st.subheader(f"📌 {selected_project['title']}")
    st.markdown(selected_project['description'])
