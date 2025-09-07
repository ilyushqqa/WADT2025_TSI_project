import streamlit as st
from pathlib import Path

st.set_page_config(page_title="IT Courses", layout="wide")
html = Path('templates/index.html').read_text()
st.components.v1.html(html, height=4000, scrolling=True)
