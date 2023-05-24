'''
20. Random Number Guessing Game
Write a program that generates a random number in the range of 1 through 100,
and asks the user to guess what the number is. If the user's guess is higher than the random number,
the program should display "Too High, try again." If the user's guess is lower than the 
random number, the program should display "Too Low, try again."
If the user guesses the number, the application should congratulate the user and generate
a new random number so the game can start over.

Optional Enhancement: Enhance the game, so it keeps count of the number of guesses
that the user makes. When the user correctly guesses the random number,
the program should display the number of guesses.
'''

import random
count_guess = 1
again = "y"

def main():
    while again == "y":
        guess_num = int (input ("Enter the predicted random number: "))
        guess(guess_num)
        game = str(input("\n\nPress y to play again: "))
    else:
        print("Terminating program...")

def guess(guess_num):
    global count_guess
    number = random_num()
    print(number)
    while guess_num != number:
        guess_num = int(input("Enter the predicted random number: "))
        count_guess +=1
        if number < guess_num:
            print("Too High, try again.")
        else:
            print("Too Low, try again.")
    else:
        print("Congratulation you guessed the number!\n"
              f"It took {count_guess} guesses to reach the right answer.")


def random_num():
    number = random.randint(1, 100)
    return number

if __name__ == "__main__":
    main()