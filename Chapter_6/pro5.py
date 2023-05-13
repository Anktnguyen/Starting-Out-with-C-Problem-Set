''' 5. Sum of Numbers'''

def main():
    sum = 0
    read_file = open(input('Enter file name: '), 'r')
    for line in read_file:
        #the following line of code will read each line and convert the value to float
        number = float(line.strip('\n'))
        sum += number
    print(f'The sum is {sum}')

    read_file.close()


if __name__ == '__main__':
    main()
