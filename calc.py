from math import pow, sqrt
from random import randint

EXITFLAG = False
print('Турбо-калькулятор 3000')

while not EXITFLAG:
    print('Выберите режим:')
    print('0 - выйти')
    print('1 - калькулятор')
    print('2 - решение квадратных уравнений')
    print('3 - генератор случайных чисел')

    CHOISE = int(input())

    if CHOISE == 1:
        print('Калькулятор')
        print('Введите выражение, разделяя каждый символ пробелом.'
              ' Например: 27 + (9 * 6 - 25) + 72 : 8')
        print('Приоритеты выполнения: Степень ^; Умножение */ Деление : '
              'или /; Сложение +/Вычитание -')

        QUERY = input()
        CORRECTED_QUERY = QUERY.replace(',', '.').split()  # Исправление , на . в дробных числах

        ACTIONS = []  # Список действий
        ARG = []  # Список аргументов
        HIPRIORITY = []  # Список из срезов со скобками
        HIPRIORITYACTIONS = []  # Список действий в скобках
        HIPRIORITYARG = []  # Список аргументов в скобках
        HIPRIORITYINDEX = []  # Список индексов переменных в скобках
        HIPRIOR = False

        for I in CORRECTED_QUERY:  # Составление списков действий в скобках и без них
            if I.startswith('('):
                HIPRIOR = True
            if I == '+':
                if HIPRIOR:
                    HIPRIORITYACTIONS.append('+')
                else:
                    ACTIONS.append('+')
            elif I == '-':
                if HIPRIOR:
                    HIPRIORITYACTIONS.append('-')
                else:
                    ACTIONS.append('-')
            elif I in ('/', ':'):
                if HIPRIOR:
                    HIPRIORITYACTIONS.append('/')
                else:
                    ACTIONS.append('/')
            elif I == '*':
                if HIPRIOR:
                    HIPRIORITYACTIONS.append('*')
                else:
                    ACTIONS.append('*')
            elif I == '^':
                if HIPRIOR:
                    HIPRIORITYACTIONS.append('^')
                else:
                    ACTIONS.append('^')
            elif I.endswith(')'):
                HIPRIORITY.append(I)
                HIPRIORITYACTIONS.append('end')
                HIPRIOR = False
            if HIPRIOR:
                HIPRIORITY.append(I)

        HIPRIORITYARGFLAG = False
        for I in CORRECTED_QUERY:  # Определение чисел, внесение их в список
            if I.isnumeric() and not HIPRIORITYARGFLAG:
                ARG.append(float(I))
            elif I.isnumeric() and HIPRIORITYARGFLAG:
                HIPRIORITYARG.append(float(I))
                ARG.append(float(I))
            elif I.startswith('('):
                HIPRIORITYARG.append(float(I[1:]))
                ARG.append(float(I[1:]))
                HIPRIORITYINDEX.append(
                    len(ARG) - 1)  # Внесение индексов приоритетных действий для замены переменных в списке аргументов ARG
                HIPRIORITYARGFLAG = True
            elif I.endswith(')'):
                HIPRIORITYARG.append(float(I[:-1]))
                ARG.append(float(I[:-1]))
                HIPRIORITYINDEX.append(len(ARG) - 1)
                HIPRIORITYARGFLAG = False
                continue

        while '^' in HIPRIORITYACTIONS:  # Выполнение возведений в степень (скобки)
            for I in HIPRIORITYACTIONS:
                if I == '^':
                    IND = HIPRIORITYACTIONS.index(I)
                    HALFRES = HIPRIORITYARG[IND:IND + 2]
                    B = pow(HALFRES[0], HALFRES[1])
                    HIPRIORITYARG.pop(IND + 1)
                    HIPRIORITYARG[IND] = B
                    HIPRIORITYACTIONS.pop(HIPRIORITYACTIONS.index(I))  # Замена 2 чисел на результат действия. Аналогично во всех действиях (скобки)

        while '*' in HIPRIORITYACTIONS or '/' in HIPRIORITYACTIONS:  # Выполнение умножений и делений (скобки)
            for I in HIPRIORITYACTIONS:
                if I == '*':
                    IND = HIPRIORITYACTIONS.index(I)
                    HALFRES = HIPRIORITYARG[IND:IND + 2]
                    B = HALFRES[0] * HALFRES[1]
                    HIPRIORITYARG.pop(IND + 1)
                    HIPRIORITYARG[IND] = B
                    HIPRIORITYACTIONS.pop(HIPRIORITYACTIONS.index(I))
                elif I == '/':
                    IND = HIPRIORITYACTIONS.index(I)
                    HALFRES = HIPRIORITYARG[IND:IND + 2]
                    B = HALFRES[0] / HALFRES[1]
                    HIPRIORITYARG.pop(IND + 1)
                    HIPRIORITYARG[IND] = B
                    HIPRIORITYACTIONS.pop(HIPRIORITYACTIONS.index(I))

        while '+' in HIPRIORITYACTIONS or '-' in HIPRIORITYACTIONS:  # Выполнения сложений, вычитаний (скобки)
            for I in HIPRIORITYACTIONS:
                if I == '+':
                    IND = HIPRIORITYACTIONS.index(I)
                    HALFRES = HIPRIORITYARG[IND:IND + 2]
                    B = HALFRES[0] + HALFRES[1]
                    HIPRIORITYARG.pop(IND + 1)
                    HIPRIORITYARG[IND] = B
                    HIPRIORITYACTIONS.pop(HIPRIORITYACTIONS.index(I))
                elif I == '-':
                    IND = HIPRIORITYACTIONS.index(I)
                    HALFRES = HIPRIORITYARG[IND:IND + 2]
                    B = HALFRES[0] - HALFRES[1]
                    HIPRIORITYARG.pop(IND + 1)
                    HIPRIORITYARG[IND] = B
                    HIPRIORITYACTIONS.pop(HIPRIORITYACTIONS.index(I))

        DELCOUNTER = 0
        DELCOUNTER1 = 0
        for J in range(len(HIPRIORITYARG)):  # Замена аргументов основного списка на результаты действий в скобках с удалением лишних
            CHANGEFLAG = False
            for I in range(2):
                if CHANGEFLAG:
                    DELCOUNTER += len(ARG[int(HIPRIORITYINDEX[0]) + 1:int(HIPRIORITYINDEX[1] + 1)])
                    del ARG[int(HIPRIORITYINDEX[0] - DELCOUNTER1) + 1:int(HIPRIORITYINDEX[1] + 1 - DELCOUNTER1)]
                    DELCOUNTER1 = DELCOUNTER
                    HIPRIORITYINDEX.pop(0)
                    HIPRIORITYINDEX.pop(0)
                    HIPRIORITYARG.pop(0)
                else:
                    ARG[int(HIPRIORITYINDEX[0]) - DELCOUNTER] = HIPRIORITYARG[0]
                    CHANGEFLAG = True

        while '^' in ACTIONS:  # Выполнение возведений в степень
            for I in ACTIONS:
                if I == '^':
                    IND = ACTIONS.index(I)
                    HALFRES = ARG[IND:IND + 2]
                    B = pow(HALFRES[0], HALFRES[1])
                    ARG.pop(IND + 1)
                    ARG[IND] = B
                    ACTIONS.pop(ACTIONS.index(I))  # Замена 2 чисел на результат действия. Аналогично во всех действиях

        while '*' in ACTIONS or '/' in ACTIONS:  # Выполнение умножений и делений
            for I in ACTIONS:
                if I == '*':
                    IND = ACTIONS.index(I)
                    HALFRES = ARG[IND:IND + 2]
                    B = HALFRES[0] * HALFRES[1]
                    ARG.pop(IND + 1)
                    ARG[IND] = B
                    ACTIONS.pop(ACTIONS.index(I))
                elif I == '/':
                    IND = ACTIONS.index(I)
                    HALFRES = ARG[IND:IND + 2]
                    B = HALFRES[0] / HALFRES[1]
                    ARG.pop(IND + 1)
                    ARG[IND] = B
                    ACTIONS.pop(ACTIONS.index(I))

        while '+' in ACTIONS or '-' in ACTIONS:  # Выполнения сложений, вычитаний
            for I in ACTIONS:
                if I == '+':
                    IND = ACTIONS.index(I)
                    HALFRES = ARG[IND:IND + 2]
                    B = HALFRES[0] + HALFRES[1]
                    ARG.pop(IND + 1)
                    ARG[IND] = B
                    ACTIONS.pop(ACTIONS.index(I))
                elif I == '-':
                    IND = ACTIONS.index(I)
                    HALFRES = ARG[IND:IND + 2]
                    B = HALFRES[0] - HALFRES[1]
                    ARG.pop(IND + 1)
                    ARG[IND] = B
                    ACTIONS.pop(ACTIONS.index(I))

        print('Ответ: ', float(ARG[0]))

    elif CHOISE == 2:
        print('Решение квадратных уравнений')
        print('Введите квадратное уравнение по форме a * x ^ 2 + b * x + c')

        FUNC = input()
        FUNCFORARG = FUNC.split()
        ARG = []
        FLAG = 0  # Введение флага для работы как ввода вида "X^2", так и "x ^ 2"
        MINUS = False

        for I in FUNCFORARG:  # Определение к-тов a, b и c, внесение их в список
            if I == '-':
                MINUS = True
            if I.isnumeric():
                if MINUS:
                    ARG.append(float('-' + I))
                    MINUS = False
                else:
                    if FLAG == '^':
                        continue
                    else:
                        ARG.append(float(I))
            else:
                FLAG = I
                continue

        A, B, C = ARG
        D = (pow(B, 2)) - (4 * A * C)

        if D < 0:  # Решение уравнения
            print('Действительных решений нет =(')
        elif D == 0:
            X = (-B / A)
            print('x1,x2 = ', X)
        else:
            X1 = (-B + sqrt(D)) / A
            X2 = (-B - sqrt(D)) / A
            print('x1 = ', X1, 'x2 = ', X2)

    elif CHOISE == 3:
        print('Генератор случайных чисел')
        print('Требуется ли исключить какие-либо значения? (список значений через пробел или "Enter", если не требуется)')

        BAN = input().split()
        print('Введите диапазон значений (1 100)')

        RANDRANGE = input().split()
        print('Случайное число в промежутке от', RANDRANGE[0], 'до', RANDRANGE[1] + ':')

        while True:
            RES = randint(int(RANDRANGE[0]), int(RANDRANGE[1]))
            if str(RES) not in BAN:
                break

        print(RES)
    elif CHOISE == 0:
        break
