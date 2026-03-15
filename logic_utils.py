"""
Game logic module for the Number Guessing Game.

This module contains the core game logic functions:
- parse_guess: Converts user input to an integer
- check_guess: Compares guess to secret and returns feedback
- start_game: Initializes a new game session
"""


def parse_guess(guess_str):
    """
    Parse a string input into an integer guess.
    
    Args:
        guess_str (str): The user's input as a string
        
    Returns:
        int: The parsed integer, or None if invalid
        
    Raises:
        None - Returns None gracefully on error
    """
    try:
        guess = int(guess_str.strip())
        if guess < 1 or guess > 100:
            return None
        return guess
    except ValueError:
        return None


def check_guess(guess, secret):
    """
    Check the user's guess against the secret number.
    
    Args:
        guess (int): The user's guess
        secret (int): The secret number to guess
        
    Returns:
        str: Feedback message ("Correct!", "Too High", or "Too Low")
    """
    if guess == secret:
        return "Correct!"
    elif guess > secret:
        # FIX #1: Corrected reversed logic - now correctly returns "Too High" when guess is greater
        return "Too High"
    else:
        # FIX #1: Corrected reversed logic - now correctly returns "Too Low" when guess is less
        return "Too Low"


def start_game():
    """
    Initialize a new game session.
    
    Returns:
        dict: A dictionary with keys:
            - 'secret': The random number (1-100)
            - 'max_guesses': Maximum number of guesses allowed
            - 'guesses_made': Counter for guesses so far
            - 'game_over': Boolean flag
            
    NOTE: BUG #2 - The max_guesses logic doesn't work properly
    The counter will be set but never incremented correctly in app.py
    """
    import random
    return {
        'secret': random.randint(1, 100),
        'max_guesses': 10,
        'guesses_made': 0,
        'game_over': False
    }
