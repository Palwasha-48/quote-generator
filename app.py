import streamlit as st
import random
from quote import quote 

st.title("💬 Random Quote Generator 💡")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #252422;
        color: #CCC5B9;
    }
    header[data-testid="stHeader"] {
            background-color: #201F1D; 
        }

     @media (prefers-color-scheme: light) {
            /* background color */
            .stApp {
                background-color: #F3BDB9;
                color: #57140F;
            }

            /* Top navigation bar color */
            header[data-testid="stHeader"] {
                background-color: #F0ADA8; 
            }
    </style>
    """,
    unsafe_allow_html=True
)

categories = ["select any category",
              "ambition", "appreciation", "authenticity", "balance", "belief", "bravery", "change", "charity",
              "commitment", "compassion", "confidence", "consistency", "courage", "creativity", "curiosity", "dedication",
              "determination", "discipline", "dreams", "education", "empathy", "encouragement", "enthusiasm", "ethics",
              "faith", "failure", "forgiveness", "freedom", "friendship", "funny", "generosity", "goals", "gratitude",
              "growth", "happiness", "hard work", "healing", "health", "hope", "honesty", "humility", "humor", "imagination",
              "independence", "inspiration", "integrity", "joy", "justice", "kindness", "knowledge", "leadership",
              "learning", "life", "love", "loyalty", "mindfulness", "motivation", "opportunity", "optimism",
              "overcoming challenges", "passion", "patience", "peace", "perseverance", "personal growth", "positive",
              "power", "productivity", "purpose", "relationships", "resilience", "sacrifice", "self-acceptance",
              "self-actualization", "self-awareness", "self-belief", "self-care", "self-compassion", "self-confidence",
              "self-control", "self-discipline", "self-discovery", "self-empowerment", "self-enrichment", "self-esteem",
              "self-expression", "self-forgiveness", "self-gratitude", "self-growth", "self-help", "self-identity",
              "self-image", "self-improvement", "self-inspiration", "self-love", "self-motivation", "self-reflection",
              "self-respect", "self-sacrifice", "self-transformation", "service", "spirituality", "strength", "success",
              "teamwork", "time", "trust", "truth", "understanding", "unity", "values", "vision", "wisdom", "work"]


selected_category = st.selectbox("🎯 Choose a category:", categories)
if st.button("📝 Generate Quote"):
    quotes = quote(selected_category)
    if quotes:
        random_quote = random.choice(quotes)  
        st.markdown(f"> *{random_quote['quote']}*")  
        st.write(f"— **{random_quote['author']}**")  
    else:
        st.write("No quotes found. Try again!") 

st.markdown("<hr>", unsafe_allow_html=True)
st.write("**Made with ❤️ by Palwasha**")