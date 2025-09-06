# Tic Tac Toe using simple DFS approach

# Board setup
board = ["-"] * 9

# Function to display board
def show_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

# Check winner or tie
def check_status():
    wins = [(0,1,2),(3,4,5),(6,7,8),  # rows
            (0,3,6),(1,4,7),(2,5,8),  # cols
            (0,4,8),(2,4,6)]          # diagonals
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "-":
            return "win"
    if "-" not in board:
        return "tie"
    return "play"

# Handle player turn
def take_turn(player):
    while True:
        pos = int(input(f"{player}'s turn (1-9): ")) - 1
        if 0 <= pos <= 8 and board[pos] == "-":
            board[pos] = player
            break
        print("Invalid move, try again.")
    show_board()

# Main loop
def play_game():
    show_board()
    player = "X"
    while True:
        take_turn(player)
        result = check_status()
        if result == "win":
            print(f"{player} wins!")
            break
        elif result == "tie":
            print("It's a tie!")
            break
        player = "O" if player == "X" else "X"

play_game()
