from Grid import printing_board
from Toss import cointoss

# THE CHOICE OF SYMBOL BETWEEN Player1 and Player2
def choosing_symbol():
    global symbol1, symbol2
    symbol = 0
    while symbol not in ["X", "O"]:
        symbol = input("Choose the Symbol, 'X' or 'O': ").upper()
        if symbol == "X":
            symbol1 = "X"
            symbol2 = "O"
        elif symbol == "O":
            symbol1 = "O"
            symbol2 = "X"
        else:
            print("Invalid input. Please enter again.")

# LIST FOR BOARD
def initialize_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

# In this step, we'll get inputs from players
def player_input(board, symbol):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    position = 0
    while position not in numbers:
        position = input(f"Enter the number of the cell you want to place your {symbol}, 1-9:\n")
        if position == "1" and board[0][0] == " ":
            board[0][0] = symbol
        elif position == "2" and board[0][1] == " ":
            board[0][1] = symbol
        elif position == "3" and board[0][2] == " ":
            board[0][2] = symbol
        elif position == "4" and board[1][0] == " ":
            board[1][0] = symbol
        elif position == "5" and board[1][1] == " ":
            board[1][1] = symbol
        elif position == "6" and board[1][2] == " ":
            board[1][2] = symbol
        elif position == "7" and board[2][0] == " ":
            board[2][0] = symbol
        elif position == "8" and board[2][1] == " ":
            board[2][1] = symbol
        elif position == "9" and board[2][2] == " ":
            board[2][2] = symbol
        else:
            print("Invalid number or cell already taken. Enter again.")

# CONDITIONS FOR WIN AND DRAW.
def check_win(board):
    symbols = [symbol1, symbol2]

    for symbol in symbols:
        for i in range(3):
            # Check rows and columns
            if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
                print(f"{symbol} won!")
                return True

        # Check diagonals
        if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
            print(f"{symbol} won!")
            return True

    # Check for a draw
    if all(cell != " " for row in board for cell in row):
        print("Game is a draw.")
        return True

    return False

# ___________________ GAME STARTING POINT ___________________#
print("_______________________________________________________________________________________________________________\n")
print("                                             Welcome to The Game                                                 ")
print("                                                 Tic-Tac-Toe                                                     ")
print("_______________________________________________________________________________________________________________\n")

name1 = input("Please enter the name for Player 1:\n") or "Player 1"
name2 = input("Please enter the name for Player 2:\n") or "Player 2"

game_repetition = "Y"
while game_repetition == "Y":
    board = initialize_board()
    printing_board(board)
    choosing_symbol()
    user_turn = cointoss()
    if user_turn:
        print(f"{name1} won the toss. {name1} will go first.")
    else:
        print(f"{name2} won the toss. {name2} will go first.")

    while True:
        if user_turn:
            player_input(board, symbol1)
        else:
            player_input(board, symbol2)

        printing_board(board)

        if check_win(board):
            break
        else:
            user_turn = not user_turn

    game_repetition = input("Do you want to repeat the game?\n'Y' for Yes and 'N' for No. Anything else will be considered as No:\n").upper()

print("Game has ended. Thank you for playing.")