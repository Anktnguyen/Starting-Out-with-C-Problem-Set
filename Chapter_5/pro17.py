"""
17. Prime Numbers
A prime number is a number that is only evenly divisible by itself and 1.
For example, the number 5 is prime because it can only be evenly divided by 1 and 5.
The number 6, however, is not prime because it can be divided evenly by 1, 2, 3 and 6.

Write a Boolean function named is_prime which takes an integer as an argument
and returns true if the argument is a prime number, or false otherwise.
Use the function is a program that prompts the user to enter a number then
displays a message indicating whether the number is prime.
"""
def main():
    number = int(input("Enter a number to check for prime: "))
    print(f"Number {number} is prime? {is_prime(number)} ")


def is_prime(number):
    if number > 1:
        #starting from 2 because 2 is a prime number
        for runs in range(2, number):
            if number % runs == 0:
                return False
        return True

if __name__ == "__main__":
    main()