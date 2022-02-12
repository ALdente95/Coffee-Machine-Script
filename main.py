
# Requirement:
# TODO 1) Print report
# TODO 2) Check resources sufficient?
# TODO 3) Process coins
# TODO 4) Check transaction successful
# TODO 5) Make Coffee
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

depleted = False


def calculate_resources(user_input):
    if user_choice == "espresso":
        resources["water"] = 50
        resources["coffee"] = 18
        resources["Money"] = 1.5
        return resources
    elif user_choice == "latte":
        resources["water"] = 200
        resources["milk"] = 150
        resources["coffee"] = 24
        resources["Money"] = 2.5
        return resources
    elif user_choice == "cappuccino":
        resources["water"] = 250
        resources["milk"] = 100
        resources["coffee"] = 24
        resources["Money"] = 3.0
        return resources


def compare_resources(user_input,current_resources):
    if MENU[f"{user_input}"]["ingredients"]["water"] > current_resources["water"]:
        print("Sorry there is not enough water.")
    elif MENU[f"{user_input}"]["ingredients"]["milk"] > current_resources["milk"]:
        print("Sorry there is not enough milk.")
    elif MENU[f"{user_input}"]["ingredients"]["coffee"] > current_resources["coffee"]:
        print("Sorry there is not enough coffee.")


def calculate_coins(no_quarters, no_dimes, no_nickles, no_pennies,user_drink):
    user_coins = no_quarters*0.25 + no_dimes*0.1 + no_nickles*0.05 + no_pennies*0.01
    if user_coins < MENU[f"{user_drink}"]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif user_coins > MENU[f"{user_drink}"]["cost"]:
        print(f'Here is ${user_coins - MENU[f"{user_drink}"]["cost"]:.2f} dollars in change.')
    else:
        resources["Money"] = user_coins


while not depleted:

    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice == "off":
        depleted = True
    elif user_choice == "report":
        print(resources)
    print(resources)
    compare_resources(user_choice,resources)

    print("Please insert coins.")
    quarter = float(input("How many quarters?: "))
    dime = float(input("How many dimes?: "))
    nickle = float(input("How many nickles?: "))
    penny = float(input("How many pennies?: "))
    calculate_coins(quarter, dime, nickle, penny, user_choice)
    if calculate_coins(quarter, dime, nickle, penny, user_choice) == 0:
        depleted = True
    else:
        print(calculate_resources(user_choice))
        print(f"Here is your {user_choice}. Enjoy!")