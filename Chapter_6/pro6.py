"""6. Average Numbers"""

def main():
    file_read = open('numbers.txt', 'r')
    count = 0 #setting a base value
    sum = 0
    for line in file_read:
        count += 1
        #This line consolidate all of the conversion from string to int and do the calculation 
        sum += int(line.strip('\n'))   
    avg = sum / count
    print(f'The average is {avg}')

    file_read.close()

if __name__ == "__main__":
    main()
