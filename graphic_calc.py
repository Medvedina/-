import tkinter as tk
import tkinter.ttk as ttk
from service.service_functions import calc
import errors.errors as er
import os
def main():
    def notify_user(answer_box, answer):
        answer_box.config(state=tk.NORMAL)
        answer_box.insert(tk.END, answer)
        answer_box.config(state=tk.DISABLED)

    def mode_button_menu(*args):
        button_mode_calc.place(width=150, height=40, x=30, y=70)
        button_mode_calc.bind("<KP-1>")
        entry_logs_state.place(x=200, y=300)
        entry_logs_state.insert(index=1, string=f'Размер файла логов: {os.path.getsize("history/logs.txt")}')
        entry_logs_state.config(state=tk.DISABLED)
        button_clear_logs.place(width=70, height=30, x=30, y=300)

        for i in args:
            i.destroy()


    def mode_calc():
        button_mode_calc.place_forget()
        button_clear_logs.place_forget()
        entry_logs_state.place_forget()

        def key_pressed(event):
            calculate()

        def calculate():
            if float(answer_box.index('end')) >= 10:
                answer_box.config(state=tk.NORMAL)
                answer_box.delete('1.0', '2.0')
                answer_box.config(state=tk.DISABLED)
            get = entry_calc.get()
            try:
                answer = calc(get)
                notify_user(answer_box, f"Ответ: {answer}\n" )
            except er.BracketError as e:
                notify_user(answer_box, f'Ошибка ввода. Закройте все скобки ({e.__class__.__name__})\n')
            except er.DivZero as e:
                notify_user(answer_box, f'Ошибка. Деление на 0 ({e.__class__.__name__})\n')
            except er.InputError as e:
                notify_user(answer_box, f'Ошибка ввода. Введите выражение согласно примеру ({e.__class__.__name__})\n')

        label_calc = tk.Label(text='Введите выражение:',
                         font=20,
                         foreground='black',
                         height=1)
        label_calc.place(x=45, y=65)

        entry_calc = tk.Entry(width=50)
        entry_calc.pack(pady=30)

        button_calc = ttk.Button(window, text='Рассчитать', command=calculate)
        button_calc.pack(fill=tk.X, padx=[250, 20], pady=10)
        entry_calc.bind('<Return>', key_pressed)

        answer_box = tk.Text(window, height=10, width=40, state=tk.DISABLED)
        answer_box.pack()

        button_back = ttk.Button(window, text='Назад', command=lambda: mode_button_menu(button_calc, entry_calc, answer_box, button_back, label_calc), state=tk.NORMAL)
        button_back.place(width=100, height=30, x=30, y=360)


    def clear_logs():
        with open('history/logs.txt', 'w') as f:
            f.close()


    window = tk.Tk()
    window.geometry("400x400")
    window.resizable(width=False, height=False)

    Title = tk.Label(text='Турбо-Калькулятор 3000',
                     font=100,
                     foreground='black',
                     background='lightCyan2',
                     height=2)
    Title.pack(pady=10)

    button_mode_calc = ttk.Button(window, text='Калькулятор', command=mode_calc)
    button_mode_calc.place(width=150, height=40, x=30, y=70)
    button_mode_calc.bind("<KP-1>")

    button_clear_logs = ttk.Button(window, text='Очистить', command=clear_logs)
    button_clear_logs.place(width=70, height=30, x=30, y=300)
    entry_logs_state = ttk.Entry(width=50)
    entry_logs_state.place(x=200, y=300)
    entry_logs_state.insert(index=1, string=f'Размер файла логов: {os.path.getsize("history/logs.txt")}')
    entry_logs_state.config(state=tk.DISABLED)
    #mode_button_rand = ttk.Button(window, text='Рандомайзер', command=mode_rand)
    #mode_button_rand.pack(fill=tk.X, padx=[1, 2], pady=20)

    window.mainloop()
if __name__ == '__main__':
    main()