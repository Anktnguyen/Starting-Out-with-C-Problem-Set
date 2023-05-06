
def main():
    count = 0
    max = 0
    read_file = open('scores.txt', 'r')
    name = read_file.readline()
    while name != '':  #while the line is not a string
        name = name.rstrip('\n') #
        score = int(read_file.readline().strip()) #This line read numeric value and convert it to an integer
        if score > max: #Here is the condition to check for highest score and the name
            max = score
            highest_score = name
        name = read_file.readline()
        count += 1
    read_file.close()
    #Print out all of the findings
    print(f'{count} records in file.')
    print(f'The highest score is {max}')
    print(f'Name: {highest_score}')
    
if __name__ == '__main__':
    main()