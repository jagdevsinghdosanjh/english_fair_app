# modules/english_circles.py

import streamlit as st
from utils.helpers import mark_module_complete, display_badges, poetic_prompt

# After activity is completed
mark_module_complete("English Circles")

# Show poetic reflection
st.markdown(f"🪞 {poetic_prompt()}")

# Show earned badges
display_badges()


def render():
    st.header("🔵 English Circles Stall")
    st.markdown("""
    _Step into the circle where words are not just learned—they're lived._

    This stall invites you to explore basic English through:
    - 🔤 Vocabulary building
    - 🗣️ Simple sentence formation
    - 🎭 Expressive speaking
    """)

    st.subheader("🧠 Word of the Circle")
    word = st.selectbox("Choose a word to explore:", ["apple", "run", "happy", "school", "friend"])
    st.write(f"**Definition**: _(Click to reveal)_")
    with st.expander("Reveal Meaning"):
        meanings = {
            "apple": "A sweet fruit often red or green.",
            "run": "To move quickly on foot.",
            "happy": "Feeling joy or pleasure.",
            "school": "A place where students learn.",
            "friend": "Someone you care about and trust."
        }
        st.write(meanings[word])

    st.subheader("✍️ Make a Sentence")
    sentence = st.text_input(f"Use '{word}' in a sentence:")
    if sentence:
        st.success("Beautiful! Your sentence adds a new thread to the circle.")

    st.subheader("🎭 Speak It Aloud")
    st.markdown("Try saying your sentence aloud. Imagine you're teaching it to someone younger than you.")

    st.markdown("---")
    st.markdown("🌱 _Every word you plant here grows into a forest of understanding._")
