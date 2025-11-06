import streamlit as st
import requests
st.set_page_config(layout="wide")
gradio_url = "https://d8f785e4a6f8249882.gradio.live"
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



    



