logo = '''


  ________                           __________.__            _______               ___.                 
 /  _____/ __ __  ____   ______ _____\__    ___|  |__   ____  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  _/ __ \ /  ___//  ___/ |    |  |  |  \_/ __ \ /   |   \|  |  \/     \| __ \_/ __ \_  __ \\
\    \_\  |  |  \  ___/ \___ \ \___ \  |    |  |   Y  \  ___//    |    |  |  |  Y Y  | \_\ \  ___/|  | \/
 \______  |____/ \___  /____  /____  > |____|  |___|  /\___  \____|__  |____/|__|_|  |___  /\___  |__|   
        \/           \/     \/     \/               \/     \/        \/            \/    \/     \/       

'''
import random
print(logo)
target = random.randint(0,100)
print("\nI'm thinking of a number between 0 - 100 including both end points... Try to guess it!\n")

difficulty = input("Select difficulty, type easy or hard: ")

if difficulty == "easy":
    lives = 10
else:
    lives = 5

cont = True

def game(lives, cont):
    
    while cont:
        print(f"\nYou have {lives} lives remaining to guess the number\n")
        guess = int(input("make a guess: "))
        if guess > target:
            print("\nToo high!\n")
            lives -= 1
            if lives == 0:
                print("Zero lives remain... You loose!\n")
                print(f"The number you were trying to guess was {target}\n")
                cont = False
        elif guess < target:
            print("\nToo low!\n")
            lives -=1
            if lives == 0:
                print("Zero lives remain... You loose!")
                print(f"The number you were trying to guess was {target}\n")
                cont = False
        else:
            print(f"\nYour guess of {guess} was correct!! Well done!\n")
            cont = False

game(lives, cont)
    
