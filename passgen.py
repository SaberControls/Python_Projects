#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


total = nr_letters+nr_numbers+nr_symbols

password = []

for y in range(0,nr_letters):
    rand1 = random.randint(0,25)
    password += letters[rand1]
for x in range(0,nr_symbols):
    rand2 = random.randint(0,7)
    password += symbols[rand2]
for z in range(0,nr_numbers):
    rand3 = random.randint(0,9)
    password += numbers[rand3]

pass1 = random.sample(password, total)
pass2 = ''

for p in pass1:
    pass2 += p

print(pass2)
