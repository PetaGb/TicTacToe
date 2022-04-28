import random

current_player = "X"


def print_board(board):
    print("\n")
    print(board[0] + '|' + board[1] + '|' + board[2] + '  1|2|3')
    print('-+-+-  -+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5] + '  4|5|6')
    print('-+-+-  -+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8] + '  7|8|9')
    print("\n")


def player_input(board):
    try:
        inp = int(input("Enter the number 1-9: "))
        if inp in range(1, 10) and board[inp - 1] == "-":
            board[inp - 1] = current_player
        elif inp in range(1, 10) and board[inp - 1] != "-":
            print("This position is already taken")
            switch_player()
        elif inp not in range(1, 10):
            print("Your insert is out of range")
            switch_player()
    except ValueError:
        print("You must enter a number.")
        switch_player()


def player_win(board):
    if board[0] == board[1] and board[0] == board[2] and board[0] == "X":
        return True
    elif board[3] == board[4] and board[3] == board[5] and board[3] == "X":
        return True
    elif board[6] == board[7] and board[6] == board[8] and board[6] == "X":
        return True
    elif board[0] == board[3] and board[0] == board[6] and board[0] == "X":
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == "X":
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == "X":
        return True
    elif board[0] == board[4] and board[0] == board[8] and board[0] == "X":
        return True
    elif board[2] == board[4] and board[2] == board[6] and board[2] == "X":
        return True
    else:
        return False


def comp_win(board):
    if board[0] == board[1] and board[0] == board[2] and board[0] == "O":
        return True
    elif board[3] == board[4] and board[3] == board[5] and board[3] == "O":
        return True
    elif board[6] == board[7] and board[6] == board[8] and board[6] == "O":
        return True
    elif board[0] == board[3] and board[0] == board[6] and board[0] == "O":
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == "O":
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == "O":
        return True
    elif board[0] == board[4] and board[0] == board[8] and board[0] == "O":
        return True
    elif board[2] == board[4] and board[2] == board[6] and board[2] == "O":
        return True
    else:
        return False


def check_tie(board):
    if "-" not in board:
        return True


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def comp_run(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()
        elif check_tie(board):
            print("Its a tie")
            break
