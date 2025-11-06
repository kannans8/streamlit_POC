import streamlit as st

st.title("🎨 Embedded Gradio App")
gradio_url = "https://ce0fd43838549f4a9b.gradio.live"
st.components.v1.iframe(gradio_url, height=800, scrolling=True)
