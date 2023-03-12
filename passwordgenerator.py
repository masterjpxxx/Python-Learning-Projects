#This python program generates random strong password based on user input.
#Step 1: Create a list of random characters where the password will be chosen
#Step 2: Ask for the number of passwords to be generated
#Step 3: Ask for the password length
#Step 4: Generate the password
#Step 5: Display the passwords generated

import random

passwordchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*(),.'

numpassword = int(input("How many passwords will be generated? "))
passwordlen = int(input("What is the desired password length? "))

for i in range(numpassword):
    password = ""
    for j in range(passwordlen):
        password += random.choice(passwordchars)
    print(password)