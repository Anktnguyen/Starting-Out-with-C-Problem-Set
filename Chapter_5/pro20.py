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

def main():
    again = input("\n\nPress y to play: ")
    while again.lower() == "y":
        guess_num = int (input ("Enter the predicted random number: "))
        guess(guess_num)
        again = input("\n\nPress y to play again: ")
    else:
        print("Terminating program...")

def guess(guess_num):
    global count_guess
    number = random_num()
    #print(number)
    while guess_num != number:
        count_guess +=1
        if guess_num > number:
            print("\nToo High, try again.")
            guess_num = int(input("Enter the predicted random number: "))
        elif guess_num < number:
            print("\nToo Low, try again.")
            guess_num = int(input("Enter the predicted random number: "))
    else:
        print(f"Congratulation you guessed the number {number}!\n"
              f"It took {count_guess} guesses to reach the right answer.")


def random_num():
    number = random.randint(1, 100)
    return number

if __name__ == "__main__":
    main()