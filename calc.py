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
                    notify_user('Ошибка ввода. Закройте все скобки')
                    query = 'exit'
                    continue
                #except er.DivZero(ZeroDivisionError) as e:
                    #pass
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
                        result = rand(rand_range, ban_list)
                        notify_user(f'\nЧисло: {result}')
                    else:
                        break
                else:
                    break
if __name__ == '__main__':
    main()
