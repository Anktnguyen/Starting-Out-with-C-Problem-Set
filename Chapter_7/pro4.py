"""
4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list then display the following data:
• The lowest number in the list
• The highest number in the list
• The total of the numbers in the list
• The average of the numbers in the list
"""

def main():
    #empty list to store number
    list_20num = []
    count = 0
    total = 0
    #while loop to count the number of entries
    while count < 20:
        user_num = int(input("Enter a number using integer: "))
        list_20num.append(user_num)
        #math
        total += user_num
        count += 1
    average = total / count

    #the result
    print(f"The list of number:\n"
          f"{list_20num}")
    print(f"The lowest number in the list is  {min(list_20num)}")
    print(f"The highest number in the list is {max(list_20num)}")
    print(f"The sum of all numbers is {total}")
    print(f"The average of all numbers is {average}")


if __name__ == "__main__":
    main()