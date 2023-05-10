"""
6. Dice Rolling Function
In a program, write a function named roll that accepts an integer argument number_
of_throws. The function should generate and return a sorted list of number_of_throws
random numbers between 1 and 6. The program should prompt the user to enter a positive
integer that is sent to the function, and then print the returned list.
"""
import random

def main():
    #taking input on amount of rolls 
    number_of_throws = int(input("Enter the number of rolls for the dice: "))

    #set condition to accept only positive integer
    if number_of_throws > 0:        
        #calling the roll function
        roll(number_of_throws)
    else:
        print('Enter a positive integer.')


def roll(number_of_throws):
    #setting an empty list
    list_of_rolls = []
    #using for loop to populate the list
    for rolls in range(number_of_throws):
        #this variable is set up to generate random numbers from 1 to 6
        rolls = random.randint(1,6)
        list_of_rolls.append(rolls)
    print(list_of_rolls)


if __name__ == "__main__":
    main()
