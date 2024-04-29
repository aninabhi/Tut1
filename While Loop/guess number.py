import random
n = random.randint(1 ,10)
guess = 0

while guess != n:
    guess = int(input("guess your number "))

    if guess > n:
        print("number greater, attempt again")
    elif guess < n:
        print("number is lesser, attempt again ")
    else:
        print("Succefully attempt")


