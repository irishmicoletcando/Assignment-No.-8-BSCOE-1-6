# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You lose” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# If “n” the program will exit.

import random
import sys

def lottery_game():
    print("""Welcome to the Lottery Game!\n
            Instructions: The computer will generate 3 random numbers and the numbers that you will input must matched the computer generated numbers.\n
            The program will display "Winner!" if you input all 3 numbers correctly and "You lose!" if not.\n""")

    # computer numbers
    computer_number_list = []
    # first digit
    computer_digit1 = random.randint(0,9)
    computer_number_list.append(computer_digit1)
    # second digit
    computer_digit2 = random.randint(0,9)
    computer_number_list.append(computer_digit2)
    # third digit
    computer_digit3 = random.randint(0,9)
    computer_number_list.append(computer_digit3)

    # user numbers
    user_number_list = []
    try:
        user_digit1 = int(input("Enter your first digit: "))
        if 0 <= user_digit1 <= 9:
            user_number_list.append(user_digit1)
        else:
            print("Enter a number from 0-9 only.")
    except ValueError:
        print("Enter a number only.")

    try:
        user_digit2 = int(input("Enter your second digit: "))
        if 0 <= user_digit2 <= 9:
            user_number_list.append(user_digit2) 
        else:
            print("Enter a number from 0-9 only.") 
    except ValueError:
        print("Enter a number only.")

    try:
        user_digit3 = int(input("Enter your third digit: "))
        if 0 <= user_digit3 <= 9:
            user_number_list.append(user_digit3) 
        else:
            print("Enter a number from 0-9 only.")
    except ValueError:
        print("Enter a number only.")

    print(f"The numbers you inputted are: {user_number_list}")

    # Game Proper
    if sorted(user_number_list) == sorted(computer_number_list):
        print(f"Winner!\nRandom Computer Numbers: {computer_number_list}")
    else:
        print(f"You lose!\nRandom Computer Numbers: {computer_number_list}")

def try_again():
    try_again = input("Try again? Type y if yes and n if no. ").lower()
    if try_again == "y":
        lottery_game()
    else:
        sys.exit()


lottery_game()
try_again()