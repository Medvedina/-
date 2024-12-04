import tkinter as tk
import tkinter.ttk as ttk
from service.service_functions import calc
import errors.errors as er

def mode_calc():
    def calc_notify():
        if float(answer_box.index('end')) >= 12:
            answer_box.delete('1.0', '2.0')
        get = calc_entry.get()
        try:
            answer = calc(get)
            answer_box.insert(tk.END, f"Ответ: {answer}\n")
        except er.BracketError as e:
            answer_box.insert(tk.END, f'Ошибка ввода. Закройте все скобки ({e.__class__.__name__})\n')
        except er.DivZero as e:
            answer_box.insert(tk.END, f'Ошибка. Деление на 0 ({e.__class__.__name__})\n')
        except er.InputError as e:
            answer_box.insert(tk.END, f'Ошибка ввода. Введите выражение аналогично примеру ({e.__class__.__name__})\n')

    calc_entry = tk.Entry(width=50)
    calc_entry.pack(pady=30)
    button = ttk.Button(window, text='Рассчитать', command=calc_notify)
    button.pack(fill=tk.X, padx=[250, 20], pady=10)

    answer_box = tk.Text(window, height=10, width=40)
    answer_box.pack()

window = tk.Tk()
window.geometry("400x400")

Title = tk.Label(text='Турбо-Калькулятор 3000',
                 font=100,
                 foreground='black',
                 background='lightCyan2',
                 height=2)
Title.pack(pady=10)

mode_button_calc = ttk.Button(window, text='Калькулятор', command=mode_calc)
mode_button_calc.place(width=150, height=40, x=30, y=70)

#mode_button_rand = ttk.Button(window, text='Рандомайзер', command=mode_rand)
#mode_button_rand.pack(fill=tk.X, padx=[1, 2], pady=20)

window.mainloop()