"""
1. Name Display
Write a program that gets strings containing a person's first and last name as separate
values.
The program should then display their initials, their name in the address book (first
name in title case and last name in upper case), and their username (a combination of their
first name's first letter and their full last name, all in lower case). For example, if the user
enters a first name of “John” and a last name of “Smith”, the program should display
“J.S.”, “John SMITH”, and “jsmith”.
"""

def main():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")

    #used index to access the first character of the input and joining them
    print(f_name[0] + '.' + l_name[0] + '.')
    #applying upper() method only to the first letter for the first name at index 0
    #joining the rest of first name using string slicing at index position 1: - indicate for the rest of the string
    print(f"{f_name[0].upper()}{f_name[1:]} {l_name.upper()}")
    #applying lower() method only to the first character of the first name using index
    print(f"{f_name[0].lower()}{l_name.lower()}")


if __name__ == "__main__":
    main()