# Number Guessing Game

This is a simple number guessing game written in Python, where the player has to guess a random number between 1 and 100. The game features two difficulty levels: easy and hard.

## How the Game Works

1. The game begins by displaying a logo and explaining how to play.
2. The player chooses the difficulty level:
   - **Easy**: The player has 10 attempts to guess the correct number.
   - **Hard**: The player has only 5 attempts.
3. After each guess, the game will tell the player if the guess was too high, too low, or correct.
4. The game ends when the player guesses the correct number or runs out of attempts.

## Project Structure

The project contains the following files:

- `main.py`: This file contains the game logic.
- `art.py`: (Optional) If you use a separate module for the game's logo, include this file in the project.

## How to Run the Game

### Prerequisites

- Python 3.x installed on your system.
- The `art` module (if not installed, install it using the instructions below).

### Steps to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/NumberGuessingGame.git
   cd NumberGuessingGame
