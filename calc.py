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
        NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
        OPERATIONS = ['+', '-', '*', '/', '^']
        ACTIONS = []
        FULL_ACTIONS = []
        CURRENT_ACTION = ''
        QUERY = 'Null'
        while(QUERY != 'exit'):
            print('Введите выражение: ')
            QUERY = input()
            if QUERY == 'exit':
                continue
            else:
                for CHAR in QUERY:
                    if CHAR in NUMS:
                        if CHAR != ',':
                            CURRENT_ACTION += CHAR
                        elif CHAR == ',':
                            CURRENT_ACTION += '.'
                    elif CHAR in OPERATIONS or CHAR in '()':
                        if CURRENT_ACTION:
                            ACTIONS.append(CURRENT_ACTION)
                            CURRENT_ACTION = ''
                        ACTIONS.append(CHAR)
                if CURRENT_ACTION:
                    ACTIONS.append(CURRENT_ACTION)
                ACTIONS.insert(0, '(')
                ACTIONS.append(')')
                FULL_ACTIONS = ACTIONS.copy()
                while len(FULL_ACTIONS) != 1:
                    STEP = 0
                    BRACKETFLAG = True
                    while (STEP < len(FULL_ACTIONS)):
                        if BRACKETFLAG:
                            if FULL_ACTIONS[STEP] == ')':
                                STEP_RIGHT = STEP
                                ACTIONS.clear()
                                SUBSTEP = 0
                                while STEP_LEFT + SUBSTEP <= STEP_RIGHT:
                                    ACTIONS.append(FULL_ACTIONS[STEP_LEFT])
                                    del FULL_ACTIONS[STEP_LEFT]
                                    SUBSTEP += 1
                                BRACKETFLAG = False
                                del ACTIONS[0]
                                del ACTIONS[STEP_RIGHT - STEP_LEFT - 1]
                            elif FULL_ACTIONS[STEP] == '(':
                                STEP_LEFT = STEP
                        STEP += 1
                    ACTIONS_COPY = ACTIONS
                    STEP = 0
                    while STEP < len(ACTIONS):
                        if ACTIONS[STEP] == '^':
                            ACTIONS_COPY[STEP - 1] = float(ACTIONS_COPY[STEP - 1]) ** float(ACTIONS_COPY[STEP + 1])
                            del ACTIONS_COPY[STEP]
                            del ACTIONS_COPY[STEP]
                            STEP -= 2
                        STEP += 1
                    STEP = 0
                    ACTIONS = ACTIONS_COPY
                    while STEP < len(ACTIONS):
                        if ACTIONS[STEP] == '*':
                            ACTIONS_COPY[STEP - 1] = float(ACTIONS_COPY[STEP - 1]) * float(ACTIONS_COPY[STEP + 1])
                            del ACTIONS_COPY[STEP]
                            del ACTIONS_COPY[STEP]
                            STEP -= 2
                        elif ACTIONS[STEP] == '/':
                            ACTIONS_COPY[STEP - 1] = float(ACTIONS_COPY[STEP - 1]) * float(ACTIONS_COPY[STEP + 1])
                            del ACTIONS_COPY[STEP]
                            del ACTIONS_COPY[STEP]
                            STEP -= 2
                        STEP += 1
                    STEP = 0
                    ACTIONS = ACTIONS_COPY
                    while STEP < len(ACTIONS):
                        if ACTIONS[STEP] == '+':
                            ACTIONS_COPY[STEP - 1] = float(ACTIONS_COPY[STEP - 1]) + float(ACTIONS_COPY[STEP + 1])
                            del ACTIONS_COPY[STEP]
                            del ACTIONS_COPY[STEP]
                            STEP -= 2
                        elif ACTIONS[STEP] == '-':
                            ACTIONS_COPY[STEP - 1] = float(ACTIONS_COPY[STEP - 1]) - float(ACTIONS_COPY[STEP + 1])
                            del ACTIONS_COPY[STEP]
                            del ACTIONS_COPY[STEP]
                            STEP -= 2
                        STEP += 1
                    FULL_ACTIONS.insert(STEP_LEFT, ACTIONS_COPY[0])
                print(float(FULL_ACTIONS[0]))

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
            X1 = (-B + D ** (0.5)) / A
            X2 = (-B - D ** (0.5)) / A
            print('x1 = ', X1, 'x2 = ', X2)

    elif CHOISE == 3:
        print('Генератор случайных чисел')
        print(
            'Требуется ли исключить какие-либо значения? (список значений через пробел или "Enter", если не требуется)')

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
