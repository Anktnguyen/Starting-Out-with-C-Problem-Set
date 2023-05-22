"""
16. Odd/Even Counter
Write a program that generates 100 random numbers and keeps a count of how many of those random
numbers are even, and how many of them are odd.
"""
import random
total_even = 0
total_odd = 0

def even_odd():
    global total_even
    global total_odd
    for runs in range (100):
        number = random.randint(1, 100)
        #even number will result in no left over when modulo by 2
        if number % 2 == 0:
            #the number is converted to 1 for counting purposes
            total_even += 1
        #if the number modulo by 2 with left over then it's an odd number
        else:
            total_odd += 1
    print(total_even)
    print(total_odd)


even_odd()