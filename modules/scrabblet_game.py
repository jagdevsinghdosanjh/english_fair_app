# 🎲 Scrabblet Game in Sidebar
st.sidebar.markdown("---")
st.sidebar.subheader("🔤 Scrabblet Challenge")

# Initialize session state
if "scrabble_word" not in st.session_state:
    selected_word = random.choice(word_pool)
    st.session_state.scrabble_word = selected_word
    st.session_state.scrambled = ''.join(random.sample(selected_word, len(selected_word)))
    st.session_state.score = 0
    st.session_state.last_correct = False

# Display scrambled word
st.sidebar.markdown(f"**Unscramble:** `{st.session_state.scrambled.upper()}`")
user_guess = st.sidebar.text_input("Your guess:")

# Check guess
if user_guess.lower() == st.session_state.scrabble_word and not st.session_state.last_correct:
    st.sidebar.success("✅ Correct! Well done.")
    st.session_state.score += 1
    st.session_state.last_correct = True  # Prevent multiple increments
elif user_guess and user_guess.lower() != st.session_state.scrabble_word:
    st.sidebar.error("❌ Try again!")
    st.session_state.last_correct = False

# Show score
st.sidebar.markdown(f"🏅 Your score: **{st.session_state.score}**")

# Button to play next word
if st.sidebar.button("🔄 Next Word"):
    new_word = random.choice(word_pool)
    st.session_state.scrabble_word = new_word
    st.session_state.scrambled = ''.join(random.sample(new_word, len(new_word)))
    st.session_state.last_correct = False

# import streamlit as st
# import random

# def show_scrabblet_sidebar():
#     st.title("🎲 Scrabblet Challenge")
#     word_pool = ["merge", "realm", "essence", "story", "lamp", "soul", "truth", "fair", "badge", "poetic"]
#     selected_word = random.choice(word_pool)
#     scrambled = ''.join(random.sample(selected_word, len(selected_word)))

#     st.subheader("🔤 Unscramble this word:")
#     st.markdown(f"**{scrambled.upper()}**")

#     user_guess = st.text_input("Your guess:")
#     if user_guess.lower() == selected_word:
#         st.success("✅ Correct! Well done.")
#     elif user_guess:
#         st.error("❌ Try again!")

#     if "score" not in st.session_state:
#         st.session_state.score = 0
#     if user_guess.lower() == selected_word:
#         st.session_state.score += 1

#     st.markdown(f"🏅 Your score: **{st.session_state.score}**")
