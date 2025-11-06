import streamlit as st

try:
    
    gradio_url = "https://2fe477cc111f555252.gradio.live"
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
except Exception :
    st.markdown("## Site is down now . Try later")

    



