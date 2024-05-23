import string
import random
def password():

    letters = string.ascii_letters
    numbers = string.digits
    punc = string.punctuation

    user_letter = int(input("Enter how many letters you want in your password :"))
    user_total = random.sample(letters,user_letter)

    user_number = int(input("Enter how many numbers you want in your password :"))
    user_total1 = random.sample(numbers,user_number)

    user_punc = int(input("Enter how many punctuation you want in your password :"))
    user_total2 = random.sample(punc,user_punc)

    final_password = "".join(user_total+user_total2+user_total1)
    l = list(final_password)

    random.shuffle(l)
    for i in l:
        print(i,end="")
password()










