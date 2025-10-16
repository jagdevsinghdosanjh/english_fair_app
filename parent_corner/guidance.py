# parent_corner/guidance.py

import streamlit as st

def render():
    st.header("👨‍👩‍👧 Parent Corner")
    st.markdown("""
    _Welcome, dear parents. You are the co-authors of your child’s learning journey._

    This space offers:
    - 🧭 Tips to support English learning at home
    - 💬 Conversation starters to build vocabulary
    - 📜 Reflections to celebrate progress
    """)

    st.subheader("💡 Home Tips")
    st.markdown("""
    - Read aloud together—books, newspapers, even signs!
    - Ask your child to describe their day in English.
    - Celebrate small wins: new words learned, stories told.

    _Learning is not just in the classroom—it’s in every moment shared._
    """)

    st.subheader("🗣️ Conversation Starters")
    starters = [
        "What new word did you learn today?",
        "Can you tell me a story about your favorite object?",
        "Let’s play a game: describe something without naming it!"
    ]
    for s in starters:
        st.markdown(f"- {s}")

    st.subheader("📬 Share Your Reflections")
    feedback = st.text_area("What did you enjoy about today’s fair?")
    if feedback:
        st.success("Thank you for sharing! Your voice helps us grow together.")

    st.markdown("---")
    st.markdown("🌼 _Together, we plant seeds of confidence and curiosity._")
