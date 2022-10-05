from random import randint

correctGuess = randint(0, 20)
guess = int(input("Input a number between 0 and 20: "))

if 0 < guess < 20:
    if guess == correctGuess:
        print("Your guess is correct!")
    elif guess < correctGuess:
        print("Number is smaller")
    elif guess > correctGuess:
        print("Number is larger")
else:
    print("Your guess is out of range!")