# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

def guessing_number():
    print("""Welcome to the Guess the Number game! \n
    Instructions: You will guess the number generated by the computer. \n
    If your guess is greater than the computer generated number, the program will display 'Greater than'. \n
    If your guess is less than the computer generated number, the program will display 'Less than'. \n""")

    computer_number = random.randint(0,100)

    ask_user_ready_or_not = input("Ready? Type y if yes and n if not. ").lower()

    if ask_user_ready_or_not == "y":
        while True:
            user_number = int(input("Your guess: "))
            if user_number > computer_number:
                print("Your guess is greater than the computer-generated number. Try again!")
            elif user_number == computer_number:
                print(f"You got it! \n The computer generated number is {computer_number}.")
            else:
                print("Your guess is less than the computer-generated number. Try again!")
    else:
        print("Please restart the game.")


guessing_number()