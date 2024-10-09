import game_data
import random
import art
a = random.choice(game_data.data)
b = random.choice(game_data.data)

def firstview():
    """This function is to print the first display of the game by showing the A and B info"""
    print(art.logo)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

def highercheck(A,B):
    """This function is checking who is has more followers and returns the more"""
    if A > B:
        return 'a'
    elif A > B:
        return 'b'

def deffaultview(cscore):
    """This function is doing the same thing that firstview() do and print the score of the playre"""
    print(art.logo)
    print(f"You're right! Current score: {cscore}")
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")

def loseview(cscore):
    """This function is printing a display of lose"""
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {cscore}")

def game():
    """The main function that organizing the game and checks if the player wins or lose"""
    global a,b
    firstview()
    gameover = False
    AB = input("Who has more followers? Type 'A' or 'B': ").lower()
    score = 0
    while not gameover:
        if highercheck(a['follower_count'],b['follower_count']) == AB:
            score+=1
            b = a
            a = random.choice(game_data.data)
            deffaultview(score)
            AB = input("Who has more followers? Type 'A' or 'B': ").lower()
        else:
            loseview(score)
            gameover = True

game()  #calling the main function