import random

print(" Welcome to Number Guessing Game!")
secret_num = random.randint(1, 100)
print(secret_num)
guess = 0
while True:
    guess_num = int(input("Guess a number between 1 and 100: "))
    guess += 1
    if guess_num == secret_num:
        print(f"🎉 Correct! You guessed it in {guess} attempts.")
        break
    elif guess_num > secret_num:
        print("Too high!")
    elif guess_num < secret_num:
        print("Too low!")