"""
Number Guessing Game - Built with Streamlit

A simple game where players guess a number between 1-100.
The game provides hints and tracks the number of guesses.

NOTE: This code intentionally mixes UI logic with game logic 
and contains bugs for you to find and fix!
"""

import streamlit as st
from logic_utils import parse_guess, check_guess, start_game


def main():
    """Main application entry point."""
    
    st.title("🎮 Number Guessing Game")
    st.write("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    # Initialize session state
    if 'game' not in st.session_state:
        st.session_state.game = start_game()
        st.session_state.feedback_history = []
    
    game = st.session_state.game
    
    # Display game status
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Guesses Made", game['guesses_made'])
    with col2:
        st.metric("Guesses Remaining", game['max_guesses'] - game['guesses_made'])
    
    # Player input
    guess_input = st.text_input("Enter your guess:", key="guess_input")
    
    if st.button("Submit Guess"):
        # Parse the input
        guess = parse_guess(guess_input)
        
        if guess is None:
            st.error("Please enter a valid number between 1 and 100.")
        else:
            # BUG #2: This increment doesn't actually work because 
            # we check max guesses AFTER incrementing, but the game never truly stops
            game['guesses_made'] += 1
            
            # Get feedback from logic
            feedback = check_guess(guess, game['secret'])
            st.session_state.feedback_history.append((guess, feedback))
            
            # Display feedback
            if feedback == "Correct!":
                st.success(f"🎉 You got it! The number was {game['secret']}!")
                st.balloons()
                game['game_over'] = True
                
                # BUG #3: Score calculation is wrong!
                # It only counts guesses, not hints given. Should count hints as penalties.
                score = 100 - (game['guesses_made'] * 10)
                st.write(f"**Your Score:** {score}")
            else:
                st.info(f"Hint: {feedback}")
                
                # BUG #2: This check doesn't properly end the game
                # The condition is here but the game state doesn't fully stop
                if game['guesses_made'] >= game['max_guesses']:
                    st.error(f"Game Over! The secret number was {game['secret']}")
                    game['game_over'] = True
    
    # Display feedback history
    if st.session_state.feedback_history:
        st.write("### Your Guesses:")
        for guess, feedback in st.session_state.feedback_history:
            st.write(f"- Guessed: **{guess}** → {feedback}")
    
    # Reset button
    if st.button("Reset Game"):
        st.session_state.game = start_game()
        st.session_state.feedback_history = []
        st.rerun()


if __name__ == "__main__":
    main()
