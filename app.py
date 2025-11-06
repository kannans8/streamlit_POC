import streamlit as st

gradio_url = "https://ce0fd43838549f4a9b.gradio.live"
st.components.v1.iframe(gradio_url,     width=1800,  
    height=800, 
    scrolling=True )
