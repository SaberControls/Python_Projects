import os
import random

from gamedata import data
from art import logo, vs

os.system('cls')
cont = True



def game(cont):

    score = 0
    print(logo)

    rand1 = random.randint(0,49)
    rand2 = random.randint(0,49)
    temp1 = data[rand1]
    temp2 = data[rand2]
    val1 = temp1["follower_count"]
    val2 = temp2["follower_count"]


    while cont:      

        if score > 0:
            print(f"You were right!! Your current score is {score}\n")
            rand1 = rand2
            temp1 = data[rand2]
            val1 = val2
            rand2 = random.randint(0,49)
            temp2 = data[rand2]
            val2 = temp2["follower_count"]
        print(temp1["name"])
        print(temp1["description"])
        print(temp1["country"])
        print(vs)
        print(temp2["name"])
        print(temp2["description"])
        print(temp2["country"])

        usr = input("\nhigher or lower? Enter H or L: ")
        print("\n")
        usr.lower
        if usr == "h":
            if val2 >= val1:
                print(temp1["name"], "has a follower count of", val1)
                print(temp2["name"], "has a follower count of", val2)
                print("\nYou are correct!\n")
                score += 1
                os.system('cls')
            else:
                print(temp1["name"], "has a follower count of", val1)
                print(temp2["name"], "has a follower count of", val2)
                cont = False
                return score
        if usr == "l":
                if val2 <= val1:
                    print(temp1["name"], "has a follower count of", val1)
                    print(temp2["name"], "has a follower count of", val2)
                    print("\nYou are correct!\n")
                    score += 1
                    os.system('cls')
                else:
                    print(temp1["name"], "has a follower count of", val1)
                    print(temp2["name"], "has a follower count of", val2)
                    cont = False
                    return score


score = game(cont)

print(f"\nYou were wrong! Your final score is {score}\n")
