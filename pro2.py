'''2. File Head Display'''

def  main():
    output_file = open(input('Enter file name: '), 'r')

    for read_file in range (5):
        read_file = output_file.readline()
        print (read_file.rstrip('\n'))
    output_file.close()

main()