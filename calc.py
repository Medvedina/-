def main():
    print('***Турбо-калькулятор 3000***\n')

    from service.service_functions import mode_check, calc, rand

    while True:
        print('Выберите режим:')
        print('0 - выйти')
        print('1 - калькулятор')
        print('2 - генератор случайных чисел')

        choise = input()


        if mode_check(choise) is False and choise != '0':
            print('Нет такого режима\n')
            continue

        elif mode_check(choise) == 0:
            print('Завершение работы')
            break

        elif mode_check(choise) == 1:
            print('Калькулятор')
            print('Введите выражение, (например: (13 + 2 * 3 / (32 + 5) + 2 ^ 5) '
                  'или exit для выхода)')
            query = input()
            while query != 'exit':
                result = str(calc(query))
                print('Ответ:', result)
                query = input()

        elif mode_check(choise) == 2:
            print('Генератор случайных чисел')
            while True:
                print('\nВведите диапазон генерируемого числа через '
                      'пробел (1 100)    exit - выход')
                rand_range = input()
                if rand_range != 'exit':
                    print('Введите значения, которых генератор должен избегать, (2 31 3), '
                          'Если таких значений нет, нажмите Enter     exit - выход')
                    ban_list = input()
                    if ban_list != 'exit':
                        result = rand(rand_range, ban_list)
                        print('\n---- Число:', result)
                    else:
                        break
                else:
                    break
if __name__ == '__main__':
    main()
