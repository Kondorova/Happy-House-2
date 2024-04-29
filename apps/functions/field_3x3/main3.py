
def start_game3x3():
    import DisplayingTheMap
    import GameProcess
    import AI
    import MapInitialization

    human_or_computer = int(input("Who do you want to play with? (1 - human, 2 - computer): "))

    # Основная программа
    game_over = False
    player1 = True

    steps = 9
    while game_over == False:

        # 1. Показываем карту
        DisplayingTheMap.print_maps()
        if human_or_computer == 1:
            if steps != 0:
                # 2. Спросим у играющего куда делать ход
                if player1 == True:
                    symbol = "❌"
                    step = int(input("Person 1, your move: "))
                else:
                    symbol = "⭕"
                    step = int(input("Person 2, your move: "))
                while step not in MapInitialization.maps:
                    step = int(input("Invalid value, try again: "))
                GameProcess.step_maps(step, symbol)  # делаем ход в указанную ячейку
                win = GameProcess.get_result()  # определим победителя
                if win != "":
                    game_over = True
                else:
                    game_over = False
            else:
                print("It\'s a tie!")
                game_over = True
                win = "Friendship"
            steps -= 1

        else:
            # 2. Спросим у играющего куда делать ход
            if player1 == True:
                symbol = "❌"
                step = int(input("Person, your move: "))
            else:
                print("The computer makes its move: ")
                symbol = "⭕️"
                step = AI.AI()
            # 3. Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
            if step != "" and step in MapInitialization.maps:
                GameProcess.step_maps(step, symbol)  # делаем ход в указанную ячейку
                win = GameProcess.get_result()  # определим победителя
                if win != "":
                    game_over = True
                else:
                    game_over = False
            else:
                print("It\'s a tie!")
                game_over = True
                win = "Friendship"

        player1 = not(player1)

    # Игра окончена. Покажем карту. Объявим победителя.
    DisplayingTheMap.print_maps()
    print("Winner: ", win)

start_game3x3()