
#Game Board
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]

game_still_going =True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # game has ended
    if winner == "X" or winner == "O":
        print(winner + "Won")
    elif winner is None:
        print("Tie")


def handle_turn(player):
    position = input("Choose a position from (1-9):")
    position = int(position) - 1

    board[position] = "X"
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global winner
    # rows
    row_winner = check_rows()
    # columns
    column_winner = check_columns()
    # diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner()
    elif column_winner:
        winner = column_winner()
    elif diagonal_winner:
        winner = diagonal_winner()
    else:
        winner = None
    return


def check_rows():

    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"


    return

def check_columns():
    return

def check_diagonals():
    return

def check_if_tie():
    return


def flip_player():
    return






play_game()
