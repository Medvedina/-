import customtkinter as ctk
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
        answer_box.configure(state=ctk.NORMAL)
        answer_box.insert(1.0, answer)
        answer_box.configure(state=ctk.DISABLED)

    def update_logs_size():
        entry_logs_state.configure(state=ctk.NORMAL)
        entry_logs_state.delete(0, 'end')
        entry_logs_state.insert(0, f'Размер файла логов: {(os.path.getsize("history/logs.txt") / 8 / 1024).__round__(3)} Кбайт')
        entry_logs_state.configure(state=ctk.DISABLED)

    def mode_button_menu(*args):
        button_mode_calc.place(x=30, y=60)
        button_mode_rand.place(x=210, y=60)
        button_clear_logs.place(x=30, y=300)
        entry_logs_state.place(x=120, y=300)
        update_logs_size()

        for i in args:
            i.destroy()

    def mode_rand():
        mode_change()

        def checkbox_function():
            if not checkbox_flag.get():
                entry_ban.delete(0, 'end')
                entry_ban.configure(state=ctk.DISABLED)
                checkbox_ban.configure(text='Выключено')
            else:
                entry_ban.configure(state=ctk.NORMAL)
                checkbox_ban.configure(text='Включено')

        def key_pressed_rand(event):
            randomize()

        def randomize():
            if float(answer_box.index('end')) >= 8:
                answer_box.configure(state=ctk.NORMAL)
                answer_box.delete('7.0', '8.0')
                answer_box.configure(state=ctk.DISABLED)
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

        label_start = ctk.CTkLabel(window, text='Начало диапазона:', font=('Arial', 12, 'bold'))
        label_start.place(x=30, y=25)

        label_finish = ctk.CTkLabel(window, text='Конец диапазона:', font=('Arial', 12, 'bold'))
        label_finish.place(x=230, y=25)

        label_ban = ctk.CTkLabel(window, text='Запрещенные значения (через пробел):', font=('Arial', 12, 'bold'))
        label_ban.place(x=30, y=95)

        label_answer = ctk.CTkLabel(window, text='Ответы:', font=('Arial', 12, 'bold'))
        label_answer.place(x=30, y=180)

        entry_start = ctk.CTkEntry(window, width=100)
        entry_start.place(x=30, y=60)
        entry_start.bind('<Return>', key_pressed_rand)

        entry_finish = ctk.CTkEntry(window, width=100)
        entry_finish.place(x=230, y=60)
        entry_finish.bind('<Return>', key_pressed_rand)

        entry_ban = ctk.CTkEntry(window, width=300)
        entry_ban.place(x=30, y=125)
        entry_ban.bind('<Return>', key_pressed_rand)

        checkbox_flag = ctk.BooleanVar()
        checkbox_ban = ctk.CTkCheckBox(window, text='Включено', variable=checkbox_flag, command=checkbox_function)
        checkbox_ban.place(x=250, y=175)
        checkbox_ban.select()

        button_rand = ctk.CTkButton(window, width=100, height=30, text='Сгенерировать', command=randomize)
        button_rand.place(x=250, y=360)

        answer_box = ctk.CTkTextbox(window, height=100, width=300)
        answer_box.place(x=30, y=220)

        button_back = ctk.CTkButton(window, text='Назад', width=100, height=30,
                                     command=lambda: mode_button_menu(button_rand, entry_start, answer_box, button_back,
                                                                      label_start, label_answer, checkbox_ban, entry_ban,
                                                                      label_ban, entry_finish, label_finish))
        button_back.place(x=30, y=360)

    def mode_calc():
        mode_change()

        def key_pressed_calc(event):
            calculate()

        def calculate():
            if float(answer_box.index('end')) >= 10:
                answer_box.configure(state=ctk.NORMAL)
                answer_box.delete('10.0', '11.0')
                answer_box.configure(state=ctk.DISABLED)

            try:
                answer = calc(entry_calc.get())
                notify_user(answer_box, f"Ответ: {answer}\n")
            except er.BracketError as e:
                notify_user(answer_box, f'Ошибка ввода. Закройте все скобки ({e.__class__.__name__})\n')
            except er.DivZero as e:
                notify_user(answer_box, f'Ошибка. Деление на 0 ({e.__class__.__name__})\n')
            except er.InputError as e:
                notify_user(answer_box, f'Ошибка ввода. Введите выражение согласно примеру ({e.__class__.__name__})\n')
            except IndexError as e:
                notify_user(answer_box, f'Ошибка ввода. Введите выражение согласно примеру. ({e.__class__.__name__})\n')

        label_calc = ctk.CTkLabel(window, text='Введите выражение:', font=('Arial', 12, 'bold'))
        label_calc.place(x=30, y=25)

        label_answer = ctk.CTkLabel(window, text='Ответы:', font=('Arial', 12, 'bold'))
        label_answer.place(x=30, y=135)

        label_example = ctk.CTkLabel(window, text='Пример: ((((31 * 12) - 15 / 3) + 2 ^ 3) - 5)', font=('Arial', 12, 'bold'))
        label_example.place(x=30, y=85)

        entry_calc = ctk.CTkEntry(window, width=340)
        entry_calc.place(x=30, y=50)

        button_calc = ctk.CTkButton(window, width=100, height=30, text='Рассчитать', command=calculate)
        button_calc.place(x=250, y=360)
        entry_calc.bind('<Return>', key_pressed_calc)

        answer_box = ctk.CTkTextbox(window, height=170, width=340)
        answer_box.place(x=30, y=160)

        button_back = ctk.CTkButton(window, width=100, height=30, text='Назад',
                                     command=lambda: mode_button_menu(button_calc, entry_calc, answer_box, button_back,
                                                                      label_calc, label_answer, label_example))
        button_back.place(x=30, y=360)

    def clear_logs(entry_logs_state):
        with open('history/logs.txt', 'w') as f:
            f.close()
        update_logs_size()
        logs_clear_success.place(x=240, y=360)

    window = ctk.CTk()
    window.title('Турбо-калькулятор 3000')
    window.geometry("400x400")
    window.resizable(width=False, height=False)

    button_mode_calc = ctk.CTkButton(window, text='Калькулятор', command=mode_calc, width=150, height=40)
    button_mode_calc.place(x=30, y=60)

    button_mode_rand = ctk.CTkButton(window, text='Рандомайзер', command=mode_rand, width=150, height=40)
    button_mode_rand.place(x=210, y=60)

    entry_logs_state = ctk.CTkEntry(window, width=240)
    entry_logs_state.place(x=120, y=300)
    update_logs_size()

    button_clear_logs = ctk.CTkButton(window, text='Очистить', command=lambda: clear_logs(entry_logs_state), width=70, height=30)
    button_clear_logs.place(x=30, y=300)

    logs_clear_success = ctk.CTkLabel(window, text='Очистка выполнена', font=('Arial', 12, 'bold'), text_color='green')

    window.mainloop()

if __name__ == '__main__':
    main()