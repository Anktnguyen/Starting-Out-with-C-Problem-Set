'''
Factorial
'''
#setting value at 1 to prevent mathematical error with 0
result = 1
def main():
    #This block make sure that input value is an integer
    try:
        number = int(input('Enter a number to see factorial result: '))
        factorial(number)
    except:
        print(None)


#factorial function
def factorial(num):
    #calling the global variable
    global result
    #if the number is less than 0 (negative integer), it will prints None
    if num >= 0:
        #if number is 0 which is 0!  then it will equal 1 because math
        if num == 0:
            result = 1
        #positive integer will be calculate here
        if num > 0:
            #this for loop multiple the number with decreasing in number value
            #5! = 5 * 4 * 3 * 2 * 1 = 120
            for factor in range(1, num + 1):
                result *= factor
        return print(f'Factorial of {num}! = {result}')
    else:
        print(None)    


if __name__ == '__main__':
    main()


