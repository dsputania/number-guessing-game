#Number guessing game
import random
secret_number = random.randint(1,20)
print("I have a number in my mind.")
#Asking the user for a guess.

for guess_taken in range(1,8):
    guess = int(input("Take a guess: "))

    if guess == secret_number:
        print(f"Good job!.You guessed the number correctly in {guess_taken} attempts")
        break
    elif guess > secret_number:
        print("Your guess is too high.")
    elif guess < secret_number:
        print("Your guess is too low.")

    if guess_taken > 6:
        print("Better luck next time.")
        print(f"The number I was thinking of was {secret_number}.")











