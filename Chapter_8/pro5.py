"""
5. Alphabetic Telephone Number Translator
Many companies use telephone numbers like 555-GET-FOOD so the number is easier for
their customers to remember. On a standard telephone, the alphabetic letters are mapped to
numbers in the following fashion:
A, B, and C = 2
D, E, and F = 3
G, H, and I = 4
J, K, and L = 5
M, N, and O = 6
P, Q, R, and S = 7
T, U, and V = 8
W, X, Y, and Z = 9
Write a program that asks the user to enter a 10-character telephone number in the format
'YYY-YYY-YYYY'. The application should display the telephone number with any
alphabetic characters that appeared in the original translated to their numeric equivalent.
For example, if the user enters 555-GET-FOOD, the application should display
555-438-3663
"""

def main():
    phone_num_char = input("Enter a phone number mixed with number and letters i.e 555-GET-FOOD: ").upper()
    #print(phone_num_char)
    #This variable has an empty string and will be use to store the convereted number
    phone_number = ""

    #for loop iterate through each character in the string
    for line in phone_num_char:
        #using isdigit() method to separate digit from alphabet
        #if it is digit then it will be added 
        if line.isdigit():
            phone_number += line
        #Here is where all of the alphabet conversion to numbers take place
        if line.isalpha():
            if line == "A" or line == "B" or line == "C":
                #conv_num is a variable storing the converted value
                conv_num = "2"
                phone_number += line
            elif line == "D" or line == "E" or line == "F":
                conv_num = "3"
            elif line == "G" or line == "H" or line == "I":
                conv_num = "4"
            elif line == "J" or line == "K" or line == "L":
                conv_num = "5"
            elif line == "M" or line == "N" or line == "O":
                conv_num = "6"
            elif line == "P" or line == "Q" or line == "R":
                conv_num = "7"
            elif line == "T" or line == "U" or line == "V":
                conv_num = "8"
            elif line == "W" or line == "X" or line == "Y" or line == "Z":
                conv_num = "9"
            #finally to concatenate all of the converted value to the digit
            phone_number += conv_num
    #printing out the converted phone number using string slicing to meet the format standard
    print(f"{phone_number[:3]}-{phone_number[3:6]}-{phone_number[6:]}")






if __name__ == "__main__":
    main()