import streamlit as st
import requests


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



    



