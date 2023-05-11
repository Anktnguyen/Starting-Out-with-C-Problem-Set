"""
10. World Series Champions
If you have downloaded the source code, you will find a file named WorldSeriesWinners.
txt in the Chapter 07 folder. This file contains a chronological list of the World Series winning
teams from 1903 through 2009. (The first line in the file is the name of the team that
won in 1903, and the last line is the name of the team that won in 2009. Note the World
Series was not played in 1904 or 1994.)
Write a program that lets the user enter the name of a team, then displays the number of
times that team has won the World Series in the time period from 1903 through 2009.
"""

def main():
    #setting up reading of file
    read_file = open("WorldSeriesWinners.txt", "r")
    winner_list = read_file.readlines()
    read_file.close()


    #converting txt file into python list
    for line in range(len(winner_list)):
        winner_list[line] = winner_list[line].strip("\n")

    #setting up search option
    search = input("Enter team to calculate wins: ")
    if search in winner_list:
        #Here I am using the count function in python to count occurences of the string
        print(f"The team {search} has won {winner_list.count(search)} times during the World series from 1903 to 2009.")


    

if __name__ == "__main__":
    main()