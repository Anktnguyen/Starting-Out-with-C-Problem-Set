"""
8. Word List File Reader
This exercise assumes you have completed the Programming Exercise 8, Word List File
Writer, from Chapter 6. Write another program that reads the words from the file and displays
the following data:
• The number of words in the file.
• The longest word in the file.
• The average length of all of the words in the file.
"""

def main():

    #create a while loop
    create_file = open("words.txt", "w+")

    while True:
        user_input = input("Enter each word to create a Word List File or type exit to end: ")
        if user_input == 'exit':
            break
        create_file.write(f"{user_input}\n")
    create_file.close()

    open_file = open("words.txt", "r")
    word_list = open_file.readlines()

    open_file.close()

    count = 0
    total = 0
    #temporary storage for characters count for each word
    temp_max = 0
    #variable to store the longest word for print out
    longest_word = ""

    #for loop iterate through all of the word elements
    for word in range(len(word_list)):
        #count the elements in the word file list
        count += 1
        #iteration through each characters within each word
        for ch in word_list[word]:
            #isalpha() used here because the input was set with \n (end line)
            if ch.isalpha():
                #comparing characters length and find the longest word (with most characters)
                if len(word_list[word]) > temp_max:
                    #len is used here to obtain the count in integer, strip away the end line to get a correct count 
                    temp_max = len(word_list[word].strip("\n"))
                    #longest word is now stored in a variable for print out
                    longest_word = word_list[word]
                #this total count the total of all of the characters from user input words
                total += 1

            
            
    print(f"{count} word(s) in the file.")
    print(f"{total/count} average length of all of the word(s).")
    print(f"The longest word has {temp_max} character(s) and the word is {longest_word}")
            





if __name__ == "__main__":
    main()
