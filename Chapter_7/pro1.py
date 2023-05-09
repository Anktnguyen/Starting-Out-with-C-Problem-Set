"""1. Valid Number Information

Design a program that uses a loop to build a list named valid_numbers that contains only
the numbers between 0 and 100 from the numbers list below. The program should then
determine and display the total and average of the values in the valid_numbers list."""


def main():
    #created empty list
    valid_numbers = []
    total = 0
    count = 0
    #prompt given list
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    #for loop to iterate through the list
    for number in numbers:
        #if statement to check for the given condition
        if number >= 0 and number <= 100:
            #append will add each number into the list
            valid_numbers.append(number)
            #Here is where the math happen
            total += number
            count += 1
    average = total /count
    #print everything out
    print(f'Valid numbers list: {valid_numbers}')
    print(f'Total is {total}')
    print(f'Average is {average:.2f}')


if __name__ == "__main__":
    main()