
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


fire = '''⠀⠀⠀⠀

      ⢱⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣧⠀⠀⠀
⠀⠀⠀⠀⡀⢠⣿⡟⣿⣿⣿⡇⠀⠀
⠀⠀⠀⠀⣳⣼⣿⡏⢸⣿⣿⣿⢀⠀
⠀⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼⡆
⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿⣿
⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿⡿
⢳⣿⣿⣿⠀⠀⠀⠀⠀⠀⢹⣿⡿⡁
⠀⠹⣿⣿⡄⠀⠀⠀⠀⠀⢠⣿⡞⠁
⠀⠀⠈⠛⢿⣄⠀⠀⠀⣠⠞⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀
'''


hmm = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)___
---.__(________)
'''
#Write your code below this line 👇
comp = int(random.randint(1,3))

ply = input("What do you choose? pick 0 for rock, 1 for paper or 2 for scissors: ")

if comp == 1:
    print(rock)
elif comp == 2:
    print(paper)
elif comp == 3:
    print(scissors)
else:
    print('invalid')

    


print(f"You picked {ply}")

ply = int(ply)

if ply == 0:
    print(rock)
elif ply == 1:
    print(paper)
elif ply == 2:
    print(scissors)
elif ply == 666:
    print(fire)
elif ply == 69:
    print(hmm)
else:
    print('invalid')



if comp - 1 == ply:
    print("you drew")
elif comp == 1 and ply == 1:
    print ("you win")
elif comp == 1 and ply == 2:
    print ("you lose")
elif comp == 2 and ply == 0:
    print ("you lose")
elif comp == 2 and ply == 2:
    print ("you win")
elif comp == 3 and ply == 0:
    print ("you win")
elif comp == 3 and ply == 1:
    print ("you lose")
elif ply == 666:
    print ("fire burns ALL... You WIN!")
elif ply == 69:
    print ("You just...... WIN!")