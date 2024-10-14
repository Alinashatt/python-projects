MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

def prompt():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()

def check_resources(choice):
    """Check if there are enough resources for the selected drink."""
    for item in MENU[choice]['ingredients']:
        if resources[item] < MENU[choice]['ingredients'][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Calculate the total amount of money inserted."""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

def make_coffee(choice):
    """Deduct the required ingredients from the resources."""
    for item in MENU[choice]['ingredients']:
        resources[item] -= MENU[choice]['ingredients'][item]
    print(f"Here is your {choice} ☕. Enjoy!")

def process_transaction(choice, inserted_money):
    """Process the transaction for the drink."""
    global money
    cost = MENU[choice]['cost']
    if inserted_money >= cost:
        change = round(inserted_money - cost, 2)
        money += cost
        print(f"Here's ${change} in change.")
        make_coffee(choice)
    else:
        print("Sorry, that's not enough money. Money refunded.")

def report():
    """Print the current resource status and money earned."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def action():
    choice = prompt()
    if choice == 'off':
        quit()
    elif choice == 'report':
        report()
    elif choice in MENU:
        if check_resources(choice):
            inserted_money = process_coins()
            process_transaction(choice, inserted_money)
    else:
        print("Invalid choice, please select again.")

def game():
    while True:
        action()

game()
