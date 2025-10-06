# Experiment: Tic Tac Toe Game
# Name: Yash | Reg No: 19255

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Tic Tac Toe Game")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        # Input move
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("Cell already taken! Try again.")
            continue

        print_board(board)

        # Check winner
        if check_winner(board, player):
            print(f"Player {player} wins! 🎉")
            break

        # Check draw
        if is_full(board):
            print("It's a draw! 🤝")
            break

        turn += 1

# Run the game
tic_tac_toe()
