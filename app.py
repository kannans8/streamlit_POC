import streamlit as st
import requests
st.set_page_config(layout="wide")
gradio_url = "https://f1e4ed93361006f676.gradio.live"
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



    



