from turtle import Turtle, Screen
import random

# Setup the screen
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? ").lower()

# Define turtle colors and starting position
colors = ["red", "blue", "purple", "green", "yellow"]
turtles = []
y_position = -100

# Create and position turtles
for color in colors:
    turtle_obj = Turtle(shape="turtle")
    turtle_obj.color(color)
    turtle_obj.penup()
    turtle_obj.goto(x=-240, y=y_position)
    turtles.append(turtle_obj)
    y_position += 40  # Move next turtle down

# Start race if the user placed a bet
race_on = bool(user_input)

while race_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))  # Move a random distance

        # Check if a turtle reaches the finish line
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            
            if winning_color == user_input:
                print("You Win!")
            else:
                print(f"You Lose! {winning_color} won the race.")

            race_on = False  # Stop the race
            break

screen.exitonclick()  # Keep window open until clicked
