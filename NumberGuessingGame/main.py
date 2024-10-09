import random
import art
rightnumber = random.randint(1,100)

def display():
    """This function is to for display the game and explain it with the logo of the game and how to play it"""
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

def score(x):
    """This function is to compare between the values of each guessed number and the correct number ( more than, less than or the same )"""
    if x > rightnumber:
        print("Too high.\nGuess again.")
        return x
    elif x < rightnumber:
        print("Too low.\nGuess again.")
        return x
    elif x == rightnumber:
        print(f"You got it! The answer was {x}.")
        quit()

def game():
    """This function is organizing the game by using the display function at the beggening of the game then asking the user
    about the diffculty of the game if it's easy he will have 10 attempts, if it's hard he will have 5 attempts only then
    starting asking him about the gussed number then using the function score() to compare. """
    display()
    diffculty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    if diffculty == "easy":
        i = 10
        for x in range(i):
            print(f"You have {i} attempts remaining to guess the number.")
            guess = int(input("Make a guess:"))
            score(guess)
            i -= 1
    elif diffculty == "hard":
        i = 5
        for x in range(i):
            print(f"You have {i} attempts remaining to guess the number.")
            guess = int(input("Make a guess:"))
            score(guess)
            i -= 1

game() # calling the main function