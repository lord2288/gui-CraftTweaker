import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('CraftTweakerGui')

# Создание контейнера для прокрутки
scroll_canvas = tk.Canvas(root)
scroll_canvas.grid(row=0, column=0, sticky='nsew')

# Добавление полосы прокрутки
scrollbar = ttk.Scrollbar(root, orient='vertical', command=scroll_canvas.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
scroll_canvas.configure(yscrollcommand=scrollbar.set)

# Создание фрейма внутри Canvas
frame = ttk.Frame(scroll_canvas)
scroll_canvas.create_window((0, 0), window=frame, anchor='nw')

# Функция для настройки области прокрутки
def configure_scroll_region(event):
    scroll_canvas.configure(scrollregion=scroll_canvas.bbox('all'))

frame.bind('<Configure>', configure_scroll_region)

# Чтение и отображение рецептов из файла
k = 0
with open('recipes.zs') as file:
    for line in file:
        if line[:14] == 'recipes.remove':

        label = tk.Label(frame, text=line)
        label.grid(row=k, column=0, sticky='w')
        k += 1

# Настройка размеров колонок и строк для правильной работы прокрутки
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Функция для прокрутки с помощью колесика мыши
def on_mouse_wheel(event):
    scroll_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Привязка события прокрутки колесика мыши к Canvas
scroll_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

root.mainloop()
