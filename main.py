
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def remaining_resources(order_ingredients):
    """return whether there are remaining resources."""
    is_enough = True
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f"Sorry, there is not enough {items}")
            is_enough = False
    return is_enough


def process_coins():
    """return total calculated coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def make_coffee(drink_name,order_ingredients):
    """Deduct ingredients from current resources."""
    for items in order_ingredients:
        resources[items] -= order_ingredients[items]
    print("Here is your drink")


def check_transaction(money_received,drink_cost):
    """return true if payment is accepted, false if not accepted"""
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is your ${change} change")
        global profit
        profit += money_received
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


is_on = True


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money:${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if remaining_resources(drink["ingredients"]):
            payment = process_coins()
            check_transaction(payment, drink["cost"])
            make_coffee(choice,drink["ingredients"])