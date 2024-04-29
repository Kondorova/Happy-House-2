
# Сделать ход в ячейку
def step_maps(step, symbol):
    import MapInitialization
    ind = MapInitialization.maps.index(step)
    MapInitialization.maps[ind] = symbol


# Получить текущий результат игры
def get_result():
    import MapInitialization
    win = ""

    for i in MapInitialization.victories:
        if MapInitialization.maps[i[0]] == "❌" and MapInitialization.maps[i[1]] == "❌" and MapInitialization.maps[i[2]] == "❌":
            win = "❌"
        if MapInitialization.maps[i[0]] == "⭕" and MapInitialization.maps[i[1]] == "⭕" and MapInitialization.maps[i[2]] == "⭕":
            win = "⭕"

    return win
