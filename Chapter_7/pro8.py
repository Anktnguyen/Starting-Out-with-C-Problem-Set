"""
8. Name Search
If you have downloaded the source code, you will find the following files in the Chapter 07
folder:
• GirlNames.txt This file contains a list of the 200 most popular names given to girls
born in the United States from the year 2000 through 2009.
• BoyNames.txt This file contains a list of the 200 most popular names given to boys
born in the United States from the year 2000 through 2009.

Write a program that reads the contents of the two files into two separate lists. The user
should be able to enter a boy's name, a girl's name, or both, and the application will display
messages indicating whether the names were among the most popular.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com.)
"""


#I use a lot of try and except in this program and I will be using try and except in the rest of my code
#wherever they are applicable to understand the logical error 
def main():

    start_search = str(input("Searching for popular boy or girl name or both (yes or no, y or n) or press any string key to exit: "))
    #while loop menu to make the program slightly more interactive
    while start_search == 'y' or start_search == 'yes':
        boy_or_girl_or_both = str(input("Look up only boy name or girl name or both (type boy or girl or both) in all lower case: "))
        while boy_or_girl_or_both == 'girl' or boy_or_girl_or_both == 'boy' or boy_or_girl_or_both == 'both':
            try: 
                if boy_or_girl_or_both == "girl":
                    name = str(input("Enter a girl name: "))
                    girl_name(name)
                elif boy_or_girl_or_both == "boy":
                    name = str(input("Enter a boy name: "))
                    boy_name(name)
                elif boy_or_girl_or_both == "both":
                    gname = str(input("Enter a girl name: "))
                    bname = str(input("Enter a boy name: "))
                    girl_name(gname)
                    boy_name(bname)
            except ValueError:
                print("Value error, type the option in all lower case.")
                boy_or_girl_or_both = str(input("Look up only boy name or girl name or both (type boy or girl or both) in all lower case: "))
        else:
            print("Cannot compute command...Restarting...")
        start_search = str(input("Search for names again? yes or no (y or n): "))
    

#function to open up Girl Names file and add them into the list
def girl_name(name):
    open_girl_name = open('GirlNames.txt', "r")
    girl_name_list = open_girl_name.readlines()
    open_girl_name.close()
    try:
        for line in range(len(girl_name_list)):
            girl_name_list[line] = girl_name_list[line].strip("\n")
        try:
            girl_name_list.index(name)
            print(f"{name} is in 200 popular girl name") 
        except ValueError:
            print(f"{name} is not in the list.")
    except IOError:
        print("File cannot be open. File does not exist or not found in the directory.")

#function to open up Boy Names file and add them into the list
def boy_name(name):
    open_boy_name = open("BoyNames.txt", "r")
    boy_name_list = open_boy_name.readlines()
    open_boy_name.close()

    try:
        for line in range(len(boy_name_list)):
            boy_name_list[line] = boy_name_list[line].strip("\n")
        try:
            boy_name_list.index(name)
            print(f"{name} is in 200 popular boy name")
        except ValueError:
            print(f"{name} is not in the list.")

    except IOError:
        print("File cannot be open. File does not exist or not found in the directory.")
    return boy_name_list

if __name__ == "__main__":
    main()