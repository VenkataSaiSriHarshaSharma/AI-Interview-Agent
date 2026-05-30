import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

st.title("AI Interview Agent")

if st.button("Test Gemini"):

    response = model.generate_content(
        "Say Hello Harsha"
    )

    st.success(response.text)