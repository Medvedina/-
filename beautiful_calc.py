import customtkinter as ctk
from service.service_functions import *
import errors.errors as er
import os


def main():
    def mode_change():
        button_mode_rand.place_forget()
        button_mode_calc.place_forget()
        button_mode_ipcalc.place_forget()
        button_mode_numsys.place_forget()
        button_clear_logs.place_forget()
        entry_logs_state.place_forget()
        logs_clear_success.place_forget()
        theme_menu.place_forget()

    def notify_user(answer_box, answer, output_mode='append'):
        answer_box.configure(state=ctk.NORMAL)
        if output_mode == 'append':
            answer_box.insert(1.0, answer)
        elif output_mode == 'write':
            answer_box.delete(1.0, 'end')
            answer_box.insert('end', answer)
        answer_box.configure(state=ctk.DISABLED)

    def update_logs_size():
        entry_logs_state.configure(state=ctk.NORMAL)
        entry_logs_state.delete(0, 'end')
        entry_logs_state.insert(0,
                                f'Размер файла логов: '
                                f'{(os.path.getsize("history/logs.txt") / 8 / 1024).__round__(3)} Кбайт')
        entry_logs_state.configure(state=ctk.DISABLED)

    def mode_button_menu(*args):
        button_mode_calc.place(x=30, y=60)
        button_mode_rand.place(x=210, y=60)
        button_clear_logs.place(x=30, y=300)
        button_mode_ipcalc.place(x=30, y=130)
        button_mode_numsys.place(x=210, y=130)
        entry_logs_state.place(x=120, y=300)
        theme_menu.place(x=240, y=350)
        update_logs_size()

        for i in args:
            i.destroy()

    class ModeRand:
        def __init__(self, window):
            self.window = window
            self.label_answer = None
            self.label_ban = None
            self.label_start = None
            self.label_finish = None
            self.button_rand = None
            self.entry_start = None
            self.entry_finish = None
            self.entry_ban = None
            self.answer_box = None
            self.checkbox_ban = None
            self.button_back = None
            self.checkbox_flag = None

            self.setup_ui()

        def checkbox_function_rand(self):
            if not self.checkbox_flag.get():
                self.entry_ban.delete(0, 'end')
                self.entry_ban.configure(state=ctk.DISABLED)
                self.checkbox_ban.configure(text='Выключено')
            else:
                self.entry_ban.configure(state=ctk.NORMAL)
                self.checkbox_ban.configure(text='Включено')

        def randomize(self):
            if float(self.answer_box.index('end')) >= 8:
                self.answer_box.configure(state=ctk.NORMAL)
                self.answer_box.delete('7.0', '8.0')
                self.answer_box.configure(state=ctk.DISABLED)
            try:
                result = rand(self.entry_start.get(), self.entry_finish.get(), self.entry_ban.get())
                notify_user(self.answer_box, f'Число: {result}\n')
            except er.RangeError as e:
                notify_user(self.answer_box, 'Ошибка ввода(введено больше двух чисел). '
                                             f'Введите диапазон согласно примеру. ({e.__class__.__name__})\n')
            except er.InvalidNumberError as e:
                notify_user(self.answer_box, 'Ошибка ввода(получены не числовые значения).'
                                             f'Введите диапазон согласно примеру. ({e.__class__.__name__})\n')
            except er.BanListRangeError as e:
                notify_user(self.answer_box, 'Ошибка ввода(избегаемые числа). '
                                             f'Введите диапазон согласно примеру. ({e.__class__.__name__})\n')
            except er.InputError as e:
                notify_user(self.answer_box, f'Ошибка ввода. Получен пустой диапазон. ({e.__class__.__name__})\n')
            except er.BanListError as e:
                notify_user(self.answer_box, f'Ошибка ввода. Запрещены все значения. ({e.__class__.__name__})\n')

        def key_pressed_rand(self, event):
            self.randomize()

        def setup_ui(self):
            mode_change()
            self.label_start = ctk.CTkLabel(self.window, text='Начало диапазона:', font=('Arial', 12, 'bold'))
            self.label_start.place(x=30, y=25)

            self.label_finish = ctk.CTkLabel(self.window, text='Конец диапазона:', font=('Arial', 12, 'bold'))
            self.label_finish.place(x=230, y=25)

            self.label_ban = ctk.CTkLabel(self.window, text='Запрещенные значения (через пробел):',
                                          font=('Arial', 12, 'bold'))
            self.label_ban.place(x=30, y=95)

            self.label_answer = ctk.CTkLabel(self.window, text='Ответы:', font=('Arial', 12, 'bold'))
            self.label_answer.place(x=30, y=180)

            self.entry_start = ctk.CTkEntry(self.window, width=100)
            self.entry_start.place(x=30, y=60)
            self.entry_start.bind('<Return>', self.key_pressed_rand)

            self.entry_finish = ctk.CTkEntry(self.window, width=100)
            self.entry_finish.place(x=230, y=60)
            self.entry_finish.bind('<Return>', self.key_pressed_rand)

            self.entry_ban = ctk.CTkEntry(self.window, width=300)
            self.entry_ban.place(x=30, y=125)
            self.entry_ban.bind('<Return>', self.key_pressed_rand)

            self.checkbox_flag = ctk.BooleanVar()
            self.checkbox_ban = ctk.CTkCheckBox(self.window, text='Включено', variable=self.checkbox_flag,
                                                command=self.checkbox_function_rand)
            self.checkbox_ban.place(x=250, y=175)
            self.checkbox_ban.select()

            self.button_rand = ctk.CTkButton(self.window, width=100, height=30, text='Сгенерировать', command=self.randomize)
            self.button_rand.place(x=250, y=360)

            self.answer_box = ctk.CTkTextbox(self.window, height=100, width=300, state=ctk.DISABLED)
            self.answer_box.place(x=30, y=220)

            self.button_back = ctk.CTkButton(self.window, text='Назад', width=100, height=30,
                                             command=lambda: mode_button_menu(self.button_rand, self.entry_start,
                                                                              self.answer_box, self.button_back,
                                                                              self.label_start, self.label_answer,
                                                                              self.checkbox_ban, self.entry_ban,
                                                                              self.label_ban, self.entry_finish,
                                                                              self.label_finish))
            self.button_back.place(x=30, y=360)
            mode_theme_change(self.button_rand, self.button_back, self.checkbox_ban)

    class ModeCalc:
        def __init__(self, window):
            self.label_example = None
            self.label_calc = None
            self.label_answer = None
            self.window = window
            self.entry_calc = None
            self.button_calc = None
            self.button_back = None
            self.answer_box = None

            self.setup_ui()

        def setup_ui(self):
            mode_change()
            self.label_calc = ctk.CTkLabel(self.window, text='Введите выражение:', font=('Arial', 12, 'bold'))
            self.label_calc.place(x=30, y=25)

            self.label_answer = ctk.CTkLabel(self.window, text='Ответы:', font=('Arial', 12, 'bold'))
            self.label_answer.place(x=30, y=135)

            self.label_example = ctk.CTkLabel(self.window, text='Пример: ((((31 * 12) - 15 / 3) + 2 ^ 3) - 5)',
                                              font=('Arial', 12, 'bold'))
            self.label_example.place(x=30, y=85)

            self.entry_calc = ctk.CTkEntry(self.window, width=340)
            self.entry_calc.place(x=30, y=50)

            self.button_calc = ctk.CTkButton(self.window, width=100, height=30, text='Рассчитать',
                                             command=self.calculate)
            self.button_calc.place(x=250, y=360)
            self.entry_calc.bind('<Return>', self.key_pressed_calc)

            self.answer_box = ctk.CTkTextbox(self.window, height=170, width=340, state=ctk.DISABLED)
            self.answer_box.place(x=30, y=160)

            self.button_back = ctk.CTkButton(self.window, width=100, height=30, text='Назад',
                                             command=lambda: mode_button_menu(self.button_calc, self.entry_calc,
                                                                              self.answer_box,
                                                                              self.button_back,
                                                                              self.label_calc, self.label_answer,
                                                                              self.label_example))
            self.button_back.place(x=30, y=360)
            mode_theme_change(self.button_calc, self.button_back)

        def key_pressed_calc(self, event):
            self.calculate()

        def calculate(self):
            if float(self.answer_box.index('end')) >= 10:
                self.answer_box.configure(state=ctk.NORMAL)
                self.answer_box.delete('10.0', '11.0')
                self.answer_box.configure(state=ctk.DISABLED)

            try:
                answer = calc(self.entry_calc.get())
                notify_user(self.answer_box, f"Ответ: {answer}\n")
            except er.BracketError as e:
                notify_user(self.answer_box, f'Ошибка ввода. Закройте все скобки ({e.__class__.__name__})\n')
            except er.DivZero as e:
                notify_user(self.answer_box, f'Ошибка. Деление на 0 ({e.__class__.__name__})\n')
            except er.InputError as e:
                notify_user(self.answer_box,
                            f'Ошибка ввода. Введите выражение согласно примеру ({e.__class__.__name__})\n')
            except IndexError as e:
                notify_user(self.answer_box,
                            f'Ошибка ввода. Введите выражение согласно примеру. ({e.__class__.__name__})\n')

    class ModeIPCalc:
        def __init__(self, window):
            self.entry_mask = None
            self.entry_ip = None
            self.label_mask = None
            self.label_ip = None
            self.label_answer = None
            self.button_ipcalc = None
            self.button_back = None
            self.answer_box = None
            self.mask_menu_var = None
            self.window = window
            self.menu_mask = None

            self.setup_ui()

        def menu_function_ipcalc(self, choice):
            if choice == 'Префикс':
                self.entry_mask.configure(width=30)
                self.label_mask.configure(text='Префикс маски подсети:')
            elif choice == 'Десятичный':
                self.entry_mask.configure(width=140)
                self.label_mask.configure(text='Маска подсети:')

        def key_pressed_ipcalc(self, event):
            self.calculate_ip()

        def calculate_ip(self):
            try:
                result = IP(self.entry_ip.get(), self.entry_mask.get(), self.mask_menu_var.get())
                notify_user(self.answer_box, f'Число: {result}\n', 'write')
            except TypeError as e:
                notify_user(self.answer_box, f'Выберите способ представления маски подсети ({e.__class__.__name__})')
            except ipaddress.NetmaskValueError as e:
                notify_user(self.answer_box, f'Ошибка ввода.(Некорректная маска подсети). ({e.__class__.__name__})\n',
                            'write')
            except ipaddress.AddressValueError as e:
                notify_user(self.answer_box, f'Ошибка ввода.(Некорректный ip-адрес). ({e.__class__.__name__})\n',
                            'write')
            except PrefixError as e:
                notify_user(self.answer_box,
                            f'Ошибка ввода.(Некорректный префикс маски подсети). ({e.__class__.__name__})\n', 'write')

        def setup_ui(self):
            mode_change()
            self.label_ip = ctk.CTkLabel(self.window, text='Ip-адрес:', font=('Arial', 12, 'bold'))
            self.label_ip.place(x=30, y=25)

            self.label_mask = ctk.CTkLabel(self.window, text='Выберите представление', font=('Arial', 12, 'bold'))
            self.label_mask.place(x=230, y=25)

            self.label_answer = ctk.CTkLabel(self.window, text='Рассчёт:', font=('Arial', 12, 'bold'))
            self.label_answer.place(x=30, y=150)

            self.entry_ip = ctk.CTkEntry(self.window, width=170)
            self.entry_ip.place(x=30, y=60)
            self.entry_ip.bind('<Return>', self.key_pressed_ipcalc)

            self.entry_mask = ctk.CTkEntry(self.window, width=100)
            self.entry_mask.place(x=230, y=60)
            self.entry_mask.bind('<Return>', self.key_pressed_ipcalc)

            self.mask_menu_var = ctk.Variable(value='Представление')
            self.menu_mask = ctk.CTkOptionMenu(self.window, values=["Префикс", "Десятичный"],
                                               command=self.menu_function_ipcalc,
                                               variable=self.mask_menu_var)
            self.menu_mask.place(x=250, y=100)

            self.button_ipcalc = ctk.CTkButton(self.window, width=100, height=30, text='Рассчитать',
                                               command=self.calculate_ip)
            self.button_ipcalc.place(x=250, y=360)

            self.answer_box = ctk.CTkTextbox(self.window, height=150, width=366, state=ctk.DISABLED)
            self.answer_box.place(x=17, y=180)

            self.button_back = ctk.CTkButton(self.window, text='Назад', width=100, height=30,
                                             command=lambda: mode_button_menu(self.button_ipcalc, self.entry_ip,
                                                                              self.answer_box, self.button_back,
                                                                              self.label_ip, self.label_answer,
                                                                              self.menu_mask,
                                                                              self.entry_mask, self.label_mask))
            self.button_back.place(x=30, y=360)
            mode_theme_change(self.button_ipcalc, self.button_back, self.menu_mask)
            if ctk.get_appearance_mode() == 'Light':
                self.menu_mask.configure(button_color='#596174')

    class ModeNumSys:
        def __init__(self, window):
            self.window = window
            self.answer_box = None
            self.entry_input = None
            self.label_answer = None
            self.label_numsys = None
            self.menu_numsys = None
            self.menu_mode_var = None

            self.setup_ui()

        def menu_function_numsys(self, choice):
            result = None
            if choice == 'Двоичная':
                result = 'binary'
            elif choice == 'Восьмеричная':
                result = 'octal'
            elif choice == 'Десятичная':
                result = 'decimal'
            elif choice == 'Шестнадцатеричная':
                result = 'hexadecimal'
            return result

        def numsys_do(self):
            try:
                result = numsys(str(self.menu_function_numsys(self.menu_mode_var.get())), self.entry_input.get())
                notify_user(self.answer_box, f'Двоичная форма: {result[0]}\n'
                                        f'Восьмеричная форма: {result[1]}\n'
                                        f'Десятичная форма: {result[2]}\n'
                                        f'Шестнадцатеричная форма: {result[3]}\n', 'write')
            except TypeError as e:
                notify_user(self.answer_box, f'Выберите систему счисления ({e.__class__.__name__})', 'write')
            except InvalidNumberError as e:
                notify_user(self.answer_box,
                            f'Ошибка ввода. Введите корректное для выбранной системы число ({e.__class__.__name__})',
                            'write')

        def key_pressed_numsys(self, event):
            self.numsys_do()

        def setup_ui(self):
            mode_change()
            self.entry_input = ctk.CTkEntry(self.window, width=200)
            self.entry_input.place(x=30, y=40)
            self.entry_input.bind('<Return>', self.key_pressed_numsys)

            self.menu_mode_var = ctk.Variable(value='Система счисления')
            self.menu_numsys = ctk.CTkOptionMenu(self.window, values=["Двоичная", "Восьмеричная", "Десятичная", "Шестнадцатеричная"],
                                            command=self.menu_function_numsys,
                                            variable=self.menu_mode_var)
            self.menu_numsys.place(x=30, y=90)

            self.label_answer = ctk.CTkLabel(self.window, text='Расчёт:', font=('Arial', 12, 'bold'))
            self.label_answer.place(x=30, y=150)

            self.label_numsys = ctk.CTkLabel(self.window, text='Введите число:', font=('Arial', 12, 'bold'))
            self.label_numsys.place(x=30, y=10)

            self.answer_box = ctk.CTkTextbox(self.window, height=150, width=340, state=ctk.DISABLED)
            self.answer_box.place(x=30, y=180)

            self.button_numsys = ctk.CTkButton(self.window, width=100, height=30, text='Рассчитать', command=self.numsys_do)
            self.button_numsys.place(x=250, y=360)

            self.button_back = ctk.CTkButton(window, text='Назад', width=100, height=30,
                                        command=lambda: mode_button_menu(self.entry_input, self.answer_box, self.button_back,
                                                                         self.button_numsys, self.menu_numsys, self.label_numsys,
                                                                         self.label_answer))

            self.button_back.place(x=30, y=360)

            mode_theme_change(self.button_numsys, self.button_back, self.menu_numsys)
            if ctk.get_appearance_mode() == 'Light':
                self.menu_numsys.configure(button_color='#596174')

    def clear_logs():
        with open('history/logs.txt', 'w') as f:
            f.close()
        update_logs_size()
        logs_clear_success.place(x=30, y=360)

    def menu_theme_change(choice):
        def theme_color_change_dark(*args):
            for widget in args:
                widget.configure(fg_color='#3B8ED0')

        def theme_color_change_light(*args):
            for widget in args:
                widget.configure(fg_color='#303A52')

        if choice == 'Тёмная тема':
            theme_menu.configure(button_color='#36719F', fg_color='#3B8ED0')
            ctk.set_appearance_mode("dark")
            theme_color_change_dark(button_mode_rand, button_mode_numsys, button_mode_ipcalc, button_clear_logs,
                                    button_mode_calc)
        elif choice == 'Светлая тема':
            theme_menu.configure(button_color='#596174', fg_color='#303A52')
            ctk.set_appearance_mode("light")
            theme_color_change_light(button_mode_rand, button_mode_numsys, button_mode_ipcalc, button_clear_logs,
                                     button_mode_calc)

    def mode_theme_change(*args):
        if ctk.get_appearance_mode() == 'Light':
            for widget in args:
                widget.configure(fg_color='#303A52')

    ctk.set_appearance_mode("dark")

    window = ctk.CTk()
    window.title('Турбо-калькулятор 3000')
    window.geometry("400x400")
    window.resizable(width=False, height=False)

    theme_menu_var = ctk.StringVar(value="Тёмная тема")
    theme_menu = ctk.CTkOptionMenu(window, values=["Светлая тема", "Тёмная тема"],
                                   command=menu_theme_change,
                                   variable=theme_menu_var)
    theme_menu.place(x=240, y=350)

    button_mode_calc = ctk.CTkButton(window, text='Калькулятор', command=lambda: ModeCalc(window), width=150, height=40)
    button_mode_calc.place(x=30, y=60)

    button_mode_rand = ctk.CTkButton(window, text='Рандомайзер', command=lambda: ModeRand(window), width=150, height=40)
    button_mode_rand.place(x=210, y=60)

    button_mode_ipcalc = ctk.CTkButton(window, text='Калькулятор IP', command=lambda: ModeIPCalc(window), width=150, height=40)
    button_mode_ipcalc.place(x=30, y=130)

    button_mode_numsys = ctk.CTkButton(window, text='Системы счисления', command=lambda: ModeNumSys(window), width=150, height=40)
    button_mode_numsys.place(x=210, y=130)

    entry_logs_state = ctk.CTkEntry(window, width=240)
    entry_logs_state.place(x=120, y=300)
    update_logs_size()

    button_clear_logs = ctk.CTkButton(window, text='Очистить', command=lambda: clear_logs(), width=70,
                                      height=30)
    button_clear_logs.place(x=30, y=300)

    logs_clear_success = ctk.CTkLabel(window, text='Очистка выполнена', font=('Arial', 12, 'bold'), text_color='green')

    window.mainloop()


if __name__ == '__main__':
    main()
