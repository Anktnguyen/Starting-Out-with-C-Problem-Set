"""
6. Average Number of Words
If you have downloaded the source code from the Premium Companion Website, you will
find a file named text.txt in the Chapter 08 folder. The text that is in the file is stored as
one sentence per line. Write a program that reads the file's contents and calculates the average
number of words per sentence.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com.)
"""
def main():
    #counter for the word
    count = 0
    open_file = open("text.txt", "r")
    read_file = open_file.readlines()

    open_file.close()
    #this for loop will read each line of the file
    for line in range(len(read_file)):
        #the current_total record previous amount of words read from count
        current_total = count
        #this for loop will count each word separated by a space (" ")
        for word in read_file[line].split(" "):
            #this count will count each word in the sentence separated by a space
            #It does not stop at the period but keep on counting i.e 
            #If first sentence has 13 words and second sentence has 28 words it will count the total = 31 words        
            count += 1
        #print out using {line+1} to counter the 0 index position
        #Here is a very important math equation using the new count (aka the total of all of the words) to subtract the current_total
        # which is the old count - because the program run from top to bottom so the count += 1 get updated with new value before current_total
        print(f"Line {line+1} has {count - current_total} words.")

    

if __name__ == "__main__":
    main()