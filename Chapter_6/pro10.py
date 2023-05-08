"""Golf Scores"""

def main():
    file = open("golf.txt", 'w')
    players = int(input('Enter the amount of golfer(s): '))
    print(f'Total golfer(s) are {players}')

    #This for loop will write golfer(s) name and the scores
    for player in range(players):
        player = str(input('Enter golfer name: '))
        score = float(input('Enter score of the golfer: '))
        file.write(f'golfer {player} : {score}\n')

    file.close()

    file = open('golf.txt', 'r')
    for line in file:
        print(line.strip())
    file.close()

if __name__ == "__main__":
    main()

