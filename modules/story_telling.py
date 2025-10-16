# modules/story_telling.py

import streamlit as st
import random

def render():
    st.header("📖 Story Telling Corner")
    st.markdown("""
    _Where imagination meets expression, and every picture hides a tale._

    Choose a storytelling mode:
    """)

    mode = st.radio("Select Mode", ["Picture-Based", "Situational Prompt"])

    if mode == "Picture-Based":
        st.subheader("🖼️ Caption This Image")
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/ca/Mauritius_fody_%28Foudia_rubra%29_male_2.jpg", caption="What’s happening here?")
        story = st.text_area("Write a short story or caption inspired by this image:")
        if story:
            st.success("Your story adds color to the canvas of imagination!")

    elif mode == "Situational Prompt":
        st.subheader("🎭 Situational Story Prompt")
        prompts = [
            "You wake up and find you can understand animals. What happens next?",
            "A mysterious letter arrives with no sender. What does it say?",
            "You are the last person on Earth who remembers how to read."
        ]
        chosen = random.choice(prompts)
        st.markdown(f"**Prompt:** _{chosen}_")
        response = st.text_area("Your story:")
        if response:
            st.success("Beautiful! Your story brings the prompt to life.")

    st.markdown("---")
    st.markdown("Disciple and Discipline One seeks the light, the other is the lamp. One asks the question, the other is the silence between words. One walks, the other is the path. Together, they become the dance of becoming.")
    st.markdown("🪶 _Every story told here becomes a thread in the tapestry of learning._")
