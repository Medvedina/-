import tkinter as tk
import tkinter.ttk as ttk
from service.service_functions import *

def func():
    get = calc_entry.get()
    answer = calc(get)
    answer_box.insert(tk.END, f"Ответ: {answer}\n")

window = tk.Tk()
window.geometry("400x400")

Title = tk.Label(text='Турбо-Калькулятор 3000',
                 font = 100,
                 foreground='black',
                 background='lightCyan2',
                 height=2)
Title.pack(pady=10)

calc_entry = tk.Entry(width = 50)
calc_entry.pack(pady=30)
button = ttk.Button(window, text='Рассчитать', command=func)
button.pack(fill=tk.X, padx=[250, 20], pady=10)

answer_box = tk.Text(window, height = 10, width = 40)
answer_box.pack()

window.mainloop()