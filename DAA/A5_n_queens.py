# Practical 5: N-Queens Problem (Backtracking)

def place_queens(row, cols, left_diag, right_diag, positions):
    n = len(cols)

    if row == n:
        return True

    for col in range(n):
        if cols[col] or right_diag[row + col] or left_diag[row - col + n - 1]:
            continue

        cols[col] = 1
        right_diag[row + col] = 1
        left_diag[row - col + n - 1] = 1
        positions.append(col)

        if place_queens(row + 1, cols, left_diag, right_diag, positions):
            return True

        positions.pop()
        cols[col] = 0
        right_diag[row + col] = 0
        left_diag[row - col + n - 1] = 0

    return False


def n_queen(n):
    cols = [0] * n
    left_diag = [0] * (2 * n)
    right_diag = [0] * (2 * n)
    positions = []

    if place_queens(0, cols, left_diag, right_diag, positions):
        board = [['.' for _ in range(n)] for _ in range(n)]
        for i in range(n):
            board[i][positions[i]] = 'Q'
        return board

    return None


def print_board(board):
    if board:
        for row in board:
            print(" ".join(row))
    else:
        print("No solution exists.")


n = int(input("Enter the number of queens: "))
board = n_queen(n)

print("\nSolution:")
print_board(board)
