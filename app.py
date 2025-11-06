import streamlit as st

st.title("🎨 Embedded Gradio App")
gradio_url = "https://83ccda4172f294dff2.gradio.live"
st.components.v1.iframe(gradio_url, height=800, scrolling=True)
