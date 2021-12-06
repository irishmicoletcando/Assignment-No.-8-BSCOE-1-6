# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You lose” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# If “n” the program will exit.

import random

def lottery_game():
    print("""Welcome to the Lottery Game!\n
            Instructions: The computer will generate 3 random numbers and the numbers that you will input must matched the computer generated numbers.\n
            The program will display "Winner!" if you input all 3 numbers correctly and "You lose!" if not.\n""")

