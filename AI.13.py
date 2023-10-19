# Tic Tac Toe Minimax Algorithm

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def evaluate(board):
    # Check for a win, loss, or tie and return the corresponding score
    for row in board:
        if all(cell == "X" for cell in row):
            return 10
        elif all(cell == "O" for cell in row):
            return -10

    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return 10
        elif all(board[row][col] == "O" for row in range(3)):
            return -10

    if all(board[i][i] == "X" for i in range(3)) or all(board[i][2 - i] == "X" for i in range(3)):
        return 10
    elif all(board[i][i] == "O" for i in range(3)) or all(board[i][2 - i] == "O" for i in range(3)):
        return -10

    return 0

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if evaluate(board) == 10:
        return 10
    if evaluate(board) == -10:
        return -10
    if is_full(board):
        return 0

    if is_maximizing:
        max_eval = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = (-1, -1)
    best_val = -1000
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                move_val = minimax(board, 0, False)
                board[row][col] = " "
                if move_val > best_val:
                    best_move = (row, col)
                    best_val = move_val
    return best_move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Tic Tac Toe Minimax Algorithm")
    print_board(board)

    while True:
        player_row = int(input("Enter your row (0, 1, 2): "))
        player_col = int(input("Enter your column (0, 1, 2): "))
        if board[player_row][player_col] != " ":
            print("Invalid move. Try again.")
            continue
        board[player_row][player_col] = "O"

        if is_full(board):
            print("It's a tie!")
            break

        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = "X"

        print_board(board)

        if evaluate(board) == 10:
            print("You lose! The computer wins.")
            break
        elif evaluate(board) == -10:
            print("Congratulations! You win.")
            break

if __name__ == "__main__":
    main()
