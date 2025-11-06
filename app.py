import streamlit as st
import requests
gradio_url = "https://af1e7458e4ba7b1a74.gradio.live"

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



    



