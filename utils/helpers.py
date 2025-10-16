# utils/helpers.py

import random
import streamlit as st

# 🌟 Badge Tracker
def mark_module_complete(module_name):
    if "completed_modules" not in st.session_state:
        st.session_state.completed_modules = set()
    st.session_state.completed_modules.add(module_name)

def get_completed_modules():
    return st.session_state.get("completed_modules", set())

def display_badges():
    completed = get_completed_modules()
    if completed:
        st.markdown("🏅 **Badges Earned:**")
        for module in completed:
            st.markdown(f"- ✅ {module}")
    else:
        st.markdown("🎯 No badges earned yet. Start exploring!")

# 🔤 Jumbled Word Generator
def jumble_word(word):
    return ''.join(random.sample(word, len(word)))

# 🧠 Session State Helper
def init_session_var(var_name, default_value):
    if var_name not in st.session_state:
        st.session_state[var_name] = default_value

# 🪞 Poetic Prompt Generator
def poetic_prompt():
    prompts = [
        "What does this word remind you of in your life?",
        "Imagine this word is a character—what would it say?",
        "How would you teach this word to a younger sibling?",
        "If this word were a color, what would it be?"
    ]
    return random.choice(prompts)
