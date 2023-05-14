"""
15. 1994 Weekly Gas Graph
In the student sample programs for this book, you will find a text file named 1994_Weekly_
Gas_Averages.txt. The file contains the average gas price for each week in the year 1994.
(There are 52 lines in the file.) Using matplotlib, write a Python program that reads the
contents of the file then plots the data as either a line graph or a bar chart. Be sure to display
meaningful labels along the X and Y axes, as well as the tick marks.
"""

import matplotlib.pyplot as plt

def main():
    count = 0
    week_count = []
    open_file = open("1994_Weekly_Gas_Averages.txt", "r")
    read_file = open_file.readlines()

    open_file.close()

    #for loop iterate through each value and add them into the list
    for line in range(len(read_file)):
        read_file[line] = float(read_file[line].strip("\n"))
        #week_count is a list contain count for each week i.e. week 1, 2, 3 etc...
        #It is also being used as x axis value - independent variable (the cause)
        count += 1
        week_count.append(count)
        
    # print(read_file)
    #print(week_count)

    #week_count is the independent value (x-axis) aka the cause - weeks being recorded
    #read_file is the dependent value (y-axis) aka the effect - gas prices
    plt.plot(week_count, read_file)

    plt.title("1994 Weekly Gas Averages")

    #x and y labels
    plt.xlabel("Weeks")
    plt.ylabel("Gas prices")

    #this part shorting grid for visual improvement
    plt.grid(True)

    plt.show()



if __name__ == "__main__":
    main()