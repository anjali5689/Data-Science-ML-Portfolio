import streamlit as st
import random

# Load word list from file
def load_words():
    with open("words_list", "r") as file:
        return file.read().splitlines()

# Initialize game state
def initialize_game():
    st.session_state.word = random.choice(load_words()).lower()
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False
    st.session_state.message = ""

# Display word with guessed letters
def get_display_word():
    return ' '.join([letter if letter in st.session_state.guessed_letters else '_' for letter in st.session_state.word])

# Check if the user won
def has_won():
    return all(letter in st.session_state.guessed_letters for letter in st.session_state.word)

# --- App Start ---
st.title("🎯 Hangman Game (Streamlit Edition)")

# Initialize game only once
if "word" not in st.session_state:
    initialize_game()

# Display current word
st.subheader("Word:")
st.write(f"**{get_display_word()}**")

# Show guessed letters and lives
st.write(f"Guessed letters: `{', '.join(st.session_state.guessed_letters)}`")
st.write(f"Lives remaining: **{st.session_state.lives}**")

# Input for guessing a letter
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter", max_chars=1).lower()

    if st.button("Guess"):
        if not guess.isalpha() or len(guess) != 1:
            st.warning("Please enter a single alphabet letter.")
        elif guess in st.session_state.guessed_letters:
            st.warning("You already guessed that letter.")
        else:
            st.session_state.guessed_letters.append(guess)

            if guess in st.session_state.word:
                st.success(f"Correct! '{guess}' is in the word.")
                if has_won():
                    st.success(f"🎉 You won! The word was **{st.session_state.word}**.")
                    st.session_state.game_over = True
            else:
                st.session_state.lives -= 1
                st.error(f"Wrong guess! '{guess}' is not in the word.")
                if st.session_state.lives == 0:
                    st.error(f"😞 Game Over! The word was **{st.session_state.word}**.")
                    st.session_state.game_over = True

# Restart game
if st.button("🔁 Restart Game"):
    initialize_game()

# to run--->streamlit run prgm_name.py in terminal with same location