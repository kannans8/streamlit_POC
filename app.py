import streamlit as st
import requests
import base64
st.set_page_config(layout="wide")

base64_img = get_base64_of_bin_file("Picture1.png")

st.markdown(
    """
    <style>

        .stApp {
            background: url("data:image/jpg;base64,"""+base64_img+""" ") no-repeat center center fixed;
            background-size: cover;
            background-position: center 25px;
        }

    </style>

    <div class="title">Crawler AI_V2</div>
    <div style="position: fixed; bottom: 10px; left: 100px; color: white; font-size: 20px;">
        Gemini API used
    </div>
    """,
    unsafe_allow_html=True
)




gradio_url = "https://f9fe2e123b4a9f88bd.gradio.live/"
st.components.v1.html(
    f"""
    <iframe src="{gradio_url}" 
            width="100%" 
            height="800" 
            style="border:none;" 
            scrolling="yes">
    </iframe>
    """,
    height=800
)



    



