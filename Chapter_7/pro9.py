"""
9. Population Data
If you have downloaded the source code, you will find a file named USPopulation.txt
in the Chapter 07 folder. The file contains the midyear population of the United States, in
thousands, during the years 1950 through 1990. The first line in the file contains the population
for 1950, the second line contains the population for 1951, and so forth.
Write a program that reads the file's contents into a list. The program should display the
following data:
• The average annual change in population during the time period
• The year with the greatest increase in population during the time period
• The year with the smallest increase in population during the time period
"""

def main():

    read_file = open("USpopulation.txt", "r")
    count = 0
    total = 0
    population_list = read_file.readlines()
    #The range and len function works for exclusively for string 
    #The for loop iterate through the list of string adding them into the list
    for line in range(len(population_list)):
        population_list[line] = int(population_list[line].strip("\n"))
        total += population_list[line]
        count +=1
    average = total / count
    #the following lines use the starting year plus the index of the list to determine a specific year
    max_year = 1950 + population_list.index(max(population_list))
    min_year = 1950 + population_list.index(min(population_list))
    # print(population_list)
    print(f"The total population is {total}")
    print(f"The annual average change in population during 1950-1990 is {average:.2f}.")
    print(f"Year {max_year} has the highest population of {max(population_list)}")
    print(f"Year {min_year} has the lowest population of {min(population_list)}")



if __name__ == "__main__":
    main()