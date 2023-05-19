"""
11. Word Separator
Write a program that accepts as input a sentence in which all of the words are run together,
but the first character of each word is uppercase. Convert the sentence to a string in which
the words are separated by spaces, and only the first word starts with an uppercase letter. For
example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
the roses.”
"""

def main():
    user_input = input("Enter a sentence without space to use the word separator: ")
    #user input
    new_list = ""

    #for loop iterate through the list of strings 
    for char in range(len(user_input)):
        #this if condition keep the first word uppercase 
        if char == 0:
            new_list += " " + user_input[char]
            #skip
            continue
        #starting at every capitalize letter it will concatenate with a space as separator and convert them to lower case
        if user_input[char].istitle():
            new_list += " " + user_input[char].lower()
        #this else statement concatenate the original lower case character to the previous capitalized charater.
        else:
            new_list += user_input[char]
    print(new_list)

#alternative version start at index 1 without skipping (using continue) in the for loop
    # new_list = ""
    # new_list += user_input[0]
    # for char in range(1, len(user_input)):
    #     if user_input[char].istitle():
    #         new_list += " " + user_input[char].lower()
    #     else:
    #         new_list += user_input[char]
    # print(new_list)

if __name__ == "__main__":
    main()