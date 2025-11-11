import streamlit as st
from text_generation import text_generation_tab
from image_understanding import image_understanding_tab

st.set_page_config(page_title="Gemini AI Demos", layout="wide")

st.title("🌟 Gemini AI Demos")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose Feature", ["Text Generation", "Image Understanding"])

if page == "Text Generation":
    text_generation_tab()
elif page == "Image Understanding":
    image_understanding_tab()
