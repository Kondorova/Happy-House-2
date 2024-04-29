def check_win(board, player):
    for row in board:
        for i in range(2):
            if all([cell == player for cell in row[i:i + 4]]):
                return True

    for col in range(5):
        for i in range(2):
            if all([board[row][col] == player for row in range(i, i + 4)]):
                return True

    for i in range(2):
        if all([board[row][col] == player for row, col in zip(range(i, i + 4), range(i, i + 4))]):
            return True
        if all([board[row][col] == player for row, col in zip(range(i, i + 4), range(4, i - 5, -1))]):
            return True

    return False