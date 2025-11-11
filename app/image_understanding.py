import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import os

def image_understanding_tab():
    st.header("🖼️ Gemini Image Understanding")

    # Load API key
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

    # Upload Image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Optional custom user query
    user_query = st.text_area(
        "Enter your query about the image (optional)",
        placeholder="e.g., What emotions do you see? or Describe this image in 3 points."
    )

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Analyze Image"):
            with st.spinner("Analyzing the image using Gemini..."):
                model = genai.GenerativeModel("gemini-2.5-flash")

                # Combine query and image in prompt
                if user_query.strip():
                    prompt = user_query
                else:
                    prompt = "Explain what you see in this image."

                response = model.generate_content([prompt, image])
                st.markdown("### 🧾 Gemini’s Response:")
                st.markdown(response.text)
