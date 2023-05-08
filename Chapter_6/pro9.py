"""Exception handing"""

def main():
    try:
        read_file = open(input('Enter file name: '), 'r')
        total = 0
        count = 0
        try:
            for line in read_file:
                total += int(line.strip('\n'))
                count +=1
            average = total / count
            print(f'The average is {average}')

        except ValueError:
            print(f'Calculation error')

        read_file.close()
    except IOError:
        print("Input/Output Error. Files might not exist in the directory.")
        print(f'The file is {read_file}')



if __name__ == "__main__":
    main()