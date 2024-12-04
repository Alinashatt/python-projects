# QuizGame (My First OOP Project)

QuizGame is a Python-based quiz application that uses a set of questions and answers to provide an engaging and interactive quiz experience. 

## Features

- Automatically fetches questions and answers from `data.py`.
- Tracks your score as you progress through the quiz.
- Provides immediate feedback on correct or incorrect answers.

## How to Use

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/QuizGame.git
    cd QuizGame
    ```

2. Install the required dependencies:
   - This project doesn't use external libraries, so a basic Python installation (3.7 or above) is sufficient.

3. Run the `main.py` file to start the quiz:
    ```bash
    python main.py
    ```

## Project Structure

- **`main.py`**: Main script to execute the QuizGame.
- **`data.py`**: Contains the question data in JSON format.
- **`question_model.py`**: Defines the `Question` class, representing a quiz question and its answer.
- **`quiz_brain.py`**: Handles the quiz logic, including displaying questions and tracking the score.

## Example Output

