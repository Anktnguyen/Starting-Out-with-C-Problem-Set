"""
12. File Line Viewer
Write a program that asks the user for the name of a file. The program should read all of
the file's data into a list and display the number of lines of data that the file contains, and
then ask the user to enter the number of the line that he or she wants to view. The program
should display the specified line.
The program should handle the following exceptions by displaying an error message:
• IOError exceptions that are raised when the specified filename cannot be found or opened.
• ValueError exceptions that are raised when a non-integer value is given as a line number.
• IndexError exceptions that are raised when the line number is outside the range of the
data list.
"""


def main():
    count = 0
    try:
        #Opening the file and read the lines into the list
        read_file = open(input("Enter name of the file: "), "r")
        list_file = read_file.readlines()

        read_file.close()

         #putting the each line of the file into the list
        for line in range(len(list_file)):
            list_file[line] = list_file[line].strip("\n")
            #counting amount of lines in the file
            count += 1
        print(f"The file has {count} lines.")
    except IOError:
        print("File cannot be open. File is not in the current directory or does not exist.")


    try:
        read_line = int(input("Enter the amount of line to display: "))
        try:
            #set this up for bound checking
            list_file[read_line]
            #print the line out using index [start:finish]
            print(f"{list_file[0:read_line]}")
        except IndexError:
            print(f"Input value {read_line} is out of bound. The file contain {count} line ")
    except ValueError:
        print(f"Input value is invalid")

if __name__ == "__main__":
    main()