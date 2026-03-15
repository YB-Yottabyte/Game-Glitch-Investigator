# 🎮 Game Glitch Investigator

A Python guessing game built with Streamlit that contains intentional bugs for you to discover, debug, and fix using AI tools like Copilot.

## Project Goal

Learn to debug AI-generated code responsibly by:
1. **Finding bugs** by playing the game and observing unexpected behavior
2. **Explaining bugs** using Copilot to understand the underlying logic flaws
3. **Fixing bugs** with AI assistance while maintaining code quality
4. **Testing fixes** with automated pytest cases
5. **Documenting the process** to show how you collaborated with AI

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/Game-Glitch-Investigator.git
cd Game-Glitch-Investigator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Game

```bash
streamlit run app.py
```

The game will open in your default browser at `http://localhost:8501`.

### Running Tests

```bash
pytest test/ -v
```

## Game Rules

- The computer picks a secret number between 1–100
- You have 10 guesses to find it
- After each guess, you get a hint: "Too High", "Too Low", or "Correct!"
- Your score is based on how few guesses you used

## Demo

<!-- TODO: Update this section with your experience -->

**How to play:**
1. Open the app with `streamlit run app.py`
2. Enter a number between 1 and 100 in the text box
3. Click "Submit Guess" to see the hint
4. Click "Reset Game" to play again

**What you'll notice (bugs are intentional!):**
- 🐛 Bug 1: [FILL IN AFTER PHASE 1]
- 🐛 Bug 2: [FILL IN AFTER PHASE 1]
- 🐛 Bug 3: [FILL IN AFTER PHASE 1]

## Document Your Experience

<!-- TODO: Fill in after Phase 3 -->

### What surprised you about debugging AI-generated code?

> Your answer here

### When did you trust the AI's suggestions? When did you doubt them?

> Your answer here

### What skill improved the most?

> Your answer here

## Project Structure

```
game-glitch-investigator/
├── README.md                 (this file)
├── reflection.md             (your debugging journal)
├── requirements.txt          (Python dependencies)
├── app.py                    (Streamlit UI + game loop)
├── logic_utils.py           (game logic with bugs)
└── test/
    └── test_game_logic.py   (pytest cases)
```

## Files Overview

| File | Purpose |
|------|---------|
| `app.py` | Streamlit interface and main game loop |
| `logic_utils.py` | Core game logic (parse, check, start functions) |
| `test/test_game_logic.py` | Unit tests for logic_utils.py |
| `reflection.md` | Your debugging notes and AI collaboration log |

## Debugging Workflow

1. **Phase 1: Glitch Hunt** (~45 mins)
   - Play the game and identify bugs
   - Document what you observe vs. what you expected
   - Ask Copilot to explain the buggy logic

2. **Phase 2: Investigate & Repair** (~60 mins)
   - Mark bugs with `# FIXME:` comments
   - Use Copilot Chat to fix each bug
   - Write pytest tests to verify fixes
   - Add `# FIX:` comments explaining your AI collaboration

3. **Phase 3: Reflection & Documentation** (~30 mins)
   - Complete this README
   - Write up your reflection in `reflection.md`
   - Commit and push all changes

## Resources

- **Streamlit Docs:** https://docs.streamlit.io/
- **Pytest Docs:** https://docs.pytest.org/
- **GitHub Copilot:** https://github.com/features/copilot
- **Python Style Guide (PEP 8):** https://pep8.org/

## License

This project is open source and available under the MIT License.

---

**Ready to debug?** Head over to `reflection.md` to document your findings!