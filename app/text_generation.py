import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

def text_generation_tab():
    st.header("🧠 Gemini Text Generation")

    # Load API key
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

    prompt = st.text_area("Enter your prompt", "Explain Data Science vs Machine Learning for a 10-year-old")

    if st.button("Generate"):
        with st.spinner("Generating..."):
            model = genai.GenerativeModel("gemini-2.0-flash")
            response = model.generate_content(prompt)
            st.markdown(response.text)
