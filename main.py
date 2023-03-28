# Goal: Implement the game connect 4 for twoplayermode and singleplayer mode against AI

import gameround as round

def main():
    while True:
        winner = round.Round()
        print(winner)
        if winner == -1:
            break

if __name__ == '__main__':
    main()