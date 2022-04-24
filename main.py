from tttfunc import *

rules = """========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
\nLet's start the game:
---------------------"""
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


def main():
    print('Welcome to Tic Tac Toe!')
    print(rules)

    while True:
        print_board(board)
        player_input(board)
        switch_player()
        comp_run(board)
        if player_win(board):
            print_board(board)
            print("Congratulations, you won!")
            break

        elif comp_win(board):
            print_board(board)
            print("You just lost to random module! You can do it better :)")
            break

        elif check_tie(board):
            print_board(board)
            print("Its a tie!")
            break

        else:
            continue


if __name__ == "__main__":
    main()
