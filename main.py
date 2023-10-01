import tkinter as tk

RADIUS = 30
STEP = 10


"""move_left(event): Эта функция перемещает круг на холсте влево на 
фиксированный шаг (STEP), когда событие "Left" (стрелка влево) обнаруживается.
Она вызывается при нажатии клавиши стрелки влево."""
def move_left(event):
    canvas.move(circle, -STEP, 0)

"""move_right(event): Эта функция перемещает круг на холсте вправо на фиксированный 
шаг (STEP), когда событие "Right" (стрелка вправо) обнаруживается. 
Она вызывается при нажатии клавиши стрелки вправо."""
def move_right(event):
    canvas.move(circle, STEP, 0)

"""move_up(event): Эта функция перемещает круг на холсте вверх на фиксированный шаг (STEP), 
когда событие "Up" (стрелка вверх) обнаруживается. Она вызывается при нажатии клавиши стрелки вверх."""
def move_up(event):
    canvas.move(circle, 0, -STEP)

"""move_down(event): Эта функция перемещает круг на холсте вниз на 
фиксированный шаг (STEP), когда событие "Down" (стрелка вниз) обнаруживается. 
Она вызывается при нажатии клавиши стрелки вниз."""
def move_down(event):
    canvas.move(circle, 0, STEP)

"""change_color_up(event): Эта функция изменяет цвет круга на холсте
 на следующий цвет из заданного списка (colors) при нажатии клавиши "PgUp" (страница вверх). 
Она циклически переключается между цветами."""
def change_color_up(event):
    global current_color_index
    current_color_index = (current_color_index + 1) % len(colors)
    canvas.itemconfig(circle, fill=colors[current_color_index])

"""change_color_down(event): Эта функция изменяет цвет круга на холсте на предыдущий цвет из заданного 
списка (colors) при нажатии клавиши "PgDn" (страница вниз). 
Она также циклически переключается между цветами."""
def change_color_down(event):
    global current_color_index
    current_color_index = (current_color_index - 1) % len(colors)
    canvas.itemconfig(circle, fill=colors[current_color_index])

# Создание окна Tkinter
root = tk.Tk()
root.title("Круг с перемещением и изменением цвета")

# Создание холста
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Начальные координаты центра круга
x, y = 200, 200

# Начальный цвет
colors = ["black", "red", "green", "blue"]
current_color_index = 0

circle = canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS, fill=colors[current_color_index])

# Привязка клавиш к функциям
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)
root.bind("<Prior>", change_color_up)  # PgUp
root.bind("<Next>", change_color_down)  # PgDn
root.bind("<Escape>", lambda event: root.quit())  # Выход по Esc

root.mainloop()
