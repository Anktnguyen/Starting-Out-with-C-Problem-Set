"""
3. Date Printer
Write a program that reads a string from the user containing a date in the form mm/dd/yyyy.
It should print the date in the format March 12, 2018.
"""

#Program does not validate years with 27 or 28 days in February.
#This program is used for printing and string conversion of the month
def main():
    user_input = input("Enter month and date in mm/dd/yyyy format: ")

    #created a list of all the month in string format
    month_list = ["January", "February", "March", 
                  "April", "May", "June",
                  "July", "August", "September",
                  "October", "November", "December"]
    
   #converting all of the string input value to appropriate integer value
    month = int(user_input[0:2]) 
    day = int(user_input[3:5])
    year = int(user_input[6:10])

    #conditional format using month to access month_list index
    
    if month == 1 or month <= 12:
        if month != 2:
            if day == 1 or day <= 31:
                if year > 0:
                    #printing portion have [month-1] because index start at 0
                    #can also do month = int(user_input[0:2]) - 1
                        print(f"{month_list[month-1]} {day}, {year}")

    #This is for february when there are only 27/28 days
    #This program does not validate which year has 27 or 28 days
    if month == 2:
        if day == 1 or day <= 28:
            if year > 0:
                print(f"{month_list[month-1]} {day}, {year}")
        else:
            print("February has 27 or 28 days.")
    


if __name__ == "__main__":
    main()