
# Искусственный интеллект: поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O, sum_X):
    import MapInitialization
    step = ""
    for line in MapInitialization.victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if MapInitialization.maps[line[j]] == "⭕️":
                o += 1
            if MapInitialization.maps[line[j]] == "❌":
                x += 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if MapInitialization.maps[line[j]] != "⭕️" and MapInitialization.maps[line[j]] != "❌":
                    step = MapInitialization.maps[line[j]]
                    return step  # Добавляем выход из функции

    return step



# Искусственный интеллект: выбор хода
def AI():
    import random
    import MapInitialization
    error_chance = random.randint(1, 3)  # Генерируем случайное число от 1 до 10
    if error_chance == 1:
        available_moves = [i for i in range(0, 9) if MapInitialization.maps[i] != "⭕️" and MapInitialization.maps[i] != "❌"]
        if not available_moves:
            return None  # Возвращаем None, если нет доступных ходов
        step = random.choice(available_moves)
    else:
        step = ""
        # 1) если на какой либо из победных линий 2 свои фигуры и 0 чужих - ставим
        step = check_line(2, 0)

        # 2) если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
        if step == "":
            step = check_line(0, 2)

            # 3) если 1 фигура своя и 0 чужих - ставим
        if step == "":
            step = check_line(1, 0)

            # 4) центр пуст, то занимаем центр
        if step == "":
            if MapInitialization.maps[4] != "❌" and MapInitialization.maps[4] != "⭕":
                step = 5

                # 5) если центр занят, то занимаем первую ячейку
        if step == "":
            if MapInitialization.maps[0] != "❌" and MapInitialization.maps[0] != "⭕":
                step = 1

    return step