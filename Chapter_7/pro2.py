"""
2. Lottery Number Generator
Design a program that generates a seven-digit lottery number. The program should generate
seven random numbers, each in the range of 0 through 9, and assign each number to a
list element. (Random numbers were discussed in Chapter 5.) Then write another loop that
displays the contents of the list.
"""
import random

def main():
    lottery_list = []
    #for look to create 7 number (can also use while loop to reach 7 numbers condition)
    for number in range(7):
        #random module using random integer (randint) setting restriction (start(0), end(9))
        number = random.randint(0,9)
        #adding number to list using append
        lottery_list.append(number)
        
    #printing everything out
    print(f'{lottery_list}')

if __name__ == "__main__":
    main()
