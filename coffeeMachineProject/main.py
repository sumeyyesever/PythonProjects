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

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01
money = 0


def check_resources(user_coffee):
    user_cof_ing = MENU[user_coffee]["ingredients"]
    if resources["water"] < user_cof_ing["water"]:
        print("Sorry there is not enough water")
    elif resources["coffee"] < user_cof_ing["coffee"]:
        print("Sorry there is not enough coffee")
    elif not user_coffee == "espresso" and resources["milk"] < user_cof_ing["milk"]:
        print("Sorry there is not enough milk")
    else:
        return True


def calculate_money(user_coffee):
    print("Please insert coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    user_money = quarters * QUARTER + dimes * DIME + nickles * NICKLE + pennies * PENNY
    coffee_money = MENU[user_coffee]["cost"]
    change = user_money - coffee_money
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return -1
    else:
        return change


def update_resources(user_coffee):
    user_cof_ing = MENU[user_coffee]["ingredients"]
    remaining_water = resources["water"] - user_cof_ing["water"]
    remaining_coffee = resources["coffee"] - user_cof_ing["coffee"]
    if not user_coffee == "espresso":
        remaining_milk = resources["milk"] - user_cof_ing["milk"]
    else:
        remaining_milk = resources["milk"] - 0
    return remaining_water, remaining_milk, remaining_coffee


flag = True

while flag:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money}")
    elif not user_input == "off":
        resources_result = check_resources(user_input)
        if resources_result:
            money_result = calculate_money(user_input)
            if money_result != -1:
                updated_resources = update_resources(user_input)
                resources = {
                    "water": updated_resources[0],
                    "milk": updated_resources[1],
                    "coffee": updated_resources[2]
                }
                money += MENU[user_input]["cost"]
                rounded_money = round(money_result, 2)
                print(f"Here is ${rounded_money} in change")
                print(f"Here is your {user_input} ☕ Enjoy!")
    else:
        flag = False
