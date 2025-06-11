# guess game by python basic

import random as r

random_number = r.randint(1, 100)
chances = int(input("Enter your chances: "))
while chances > 0 :
    chances -= 1
    user_number = int(input("Enter your number: "))
    if (random_number == user_number):
        print("Yay! You guess iss right (BOSS)".center(50, "-"))
        break
    if (user_number < random_number):
        print("Your guess is lower".center(50, "-"))

    if (user_number > random_number):
        print("Your guess is higher".center(50, "-"))
else:
    print("Play again".center(50, "-"))
print("well played BOSS".center(50, "-"))