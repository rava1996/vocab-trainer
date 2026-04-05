import streamlit as st
import pandas as pd
import os

st.title("Add New Words")

# Path to CSV
BASE_DIR = os.path.dirname(__file__)
csv_path = os.path.join(BASE_DIR, "data", "words.csv")

# Load existing words
words_df = pd.read_csv(csv_path)

st.subheader("Add a new word")

# Input fields
english_word = st.text_input("English word").strip()
italian_word = st.text_input("Italian word").strip()

# Add button
if st.button("Add word"):

    if english_word == "" or italian_word == "":
        st.warning("Both fields are required!")
    else:
        # Generate new ID
        new_id = words_df["id"].max() + 1

        # Append to dataframe
        new_row = pd.DataFrame([{
            "id": new_id,
            "english": english_word,
            "italian": italian_word
        }])

        words_df = pd.concat([words_df, new_row], ignore_index=True)

        # Save back to CSV
        words_df.to_csv(csv_path, index=False)

        st.success(f"Added '{english_word}' → '{italian_word}' to the word list!")

st.subheader("Current words in the CSV")
st.dataframe(words_df)
