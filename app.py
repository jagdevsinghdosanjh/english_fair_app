# app.py

import streamlit as st
from modules import english_circles, jumbled_words, story_telling
from parent_corner import guidance
from utils.helpers import display_badges

# Page configuration
st.set_page_config(page_title="English Fair App", layout="wide")

# Optional: Custom CSS styling
st.markdown("""
    <style>
    body {
      background-color: #fdf6e3;
      font-family: 'Segoe UI', sans-serif;
      color: #333;
    }

    .welcome-banner {
      background-color: #e0f7fa;
      padding: 20px;
      border-radius: 12px;
      text-align: center;
      box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
    }

    .welcome-banner h1 {
      color: #00796b;
      font-size: 2.5em;
      margin-bottom: 10px;
    }

    .welcome-banner p {
      font-size: 1.2em;
      color: #004d40;
    }
    .welcome-banner strong {
      font-size: 1.2em;
      color: #004d40;
    }
    </style>

    <div class="welcome-banner">
      <h1>🌟 Welcome to the English Fair</h1>
      <p>Where words bloom, stories breathe, and learning becomes celebration.</p>
      <strong>Gurpreet Kaur - English Mistress GHS Chananke Amritsar</strong>
    </div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎪 English Fair Navigation")
page = st.sidebar.radio("Choose an activity", [
    "Home",
    "English Circles",
    "Jumbled Words",
    "Story Telling",
    "Parent Corner"
])

# Page routing
if page == "Home":
    st.markdown("## 🧭 Explore the fair using the sidebar.")
    st.markdown("Each stall is a celebration of English learning—interactive, joyful, and poetic.")
    display_badges()

elif page == "English Circles":
    english_circles.render()

elif page == "Jumbled Words":
    jumbled_words.render()

elif page == "Story Telling":
    story_telling.render()

elif page == "Parent Corner":
    guidance.render()

# # app.py
# import streamlit as st
# from modules import english_circles, jumbled_words, story_telling, parent_corner

# st.set_page_config(page_title="English Fair App", layout="wide")

# st.sidebar.title("🎪 English Fair Navigation")
# page = st.sidebar.radio("Choose an activity", [
#     "Home",
#     "English Circles",
#     "Jumbled Words",
#     "Story Telling",
#     "Parent Corner"
# ])

# if page == "Home":
#     st.title("🌟 Welcome to the English Fair")
#     st.markdown("""
#         _Where words dance, stories bloom, and learning becomes celebration._
#         Explore interactive stalls designed to awaken curiosity and joy in English learning.
#     """)

# elif page == "English Circles":
#     english_circles.render()

# elif page == "Jumbled Words":
#     jumbled_words.render()

# elif page == "Story Telling":
#     story_telling.render()

# elif page == "Parent Corner":
#     parent_corner.render()
