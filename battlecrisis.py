import random
from time import sleep

board = []

print("Welcome to Battlecrisis!\n")

p1name = input("Player 1, please enter your name: ")
p2name = input("Player 2, please enter your name: ")
sleep(0.5)

for x in range(20):
    board.append(["."] * 30)

def print_board(board):
    for row in board:
        print(" ".join(row))

#print_board(board)

mines = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], ]

def create_mines():
    for i in mines:
        i[1] = random.randint(1,29)
        i[0] = random.randint(1,19)

create_mines()

# Remove this later
#for i in mines:
#    print(i)

for i in mines:
    board[i[0]][i[1]] = "!"

#print_board(board)

def is_dead(P1DEAD, P2DEAD, x1, x2, y1, y2):
    for i in mines:
        if i[1] == x1 and i[0] == y1:
            print(f"{p1name} died!")
            P1DEAD = True
        if i[1] == x2 and i[0] == y2:
            print(f"{p2name} died!")
            P2DEAD = True


def main():

    print("-"*20)
    print("\nHow to Play\n")
    print("Move using W, A, S, and D.")
    print("Each player controls one character, and either plays against another player, or against the computer.")
    print("Choose option 1 for multiplayer, or option 2 for computer.")
    print("\nReach the other side first while avoiding mines to win.")
    print("If you step on a mine, the game is over.")
    print("Good luck!\n")
    print("-"*20, "\n")


    mode = input("Which mode would you like to play? ")
    if mode == "2":
        pass
    elif mode == "1":
        x_pos = 1
        y_pos = 5
        x_pos2 = 1
        y_pos2 = 6

        P1DEAD = False
        P2DEAD = False

        while not P1DEAD and not P2DEAD:
            move = input(f"{p1name}, which direction would you like to move? ")
            if move == "W":
                board[x_pos][y_pos] = "."
                y_pos -= 1
                board[y_pos][x_pos] = "X"
            elif move == "A":
                board[x_pos][y_pos] = "."
                x_pos -= 1
                board[y_pos][x_pos] = "X"
            elif move == "S":
                board[x_pos][y_pos] = "."
                y_pos += 1
                board[y_pos][x_pos] = "X"
            elif move == "D":
                board[x_pos][y_pos] = "."
                x_pos += 1
                board[y_pos][x_pos] = "X"

            move2 = input(f"{p2name}, which direction would you like to move? ")
            if move2 == "W":
                board[x_pos2][y_pos2] = "."
                y_pos2 -= 1
                board[y_pos2][x_pos2] = "O"
            elif move2 == "A":
                board[x_pos2][y_pos2] = "."
                x_pos2 -= 1
                board[y_pos2][x_pos2] = "O"
            elif move2 == "S":
                board[x_pos2][y_pos2] = "."
                y_pos2 += 1
                board[y_pos2][x_pos2] = "O"
            elif move2 == "D":
                board[x_pos2][y_pos2] = "."
                x_pos2 += 1
                board[y_pos2][x_pos2] = "O"


            print(f"Player 1 position: {x_pos}, {y_pos}.")
            print(f"Player 2 position: {x_pos2}, {y_pos2}.")
            is_dead(P1DEAD, P2DEAD, x_pos, x_pos2, y_pos, y_pos2)
            print_board(board)

main()
