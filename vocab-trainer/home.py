import streamlit as st
import pandas as pd
import os

st.title("Daily Vocabulary Challenge")

# Get the current directory of the script
BASE_DIR = os.path.dirname(__file__)

# Build the full path
csv_path = os.path.join(BASE_DIR, "data", "words.csv")

# Load the CSV
words = pd.read_csv(csv_path)

# Choose translation direction
direction = st.radio(
    "Choose translation direction:",
    ["English → Italian", "Italian → English"]
)

if direction == "English → Italian":
    prompt_col = "english"
    answer_col = "italian"
else:
    prompt_col = "italian"
    answer_col = "english"

# Select 10 words (only once per session)
if "daily_words" not in st.session_state:
    st.session_state.daily_words = words.sample(10).reset_index(drop=True)

daily_words = st.session_state.daily_words

st.write("Translate the following words:")

answers = {}

for i, row in daily_words.iterrows():

    answers[i] = st.text_input(
        f"{i+1}. {row[prompt_col]}",
        key=f"word_{i}"
    )

if st.button("Submit Answers"):

    score = 0
    results = []

    for i, row in daily_words.iterrows():

        correct_word = row[answer_col].strip().lower()
        user_answer = answers[i].strip().lower()

        correct = user_answer == correct_word

        if correct:
            score += 1

        results.append({
            "word": row[prompt_col],
            "your_answer": user_answer,
            "correct_answer": correct_word,
            "correct": correct
        })

    st.subheader(f"Score: {score}/10")

    results_df = pd.DataFrame(results)
    st.dataframe(results_df)
