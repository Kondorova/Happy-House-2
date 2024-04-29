def print_board(board):
    print('   1   2   3   4   5')
    i = 0
    for row in board:
        i += 1
        print(i, ' | '.join(row), '|')
        print('-' * 20)