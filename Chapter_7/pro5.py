"""
5. Charge Account Validation
If you have downloaded the source code from the Premium Companion Website, you will
find a file named charge_accounts.txt in the Chapter 07 folder. This file has a list of a
company's valid charge account numbers. Each account number is a seven-digit number,
such as 5658845.
Write a program that reads the contents of the file into a list. The program should then
ask the user to enter a charge account number. The program should determine whether
the number is valid by searching for it in the list. If the number is in the list, the program
should display a message indicating the number is valid. If the number is not in the list, the
program should display a message indicating the number is invalid.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com.)

"""

def main():
    read_list = open('charge_accounts.txt', 'r')
    account_list = read_list.readlines()
    read_list.close()

    #Converting the data in file into a list
    try:
        for line in range(len(account_list)):
            account_list[line] = int(account_list[line].strip("\n"))
        print("\nAccount list have been created.\n\n")
    except IOError:
        print("File error, not found in current directory or does not exist.")

    #this line is to check for account list if needed
    #print(account_list)
    
    #Interactive portion for user to search for account number in the list
    run = input("Search for account number? yes or no (y or n): ")

    while run == "y" or run == "yes":
        try:
            #Taking input value and search for the number in the list
            num = int(input("Enter an account number (7-digit integer): "))
            account_list.index(num)
            print(f"{num} exist in the list")
        except ValueError:
            print("Value error, that item does not exist.")
        run = input("Search again? yes or no (y or n): ")



if __name__ == "__main__":
    main()