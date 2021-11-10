import random
# set high score
high_score = 10


def start_game():

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