#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to Gingie's Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

for pw_policy in [nr_letters, nr_symbols, nr_numbers]:

    if nr_letters + nr_symbols + nr_numbers < 10:
        print("Password does not meet the length requirement. Password must have at least 10 total characters.")
        input('Press ENTER to exit.')
        exit()

    elif nr_symbols < 1:
        print("Password must include at least one special character.")
        input('Press ENTER to exit.')
        exit()

    elif nr_numbers < 1:
        print("Password must include at least one number character.")
        input('Press ENTER to exit.')
        exit()

    else:
        continue

#Create 3 for loops to randomize process of choosing letters, numbers, symbols and put them in a list
password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for sym in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for num in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

#Shuffle password characters
random.shuffle(password_list)

#Concatenate shuffled characters back into a password string
password = ""
for char in password_list:
    password += char

#Output final password
print(f"Your password is {password}")
input('Press ENTER to exit')

