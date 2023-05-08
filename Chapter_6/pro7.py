"""7. Random Number File Writer"""

import random

def main():
    random_num = open('random_num.txt', 'a')
    total_num = int(input('Enter amount of random numbers to generate: '))
    for line in range(total_num):
        line = random.randint(1, 500)
        random_num.write(f"{line} \n")
    random_num.close()



if __name__ == "__main__":
    main()