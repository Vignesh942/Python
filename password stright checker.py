import string
import re


def password(score):
    user_input = input("Enter your password: ")

    upper = bool(re.search(r'[A-Z]', user_input))
    lower = bool(re.search(r'[a-z]', user_input))
    number = bool(re.search(r'[0-9]', user_input))
    symbols = string.punctuation

    if upper:
        print("1:Caps found")
        score += 1
    else:
        print("1:Caps not found!")

    if lower:
        print("2:Small caps found")
        score += 1
    else:
        print("2:Small caps not found!")

    if number:
        print("3:Number found")
        score += 1
    else:
        print("3:Number not found!")

    if any(char in symbols for char in user_input):
        print("4:Symbol found")
        score += 1
    else:
        print("4:Symbol not found!")

    char_count = set()
    for char in user_input:
        if char in char_count:
            print("5:Duplicate charters found!")
            break
        char_count.add(char)
    else:
        print("5:Duplicate not found")
        score += 1

    if len(user_input) < 8:
        print("6:Length is below 8 characters!")
    else:
        print("6:Length good")
        score += 1

    print("Your score is {}/6".format(score))

    if score <= 2:
        print("Your password is weak")
    elif 3 <= score <= 4:
        print("Your password is average")
    elif score == 5:
        print("Your password is strong")
    elif score == 6:
        print("Your password is super strong")


password(score=0)
