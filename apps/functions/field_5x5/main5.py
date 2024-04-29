
def make_computer_move(board, player):
    import CheckWin
    import random

    if random.random() < 0.5:  # С вероятностью 50% компьютер попытается выстроить свои символы
        for i in range(5):
            for j in range(5):
                if board[i][j] == ' ':
                    board[i][j] = player  # Попробуем сделать ход компьютера
                    if CheckWin.check_win(board, player):  # Если это победный ход, сделаем его
                        return
                    else:
                        board[i][j] = ' '  # Отменить ход, так как он не победный

    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                # Проверка на победу игрока, если компьютер сделает ход в клетку [i][j]
                board[i][j] = player
                if CheckWin.check_win(board, player):
                    return
                board[i][j] = ' '  # Вернуть клетку в исходное состояние

    # Рассматриваем все возможные линии на игровом поле для блокировки ходов игрока
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                # Проверка на возможный выигрыш игрока, если компьютер заблокирует клетку [i][j]
                board[i][j] = player[1]
                if CheckWin.check_win(board, player[1]):
                    return
                board[i][j] = ' '  # Вернуть клетку в исходное состояние

    # Если не удалось ни блокировать игрока, ни завершить игру, сделаем случайный ход
    empty_cells = [(i, j) for i in range(5) for j in range(5) if board[i][j] == ' ']
    row, col = random.choice(empty_cells)
    board[row][col] = player


def select_player():
    choice = int(input("Who do you want to play with? (0 - human, 1 - computer): "))
    return choice

def start_game5x5():
    import PrintBoard
    import CheckWin
    import random
    board = [[' ' for _ in range(5)] for _ in range(5)]
    players = ['❌', '⭕️']
    player_idx = 0

    PrintBoard.print_board(board)

    play_with_computer = select_player()

    while True:
        row = int(input(f'Player {players[player_idx]}, enter row (1-5): ')) - 1
        col = int(input(f'Player {players[player_idx]}, enter column (1-5): ')) - 1

        if board[row][col] != ' ':
            print('Cell is already taken. Try again.')
            continue

        board[row][col] = players[player_idx]

        PrintBoard.print_board(board)

        if CheckWin.check_win(board, players[player_idx]):
            print(f'Player {players[player_idx]} wins!')
            break

        if all(all(cell != ' ' for cell in row) for row in board):
            print('It\'s a tie!')
            break

        # Добавим символ для компьютера
        computer_symbol = '⭕️'

        if play_with_computer:
            player_idx = (player_idx + 1) % 2
            make_computer_move(board, computer_symbol)
            PrintBoard.print_board(board)

            if CheckWin.check_win(board, computer_symbol):
                print(f'Player {computer_symbol} wins!')
                break

        player_idx = (player_idx + 1) % 2

start_game5x5()