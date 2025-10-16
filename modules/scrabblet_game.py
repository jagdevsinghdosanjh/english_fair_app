import streamlit as st
import random

def show_scrabblet_sidebar():
    st.title("🎲 Scrabblet Challenge")
    word_pool = ["merge", "realm", "essence", "story", "lamp", "soul", "truth", "fair", "badge", "poetic"]
    selected_word = random.choice(word_pool)
    scrambled = ''.join(random.sample(selected_word, len(selected_word)))

    st.subheader("🔤 Unscramble this word:")
    st.markdown(f"**{scrambled.upper()}**")

    user_guess = st.text_input("Your guess:")
    if user_guess.lower() == selected_word:
        st.success("✅ Correct! Well done.")
    elif user_guess:
        st.error("❌ Try again!")

    if "score" not in st.session_state:
        st.session_state.score = 0
    if user_guess.lower() == selected_word:
        st.session_state.score += 1

    st.markdown(f"🏅 Your score: **{st.session_state.score}**")
