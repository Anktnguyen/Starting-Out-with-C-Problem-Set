"""
13. Magic 8 Ball
Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a
random response to a yes or no question. In the student sample programs for this book, you
will find a text file named 8_ball_responses.txt. The file contains 12 responses, such
as “I don't think so”, “Yes, of course!”, “I'm not sure”, and so forth. The program should
read the responses from the file into a list. It should prompt the user to ask a question, then
display one of the responses, randomly selected from the list. The program should repeat
until the user is ready to quit.
Contents of 8_ball_responses.txt:
Yes, of course!
Without a doubt, yes.
You can count on it.
For sure!
Ask me later.
I'm not sure.
I can't tell you right now.
I'll tell you after my nap.
No way!
I don't think so.
Without a doubt, no.
The answer is clearly NO.
"""
import random

def main():
    read_file = open('8_ball_responses.txt', 'r')
    responses_list = read_file.readlines()

    read_file.close()

    #For loop used to converting txt to list in python
    for line in range(len(responses_list)):
        responses_list[line] = responses_list[line].strip("\n")

    user_interaction = input("Enter your question for an answer from the 8 Magic Ball: ")

    #This while loop keep allow user to continue playing
    while user_interaction != " ":

        #The random module has a choice function that allow the element in the list to be select at random
        #I reference the random module options from here - https://stackabuse.com/how-to-randomly-select-elements-from-a-list-in-python/
        print(random.choice(responses_list))
        print("Type 'exit' in all lower case to end.")
        user_interaction = input("Enter next question to continue or exit to end: ")
        #This conditional statement provide user with an option to continue or to end the interaction
        if user_interaction == "exit":
            print("Program terminated...")
            break


if __name__ == "__main__":
    main()