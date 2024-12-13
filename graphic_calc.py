import tkinter as tk
import tkinter.ttk as ttk
from service.service_functions import *
import errors.errors as er
import os


def main():
    def mode_change():
        button_mode_rand.place_forget()
        button_mode_calc.place_forget()
        button_clear_logs.place_forget()
        entry_logs_state.place_forget()
        logs_clear_success.place_forget()

    def notify_user(answer_box, answer):
        answer_box.config(state=tk.NORMAL)
        answer_box.insert(1.0, answer)
        answer_box.config(state=tk.DISABLED)

    def update_logs_size():
        entry_logs_state.config(state=tk.NORMAL)
        entry_logs_state.delete(0, 'end')
        entry_logs_state.insert(0, f'Размер файла логов: {(os.path.getsize("history/logs.txt") / 8 / 1024).__round__(3)} Кбайт')
        entry_logs_state.config(state=tk.DISABLED)

    def mode_button_menu(*args):
        button_mode_calc.place(width=150, height=40, x=30, y=90)
        button_mode_rand.place(width=150, height=40, x=210, y=90)
        button_clear_logs.place(width=70, height=30, x=30, y=300)
        entry_logs_state.place(x=200, y=300)
        update_logs_size()

        for i in args:
            i.destroy()

    def mode_rand():
        mode_change()

        def checkbox_function():
            if not checkbox_flag.get():
                entry_ban.delete(0, 'end')
                entry_ban.config(state=tk.DISABLED)
            else:
                entry_ban.config(state=tk.NORMAL)

        def key_pressed_rand(event):
            randomize()

        def randomize():
            if float(answer_box.index('end')) >= 8:
                answer_box.config(state=tk.NORMAL)
                answer_box.delete('7.0', '8.0')
                answer_box.config(state=tk.DISABLED)
            try:
                result = rand(entry_start.get(), entry_finish.get(), entry_ban.get())
                notify_user(answer_box, f'Число: {result}\n')
            except er.RangeError as e:
                notify_user(answer_box, 'Ошибка ввода(введено больше двух чисел). '
                                        f'Введите диапазон согласно примеру. ({e.__class__.__name__})\n')
            except er.InvalidNumberError as e:
                notify_user(answer_box, 'Ошибка ввода(получены не числовые значения).'
                                        f'Введите диапазон согласно примеру. ({e.__class__.__name__})\n')
            except er.BanListRangeError as e:
                notify_user(answer_box, 'Ошибка ввода(избегаемые числа). '
                                        f'Введите диапазон согласно примеру. ({e.__class__.__name__})\n')
            except er.InputError as e:
                notify_user(answer_box, f'Ошибка ввода. Получен пустой диапазон. ({e.__class__.__name__})\n')
            except er.BanListError as e:
                notify_user(answer_box, f'Ошибка ввода. Запрещены все значения. ({e.__class__.__name__})\n')

        label_start = tk.Label(text='Начало диапазона:', font=20, foreground='black', height=1)
        label_start.place(x=30, y=25)

        label_finish = tk.Label(text='Конец диапазона:', font=20, foreground='black', height=1)
        label_finish.place(x=230, y=25)

        label_ban = tk.Label(text='Запрещенные значения (через пробел):', font=20, foreground='black', height=1)
        label_ban.place(x=30, y=95)

        label_answer = tk.Label(text='Ответы:', font=20, foreground='black', height=1)
        label_answer.place(x=30, y=155)

        entry_start = tk.Entry(width=20)
        entry_start.place(x=30, y=60)
        entry_start.bind('<Return>', key_pressed_rand)

        entry_finish = tk.Entry(width=20)
        entry_finish.place(x=230, y=60)
        entry_finish.bind('<Return>', key_pressed_rand)

        entry_ban = tk.Entry(width=53)
        entry_ban.place(x=30, y=125)
        entry_ban.bind('<Return>', key_pressed_rand)

        checkbox_flag = tk.BooleanVar()
        checkbox_ban = tk.Checkbutton(variable=checkbox_flag, command=checkbox_function)
        checkbox_ban.place(x=360, y=125)
        checkbox_ban.select()

        button_rand = ttk.Button(window, text='Сгенерировать', command=randomize)
        button_rand.place(width=100, height=30, x=250, y=360)

        answer_box = tk.Text(window, height=8, width=40, state=tk.DISABLED)
        answer_box.place(x=30, y=180)

        button_back = ttk.Button(window, text='Назад',
                                 command=lambda: mode_button_menu(button_rand, entry_start, answer_box, button_back,
                                                                  label_start, label_answer, checkbox_ban, entry_ban,
                                                                  label_ban, entry_finish, label_finish),
                                 state=tk.NORMAL)
        button_back.place(width=100, height=30, x=30, y=360)

    def mode_calc():
        mode_change()

        def key_pressed_calc(event):
            calculate()

        def calculate():
            if float(answer_box.index('end')) >= 10:
                answer_box.config(state=tk.NORMAL)
                answer_box.delete('9.0', '10.0')
                answer_box.config(state=tk.DISABLED)
            get = entry_calc.get()

            try:
                answer = calc(get)
                notify_user(answer_box, f"Ответ: {answer}\n")
            except er.BracketError as e:
                notify_user(answer_box, f'Ошибка ввода. Закройте все скобки ({e.__class__.__name__})\n')
            except er.DivZero as e:
                notify_user(answer_box, f'Ошибка. Деление на 0 ({e.__class__.__name__})\n')
            except er.InputError as e:
                notify_user(answer_box, f'Ошибка ввода. Введите выражение согласно примеру ({e.__class__.__name__})\n')

        label_calc = tk.Label(text='Введите выражение:', font=('Arial', 10, 'bold'), foreground='black', height=1)
        label_calc.place(x=30, y=25)

        label_answer = tk.Label(text='Ответы:', font=('Arial', 10, 'bold'), foreground='black', height=1)
        label_answer.place(x=30, y=135)

        label_example = tk.Label(text='Пример: ((((31 * 12) - 15 / 3) + 2 ^ 3) - 5)', font=('Arial', 10), foreground='black', height=1)
        label_example.place(x=30, y=85)

        entry_calc = tk.Entry(width=50)
        entry_calc.place(x=30, y=50)

        button_calc = ttk.Button(window, text='Рассчитать', command=calculate)
        button_calc.place(width=100, height=30, x=250, y=360)
        entry_calc.bind('<Return>', key_pressed_calc)

        answer_box = tk.Text(window, height=10, width=40, state=tk.DISABLED)
        answer_box.place(x=30, y=160)

        button_back = ttk.Button(window, text='Назад',
                                 command=lambda: mode_button_menu(button_calc, entry_calc, answer_box, button_back,
                                                                  label_calc, label_answer, label_example), state=tk.NORMAL)
        button_back.place(width=100, height=30, x=30, y=360)

    def clear_logs(entry_logs_state):
        with open('history/logs.txt', 'w') as f:
            f.close()
        update_logs_size()
        logs_clear_success.place(x=240, y=360)

    window = tk.Tk()
    window.title('Турбо-калькулятор 3000')
    window.geometry("400x400")
    window.resizable(width=False, height=False)

    button_mode_calc = ttk.Button(window, text='Калькулятор', command=mode_calc)
    button_mode_calc.place(width=150, height=40, x=30, y=90)

    button_mode_rand = ttk.Button(window, text='Рандомайзер', command=mode_rand)
    button_mode_rand.place(width=150, height=40, x=210, y=90)

    entry_logs_state = ttk.Entry(width=50)
    entry_logs_state.place(x=200, y=300)
    update_logs_size()

    button_clear_logs = ttk.Button(window, text='Очистить', command=lambda: clear_logs(entry_logs_state))
    button_clear_logs.place(width=70, height=30, x=30, y=300)

    logs_clear_success = ttk.Label(window, text='Очистка выполнена', font=('Arial', 10, 'bold'), foreground='green')

    window.mainloop()


if __name__ == '__main__':
    main()
