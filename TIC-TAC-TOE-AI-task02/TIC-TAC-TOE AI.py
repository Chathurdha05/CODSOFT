import math

# Initialize the game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Display the game board
def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check if a player has won
def is_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Check if the board is full
def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

# Get a list of all available moves
def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

# Apply a move to the board
def make_move(board, move, player):
    board[move[0]][move[1]] = player

# Minimax algorithm with optional Alpha-Beta pruning
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    if is_winner(board, 'O'):  # AI wins
        return 10 - depth
    if is_winner(board, 'X'):  # Human wins
        return depth - 10
    if is_full(board):  # Draw
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            make_move(board, move, 'O')
            eval = minimax(board, depth + 1, False, alpha, beta)
            make_move(board, move, ' ')
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            make_move(board, move, 'X')
            eval = minimax(board, depth + 1, True, alpha, beta)
            make_move(board, move, ' ')
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Find the best move for the AI
def find_best_move(board):
    best_value = -math.inf
    best_move = None
    for move in available_moves(board):
        make_move(board, move, 'O')
        move_value = minimax(board, 0, False)
        make_move(board, move, ' ')
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move

# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and the AI is 'O'.")
    display_board(board)

    while True:
        # Human player move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, 0-indexed, separated by a space): ").split())
                if board[row][col] == ' ':
                    break
                else:
                    print("Cell is already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        make_move(board, (row, col), 'X')
        display_board(board)

        if is_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        ai_move = find_best_move(board)
        make_move(board, ai_move, 'O')
        display_board(board)

        if is_winner(board, 'O'):
            print("AI wins! Better luck next time!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
