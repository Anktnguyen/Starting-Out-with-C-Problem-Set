"""Word List File Writer"""


def main():
    write_file = open('words.txt', 'a')
    amount = int(input('Amount of words to enter (answer in numeric value): '))

    for line in range(amount):
        line = input("Enter the word: ")
        write_file.write(f"{line} \n")

    write_file.close()

if __name__ == "__main__":
    main()
