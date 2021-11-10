"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

# set high score
high_score = 10


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.




    # creating a function that asks for guesses while adding to trys
    def prompter():
        nonlocal trys
        trys += 1
        return input("Choose a number from 1 - 10\n")

    #  declairing game var
    trys = 0
    answer = random.randint(1, 10)
    
    #  declairing guess so fails first loop
    guess = 0

    #  while loop that ends when player answers correct number
    while guess != answer:
        # prompting palyer for a guess
        guess = prompter()

        # while loop making sure that the number entered is a valid number 
        while type(guess) != int:
            try:
                guess = int(guess)
            except ValueError:
                print("Please enter a valid number")
                guess = prompter()

        # letting user know if they guessed higher or lowwer than answer and checking if guess is within the range(1 - 10)
        if guess < 1 or guess > 10:
            print("number was not between 1 and 10")
            guess = prompter()
        elif guess < answer:
            print("Higher")
        elif guess > answer:
            print("Lowwer")

    # after loop let player know how many tries it took them to get the correct answer and if they got the high score   
    print(f"you got it in {trys} try(s)")
    global high_score
    if high_score > trys:
        high_score = trys
        print(f"Wow!!! you just made the high score")
    elif high_score < trys:
        print(f"so close the high score was {high_score}, you were just {trys - high_score} away from breaking the record")
    else:
        print("you tied the high score")

print("Glad you joined us. We're gonna be playing a guissing game")
start_game()

#  function that answers if player would like to play again
def replay():
    replay = input("would you like to play again?\n(yes/no) ")
    if replay == "yes":
        return True
    else:
        return False
again = replay()

#  loop enabling multiple games
while again:
    start_game()
    again = replay()
print("Hate to see you leave, Goodbye!")
