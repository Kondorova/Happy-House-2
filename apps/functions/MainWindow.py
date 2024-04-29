import tkinter as tk
import field_3x3.main3
import field_5x5.main5
import field_3x3.DisplayingTheMap
import field_3x3.GameProcess
import field_3x3.AI
import field_3x3.MapInitialization

# Функция запуска игры
def start_game(field_size):
    # Создаем новое окно для игры
    game_window = tk.Tk()
    game_window.title("Крестики-нолики")

    if field_size == "3x3":
        field_3x3.main3.start_game3x3()
    elif field_size == "5x5":
        field_5x5.main5.start_game5x5()

# Создаем главное окно
window = tk.Tk()
window.title("Крестики-нолики")

# Создаем переменную для хранения выбранного поля
field_size = tk.StringVar()

# Создаем переменную для хранения выбранного оппонента
opponent = tk.StringVar()

# Создаем фрейм для выбора поля
field_frame = tk.Frame(window)
field_frame.pack()

# Создаем метку для выбора поля
field_label = tk.Label(field_frame, text="Выберите поле:")
field_label.pack(side=tk.LEFT)

# Создаем радиокнопки для выбора поля
field_size3x3 = tk.Radiobutton(field_frame, text="3x3", variable=field_size, value="3x3")
field_size3x3.pack(side=tk.LEFT)

field_size5x5 = tk.Radiobutton(field_frame, text="5x5", variable=field_size, value="5x5")
field_size5x5.pack(side=tk.LEFT)

# Создаем кнопку для запуска игры
start_button = tk.Button(window, text="Начать игру", command=lambda: start_game(field_size.get()))
start_button.pack()

# Запускаем главное окно
window.mainloop()




