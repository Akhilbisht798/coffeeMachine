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


def money_total(quaters,dimes,nickel,pennis):
    return quaters*0.25 + dimes*0.10 +nickel*0.05 +pennis*0.01

                


is_on = True
while is_on:
    choice = input("What do you want? (espresso,latte, cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"profit: {profit}")
    elif choice == "espresso":
        if resources["water"] >= MENU['espresso']['ingredients']['water']:
            if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                print("Please insert coin.")
                quaters = int(input("How many quaters: "))
                dimes =   int(input("How many dimes: "))
                nickel =  int(input("how many nickel: "))
                pennis =  int(input("How many pennis: "))
                money_paid = money_total(quaters,dimes,nickel,pennis)
                if money_paid >= MENU['espresso']['cost']:
                    remaining = money_total(quaters,dimes,nickel,pennis) - MENU["espresso"]["cost"]
                    print(f"Your change is {remaining}.")
                    print("enjoy your coffee")
                    resources['water'] -= MENU["espresso"]["ingredients"]["water"]
                    resources['coffee'] -= MENU["espresso"]["ingredients"]['coffee']
                    profit += MENU["espresso"]['cost']
                else:
                    print("Not enough money")
            else:
                print("not enough resources")
        else:
            print("not enought resources")
    elif choice == "latte":
        if resources["water"] >= MENU['latte']['ingredients']['water'] and resources["milk"] >= MENU['latte']['ingredients']["milk"]:
            if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                print("Please insert coin.")
                quaters = int(input("How many quaters: "))
                dimes =   int(input("How many dimes: "))
                nickel =  int(input("how many nickel: "))
                pennis =  int(input("How many pennis: "))
                money_paid = money_total(quaters,dimes,nickel,pennis)
                if money_paid >= MENU['latte']['cost']:
                    remaining = money_total(quaters,dimes,nickel,pennis) - MENU["latte"]["cost"]
                    print(f"Your change is {remaining}.")
                    print("enjoy your coffee")
                    resources['water'] -= MENU["latte"]["ingredients"]["water"]
                    resources['coffee'] -= MENU["latte"]["ingredients"]['coffee']
                    resources['milk'] -= MENU["latte"]["ingredients"]['milk']
                    profit += MENU["latte"]['cost']
                else:
                    print("Not enough money. Here is your change.")
            else:
                print("not enough resources")
        else:
            print("not enought resources")
    elif choice == "cappuccino":
        if resources["water"] >= MENU['cappuccino']['ingredients']['water'] and resources["milk"] >= MENU['cappuccino']['ingredients']["milk"]:
            if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                print("Please insert coin.")
                quaters = int(input("How many quaters: "))
                dimes =   int(input("How many dimes: "))
                nickel =  int(input("how many nickel: "))
                pennis =  int(input("How many pennis: "))
                money_paid = money_total(quaters,dimes,nickel,pennis)
                if money_paid >= MENU['cappuccino']['cost']:
                    remaining = money_total(quaters,dimes,nickel,pennis) - MENU["cappuccino"]["cost"]
                    print(f"Your change is {remaining}.")
                    print("enjoy your coffee")
                    resources['water'] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources['coffee'] -= MENU["cappuccino"]["ingredients"]['coffee']
                    resources['milk'] -= MENU["cappuccino"]["ingredients"]['milk']
                    profit += MENU["cappuccino"]["cost"]
                else:
                    print("Not enough money. Here is your change.")
            else:
                print("not enough resources")
        else:
            print("not enought resources")
    






        
