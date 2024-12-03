def main():
    from service.service_functions import calc, mode_check, rand, notify_user
    import errors.errors as er

    notify_user('***Турбо-калькулятор 3000***\n')

    while True:
        notify_user('Выберите режим:')
        notify_user('0 - выйти')
        notify_user('1 - калькулятор')
        notify_user('2 - генератор случайных чисел')

        choice = input()


        if mode_check(choice) is False and choice != '0':
            notify_user('Нет такого режима\n')
            continue

        elif mode_check(choice) == 0:
            notify_user('Завершение работы')
            break

        elif mode_check(choice) == 1:
            notify_user('Калькулятор')
            notify_user('Введите выражение, (например: (13 + 2 * 3 / (32 + 5) + 2 ^ 5) '
                  'или exit для выхода)')
            query = input()
            while query != 'exit':
                try:
                    result = str(calc(query))
                    notify_user(f'Ответ: {result}')
                except er.BracketError as e:
                    notify_user(f'Ошибка ввода. Закройте все скобки ({e.__class__.__name__})')
                    query = input()
                    continue
                except er.DivZero as e:
                    notify_user(f'Ошибка. Деление на 0 ({e.__class__.__name__})')
                except er.InputError as e:
                    notify_user(f'Ошибка ввода. Введите выражение аналогично примеру'
                                     f'({e.__class__.__name__})')
                query = input()

        elif mode_check(choice) == 2:
            notify_user('Генератор случайных чисел')
            while True:
                notify_user('\nВведите диапазон генерируемого числа через '
                      'пробел (1 100)    exit - выход')
                rand_range = input()
                if rand_range != 'exit':
                    notify_user('Введите значения, которых генератор должен избегать, (2 31 3), '
                          'Если таких значений нет, нажмите Enter     exit - выход')
                    ban_list = input()
                    if ban_list != 'exit':
                        try:
                            result = rand(rand_range, ban_list)
                            notify_user(f'\nЧисло: {result}')
                        except er.RangeError as e:
                            notify_user(f'Ошибка ввода(введено больше двух чисел). '
                                        f'Введите диапазон согласно примеру. ({e.__class__.__name__})')
                        except er.InvalidNumberError as e:
                            notify_user(f'Ошибка ввода(получены не числовые значения).'
                                        f'Введите диапазон согласно примеру. ({e.__class__.__name__})')
                        except er.BanListRangeError as e:
                            notify_user(f'Ошибка ввода(избегаемые числа). Введите диапазон согласно примеру. ({e.__class__.__name__})')
                        except er.InputError as e:
                            notify_user(f'Ошибка ввода. Получен пустой диапазон. ({e.__class__.__name__})')
                        except er.BanListError as e:
                            notify_user(f'Ошибка ввода. Запрещены все значения. ({e.__class__.__name__})')
                    else:
                        break
                else:
                    break
if __name__ == '__main__':
    main()
