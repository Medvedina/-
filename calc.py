print('***Турбо-калькулятор 3000***\n')

from service.service_functions import mode_check

from history.logs_script import *

while True:
    print('Выберите режим:')
    print('0 - выйти')
    print('1 - калькулятор')
    print('2 - генератор случайных чисел')

    choise = input()

    from history.logs_script import *
    inputlog(choise)

    if not mode_check(choise) and choise != '0':
        print('Нет такого режима\n')
        continue

    elif mode_check(choise) == 0:
        print('Завершение работы')
        inputlog('CLOSED')
        break

    elif mode_check(choise) == 1:
        from service.service_functions import calc
        print('Калькулятор')
        print('Введите выражение, (например: (13 + 2 * 3 / (32 + 5) + 2 ^ 5) '
              'или exit для выхода)')
        query = input()
        while query != 'exit':
            result = str(calc(query))
            print('Ответ:', result)
            outputlog(result)
            query = input()

    elif mode_check(choise) == 2:
        from service.service_functions import rand
        print('Генератор случайных чисел')
        while True:
            print('\nВведите диапазон генерируемого числа через '
                  'пробел (1 100)    exit - выход')
            randrange = input()
            if randrange != 'exit':
                print('Введите значения, которых генератор должен избегать, (2 31 3), '
                      'Если таких значений нет, нажмите Enter     exit - выход')
                banlist = input()
                if banlist != 'exit':
                    result = rand(randrange, banlist)
                    print('\n---- Число:', result)
                    outputlog(str(result))
                else:
                    break
            else:
                break
