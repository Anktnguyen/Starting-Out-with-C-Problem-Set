'''3. Line Numbers'''

def main():
    count = 0
    input_read = open(input('Enter file name:'), 'r')

    for line in input_read:
        count += 1
        print(f"Line {count}: {line.strip()}")
    input_read.close()

main()
    