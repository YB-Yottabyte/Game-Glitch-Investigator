"""
Unit tests for game logic.

TODO: You will add tests here as you fix each bug.
Example structure:

def test_check_guess_too_high():
    # Arrange: set up test data
    guess = 60
    secret = 50
    
    # Act: call the function
    result = check_guess(guess, secret)
    
    # Assert: verify the result
    assert result == "Too High"
"""

import pytest
from logic_utils import parse_guess, check_guess, start_game


class TestParseGuess:
    """Test the parse_guess function."""
    
    def test_valid_guess(self):
        """Parse a valid guess string."""
        result = parse_guess("42")
        assert result == 42
    
    def test_guess_out_of_range_low(self):
        """Invalid guess below 1."""
        result = parse_guess("0")
        assert result is None
    
    def test_guess_out_of_range_high(self):
        """Invalid guess above 100."""
        result = parse_guess("101")
        assert result is None
    
    def test_invalid_string(self):
        """Non-numeric input."""
        result = parse_guess("abc")
        assert result is None


class TestStartGame:
    """Test game initialization."""
    
    def test_start_game_returns_dict(self):
        """start_game returns a dictionary with correct keys."""
        game = start_game()
        assert isinstance(game, dict)
        assert 'secret' in game
        assert 'max_guesses' in game
        assert 'guesses_made' in game
        assert 'game_over' in game
    
    def test_secret_in_range(self):
        """Secret number is between 1 and 100."""
        game = start_game()
        assert 1 <= game['secret'] <= 100
    
    def test_initial_state(self):
        """Game starts with correct initial state."""
        game = start_game()
        assert game['guesses_made'] == 0
        assert game['max_guesses'] == 10
        assert game['game_over'] is False


# TODO: Add tests for check_guess after you fix BUG #1
# Example:
# def test_check_guess_correct():
#     assert check_guess(50, 50) == "Correct!"
#
# def test_check_guess_too_high():
#     assert check_guess(60, 50) == "Too High"
#
# def test_check_guess_too_low():
#     assert check_guess(40, 50) == "Too Low"
