import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Check rows
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Check columns

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Check diagonal from top-left to bottom-right
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Check diagonal from top-right to bottom-left

    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if is_valid_move(board, row, col):
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ai_move(board):
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == ' ']
    return random.choice(empty_cells)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        if current_player == 'X':
            row, col = player_move(board)
        else:
            print("AI's turn (O):")
            row, col = ai_move(board)

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
