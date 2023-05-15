"""
2. Sum of Digits in a String
Write a program that asks the user to enter a series of single-digit numbers with nothing
separating them. The program should display the sum of all the single digit numbers in the
string. For example, if the user enters 2514, the method should return 12, which is the sum
of 2, 5, 1, and 4.
"""

def main():
    user_input = input("Enter a chain of number (no space) to generate a sum: ")
    sum = 0
    #for loop to iterate through input string
    for num in user_input:
        #conditional checking if the input string is digit using isdigit() method
        if num.isdigit():
            #converting string type to integer type to compute for sum of input
            num = int(num)
            #adding all input digit
            sum += num
    print(sum)



if __name__ == "__main__":
    main()