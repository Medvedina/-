print('Турбо-калькулятор 3000')

while True:
    print('Выберите режим:')
    print('0 - выйти')
    print('1 - калькулятор')
    print('2 - генератор случайных чисел')

    choise = input()

    if not choise.isnumeric():
        print('Нет такого режима \n')
        continue

    elif int(choise) >= 3:
        print('Нет такого режима \n')
        continue

    choise = int(choise)

    from history.logs_script import *
    inputlog(choise)

    if choise == 0:
        inputlog('CLOSED')
        break

    elif choise == 1:
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

    elif choise == 2:
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
