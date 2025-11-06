import streamlit as st
import requests
gradio_url = "https://2fe477cc111f555252.gradio.live"
response = requests.get(gradio_url, timeout=timeout)
if (response.status_code >= 200 and response.status_code < 400):
    
    try:
    
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

else :
    st.markdown("## Site is down now . Try later")


    



