# help to build a short proyect for learn how to use loops

# This is a simple program that will print the numbers from 1 to 10 using a loop

# for i in range(1, 11):
#     print(i)

# how i can use loops in python buildning a game of guess the number

import random

# secret_number = random.randint(1, 10)
# guess = None

# while guess != secret_number:
#     guess = int(input("Guess the number: "))
#     if guess < secret_number:
#         print("Too low!")
#     elif guess > secret_number:
#         print("Too high!")
#     else:
#         print("You got it!")

# now let do another example using a for loop


# give a problem to solve easy mode
# 1. Modify the program so that the player only has 5 attempts to guess the number.
# 2. Add a feature that tells the player how many attempts they have left.
# how i can think in the second problem to solve
# 1. I need to create a variable to store the maximum number of attempts.
# 2. I need to create a variable to store the number of attempts left.
# 3. I need to create a variable to store the secret number.
# 4. I need to create a variable to store the guess.
# 5. I need to create a loop to allow the player to guess the number.
# 6. I need to create a loop to allow the player to guess the number.

# lets continue with the loops in python throught projects with while and games

# create a game of rock paper scissors with while loop and explame each step
# 1. Create a variable to store the player's choice.
# player_choice = None
# # 2. Create a variable to store the computer's choice.
# computer_choice = None
# # 3. Create a loop that allows the player to play the game multiple times.
# while True:
#     # 4. Ask the player to choose rock, paper, or scissors.
#     player_choice = input("Choose rock, paper, or scissors: ")
#     # 5. Generate a random choice for the computer.
#     computer_choice = random.choice(["rock", "paper", "scissors"])
#     # 6. Determine the winner of the game.
#     if player_choice == computer_choice:
#         print("It's a tie!")
#     elif player_choice == "rock":
#         if computer_choice == "paper":
#             print("Computer wins!")
#         else:
#             print("Player wins!")
#     elif player_choice == "paper":
#         if computer_choice == "scissors":
#             print("Computer wins!")
#         else:
#             print("Player wins!")
#     elif player_choice == "scissors":
#         if computer_choice == "rock":
#             print("Computer wins!")
#         else:
#             print("Player wins!")
#     else:
#         print("Invalid choice. Please choose rock, paper, or scissors.")
#     # 7. Ask the player if they want to play again.
#     play_again = input("Do you want to play again? (yes/no): ")
#     if play_again.lower() != "yes":
#         break
# 4. Create a loop that allows the player to play the game multiple times.


# now teach me functions through projects


# def add_numbers(num1, num2):
#     return num1 + num2


# def subtract_numbers(num1, num2):
#     return num1 - num2


# def multiply_numbers(num1, num2):
#     return num1 * num2


# def divide_numbers(num1, num2):
#     return num1 / num2


# print(divide_numbers(5, 3))

# teach me logic through projects

# steps to solve a problem`
# 1. Identify the problem.
# 2. Analyze the problem.
# 3. Write the code.`

# create a program that will determine if a number is even or odd
# 1. Create a variable to store the number.

# number = int(input("Enter a number: "))

# # 2. Determine if the number is even or odd.

# if number % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# # 3. Print the result.

# print("The number is even.") if number % 2 == 0 else print("The number is odd.")

# now teach me how to use conditional statements through projects

# steps to solve a problem
# 1. Identify the problem.
# 2. Analyze the problem.
# 3. Write the code.

# create a program that will determine if a number is positive, negative, or zero
# 1. Create a variable to store the number.

number = int(input("Enter a number: "))
# 2. Determine if the number is positive, negative, or zero.

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 3. Print the result.
