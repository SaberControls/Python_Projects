cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import os
clear = lambda: os.system('cls')
con = True

def game():

    global con
    global cont
    global cont1
    while con:
        
        logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
            |  \/ K|                            _/ |                
            `------'                           |__/           
        """
                        
        import random

        print(logo)
        ply_list = []
        dlr_list = []

        def deal():

            ply_hld = random.choice(cards)
            ply_hld1 = random.choice(cards)
            dlr_hld = random.choice(cards)
            dlr_hld1 = random.choice(cards)

            ply_list.append(ply_hld)
            ply_list.append(ply_hld1)
            dlr_list.append(dlr_hld)
            dlr_list.append(dlr_hld1)

            print(f"Your cards are {ply_list}")
            print(f"The dealers first car is: {dlr_list[0]}")

        cont = True
        cont1 = True

        def player():
            global cont
            global ply_val
            global dlr_val
            while cont:

                inp1 = input("Do you want to hit or stick: ")
                inp1 = inp1.lower()

                if inp1 == "stick":
                    ply_val = sum(ply_list)
                    print(f"your final total is {ply_val}!")
                    cont = False
                    

                elif inp1 == "hit":
                    ply_list.append(random.choice(cards))
                    print(ply_list)
                    ply_val = sum(ply_list)

                    if 11 in ply_list and ply_val > 21:
                        ply_list.remove(11)
                        ply_list.append(1)
                        ply_val = sum(ply_list)

                    print(f"Your new total is {ply_val}")
                    if ply_val > 21:
                        print("You are bust!")
                        cont = False
                        return
                
                elif inp1 != "hit" or inp1 != "stick":
                    print("Invalid input donkey")

            global cont1
            while cont1:

                if sum(dlr_list) > 15:
                    dlr_val = sum(dlr_list)
                    print(f"The dealers final total is {dlr_val}!") 
                    cont1 = False

                if sum(dlr_list) < 15:
                    dlr_list.append(random.choice(cards))
                    print(dlr_list)
                    dlr_val = sum(dlr_list)
                    print(f"The dealers new total is {dlr_val}")
                    if dlr_val > 21:
                        print("Dealer is bust!")
                        cont1 = False


            if ply_val == dlr_val:
                print(f"You both have a value of {ply_val}, so its a draw!")
            elif ply_val > 21 or dlr_val > 21:
                return
            elif ply_val > dlr_val:
                print(f"You had {ply_val}, the dealer had {dlr_val}, you win!")
            else:
                print(f"You had {ply_val}, the dealer had {dlr_val}, you loose!")

        deal()
        player()

        if input("Do you want to restart game? type y for yes n for no: ") == "y":
            clear()
        else:
            con = False

game()