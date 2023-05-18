"""
7. Character Analysis
If you have downloaded the source code, you will find a file named text.txt in the Chapter
08
folder. Write a program that reads the file's contents and determines the following:
• The number of uppercase letters in the file
• The number of lowercase letters in the file
• The number of digits in the file
• The number of whitespace characters in the file
"""


def main():
    open_file = open("text.txt", "r")
    read_file = open_file.readlines()

    open_file.close()
    #Each condition has it own varaibles for tracebility.
    count_upper = 0
    count_lower = 0
    count_digits = 0
    count_spaces = 0

    #this for loop iterate through the file
    for line in range(len(read_file)):
        #This for loop count each word separately
        for word in read_file[line].split(" "):
            if word.isupper():
                count_upper += 1
            elif word.islower():
                count_lower += 1
            #using isalnum() instead of isdigit() because some text contain number in different format
            elif word.isalnum(): #use isdigit() for digit only
                count_digits += 1
        #same for loop as above without the split at every space to count the word.
        for word in read_file[line]:
            if word.isspace():
                count_spaces += 1
    
    print(f"{count_upper} upper case word(s).")
    print(f"{count_lower} lower case word(s).")
    print(f"{count_digits} digit(s).")
    print(f"{count_spaces} white space character(s).")
        



if __name__ == "__main__":
    main()