MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = {"money": 0,}

can_supply = True
cont = True


while cont:

    inp = input("\nWhat would you like? (espresso/latte/cappuccino): ")



    def resources1():

        global can_supply
        global cont

        for key, value in MENU.items():
            if key == inp:
                temp = value["ingredients"]



        if inp == "report":
            for x,y in resources.items():
                if x == "water" or x == "milk":
                    print(str(x) + ":" + " " + str(y) + "ml")
                else:
                    print(str(x) + ":" + " " + str(y) + "g")
            for x,y in money.items():
                    print(str(x) + ":" + " " + "$" + str(y))
        elif inp == "off":
            cont = False
        elif inp == "espresso" or inp == "latte" or inp == "cappuccino":

            ok = 0
            for key1, total in temp.items():
                for key2, remaining in resources.items():
                    if key1 == key2:
                        if remaining >= total:
                            ok += 1
                            if ok == 3:
                                can_supply = True
                        else:
                            temp_str_1 = "Sorry there is not enough" + " " + key1
                            print(temp_str_1)
                            can_supply = False
                            break

            if can_supply == True:

                for key, value in MENU.items():
                    if key == inp:
                        temp2 = value
                        cost = temp2["cost"]

                print(f"\nPlease insert coins, a {inp} costs ${cost}\n")

                num_quart = int(input("please insert number of quarters: "))
                num_dime = int(input("please insert number of dimes: "))
                num_nick = int(input("please insert number of nickels: "))
                num_pen = int(input("please insert number of pennies: "))

                input_total = 0.25 * num_quart + 0.1 * num_dime + 0.05 * num_nick + 0.01 * num_pen

                calc = cost - input_total

                if calc > 0:
                    print(f"\nSorry ${input_total} is not enough money. Money will be refunded.")
                    can_supply = False
                elif calc < 0:
                    calc = calc * -1
                    calc = "{:.2f}".format(calc)
                    print(f"\nYou have input too much money, ${calc} will be refunded.")
                    money["money"] += cost
                else:
                    print("\nThat is the correct input, thank you.")
                    money["money"] += cost

                for key1, total in temp.items():
                    for key2, remaining in resources.items():
                        if key1 == key2:
                            if remaining >= total:
                                resources[key1] = remaining - total
                print(f"\nHere is your {inp}.... Enjoy!")

        else:
            print("Invalid input")






    resources1()