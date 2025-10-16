# modules/jumbled_words.py
import streamlit as st
import random

def render():
    st.header("🔤 Jumbled Words Challenge")
    words = ["education", "language", "dictionary", "creative", "story"]
    selected = random.choice(words)
    jumbled = ''.join(random.sample(selected, len(selected)))

    st.write(f"Unscramble this word: **{jumbled}**")
    answer = st.text_input("Your guess:")
    
    if answer.lower() == selected:
        st.success("Correct! 🎉")
    elif answer:
        st.error("Try again!")
