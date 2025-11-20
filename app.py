import streamlit as st
import requests
import base64
st.set_page_config(layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
    
base64_img = get_base64_of_bin_file("Pic1.png")

st.markdown(
    """
    <style>

        .stApp {
            background: url("data:image/jpg;base64,"""+base64_img+""" ") no-repeat center center fixed;
            background-size: cover;
            background-position: center 25px;
        }

    </style>


    </div>
    """,
    unsafe_allow_html=True
)




gradio_url = "https://c1d14d1671909de189.gradio.live/"
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



    



