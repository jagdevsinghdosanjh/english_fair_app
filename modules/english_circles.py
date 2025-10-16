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
    word = st.selectbox("Choose a word to explore:", ["apple", "run", "happy", "school", "friend","book","laugh","tree","kind","water","play","light","home","dream","learn"])
    st.write("**Definition**: _(Click to reveal)_")
    with st.expander("Reveal Meaning"):
        meanings = {
            "apple": "A sweet fruit often red or green.",
            "run": "To move quickly on foot.",
            "happy": "Feeling joy or pleasure.",
            "school": "A place where students learn.",
            "friend": "Someone you care about and trust.",
            "book": "A set of written pages bound together, often telling a story or sharing knowledge.",
            "laugh": "To make a joyful sound when something is funny or delightful.",
            "tree": "A tall plant with a trunk, branches, and leaves that gives shade and oxygen.",
            "kind": "Showing care and respect for others through words or actions.",
            "water": "A clear liquid that all living things need to survive.",
            "play": "To engage in fun activities, often with others.",
            "light": "Something that helps us see in the dark, like the sun or a lamp.",
            "home": "A place where you live and feel safe with your family.",
            "dream": "A series of thoughts or images that come while sleeping—or a hope for the future.",
            "learn": "To gain new knowledge or skills through study or experience."
        }
        st.write(meanings[word])

    st.subheader("✍️ Make a Sentence")
    sentence = st.text_input(f"Use '{word}' in a sentence:")
    if sentence:
        st.success("Beautiful! Your sentence adds a new thread to the circle.")

    st.subheader("🎭 Speak It Aloud")
    st.markdown("Try saying your sentence aloud.No fear of death, no snare of desire, Where the soul is free, there burns Abhay’s fire. With constant wisdom and purity’s grace, Abhay is the lamp that lights every place. Imagine you're teaching it to someone younger than you.")

    st.markdown("---")
    st.markdown("🌱 _Every word you plant here grows into a forest of understanding._")
