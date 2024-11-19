#Турбо калькулятор
from math import *
import math
exitflag = False
print('Турбо-калькулятор 3000')
while exitflag == False:
    print('Выберите режим:')
    print('0 - выйти')
    print('1 - калькулятор')
    print('2 - решение квадратных уравнений')
    choise = int(input())
    if choise == 1:
        print('Калькулятор')
        print('Введите выражение, разделяя каждый символ пробелом. Например: 27 + (9 * 6 - 25) + 72 : 8')
        print('Приоритеты выполнения: Степень ^; Умножение */ Деление : или /; Сложение +/Вычитание -')
        query = input()
        corrected_query = query.replace(',', '.').split()   #Исправление , на . в дробных числах
        actions = []                             #Список действий
        arg = []                                 #Список аргументов
        hipriority = []                          #Список из срезов со скобками
        hipriorityactions = []                   #Список действий в скобках
        hipriorityarg = []                       #Список аргументов в скобках
        hipriorityindex = []                     #Список индексов переменных в скобках
        hiprior = False
        for i in corrected_query:                           #Составление списков действий в скобках и без них
            if i.startswith('(') == True:
                hiprior = True
            if i == '+':
                if hiprior == True:
                    hipriorityactions.append('+')
                else:
                    actions.append('+')
            elif i == '-':
                if hiprior == True:
                    hipriorityactions.append('-')
                else:
                    actions.append('-')
            elif i == '/' or i == ':':
                if hiprior == True:
                    hipriorityactions.append('/')
                else:
                    actions.append('/')
            elif i == '*':
                if hiprior == True:
                    hipriorityactions.append('*')
                else:
                    actions.append('*')
            elif i == '^':
                if hiprior == True:
                    hipriorityactions.append('^')
                else:
                    actions.append('^')
            elif i.endswith(')') == True:
                hipriority.append(i)
                hipriorityactions.append('end')
                hiprior = False
            if hiprior == True:
                hipriority.append(i)

        hipriorityargflag = False
        for i in corrected_query:                                         #Определение чисел, внесение их в список
            if i.isnumeric() == True and hipriorityargflag == False:
                arg.append(float(i))
            elif i.isnumeric() == True and hipriorityargflag == True:
                hipriorityarg.append(float(i))
                arg.append(float(i))
            elif i.startswith('(') == True:
                hipriorityarg.append(float(i[1:]))
                arg.append(float(i[1:]))
                hipriorityindex.append(len(arg)-1)                        #Внесение индексов приоритетных действий для замены переменных в списке аргументов arg
                hipriorityargflag = True
            elif i.endswith(')') == True:
                hipriorityarg.append(float(i[:-1]))
                arg.append(float(i[:-1]))
                hipriorityindex.append(len(arg)-1)
                hipriorityargflag = False
                continue

        while ('^' in hipriorityactions):                                                                     # Выполнение возведений в степень (скобки)
            for i in hipriorityactions:
                if i == '^':
                    ind = hipriorityactions.index(i)
                    halfres = hipriorityarg[ind:ind + 2]
                    b = math.pow(halfres[0], halfres[1])
                    hipriorityarg.pop(ind + 1)
                    hipriorityarg[ind] = b
                    hipriorityactions.pop(hipriorityactions.index(i))                                        # Замена 2ух чисел на результат действия. Аналогично во всех действиях (скобки)
        while ('*' in hipriorityactions or '/' in hipriorityactions):                                        # Выполнение умножений и делений (скобки)
            for i in hipriorityactions:
                if i == '*':
                    ind = hipriorityactions.index(i)
                    halfres = hipriorityarg[ind:ind + 2]
                    b = halfres[0] * halfres[1]
                    hipriorityarg.pop(ind + 1)
                    hipriorityarg[ind] = b
                    hipriorityactions.pop(hipriorityactions.index(i))
                elif i == '/':
                    ind = hipriorityactions.index(i)
                    halfres = hipriorityarg[ind:ind + 2]
                    b = halfres[0] / halfres[1]
                    hipriorityarg.pop(ind + 1)
                    hipriorityarg[ind] = b
                    hipriorityactions.pop(hipriorityactions.index(i))
        while ('+' in hipriorityactions or '-' in hipriorityactions):                        # Выполнения сложений, вычитаний (скобки)
            for i in hipriorityactions:
                if i == '+':
                    ind = hipriorityactions.index(i)
                    halfres = hipriorityarg[ind:ind + 2]
                    b = halfres[0] + halfres[1]
                    hipriorityarg.pop(ind + 1)
                    hipriorityarg[ind] = b
                    hipriorityactions.pop(hipriorityactions.index(i))
                elif i == '-':
                    ind = hipriorityactions.index(i)
                    halfres = hipriorityarg[ind:ind + 2]
                    b = halfres[0] - halfres[1]
                    hipriorityarg.pop(ind + 1)
                    hipriorityarg[ind] = b
                    hipriorityactions.pop(hipriorityactions.index(i))
        delcounter = 0
        delcounter1 = 0
        for j in range(len(hipriorityarg)):                                 #Замена аргументов основного списка на результаты действий в скобках с удалением лишних
            changeflag = False
            for i in range(0, 2):
                if changeflag == True:
                    delcounter += len(arg[int(hipriorityindex[0]) + 1:int(hipriorityindex[1]+1)])
                    del arg[int(hipriorityindex[0] - delcounter1) + 1:int(hipriorityindex[1]+1 - delcounter1)]
                    delcounter1 = delcounter
                    hipriorityindex.pop(0)
                    hipriorityindex.pop(0)
                    hipriorityarg.pop(0)
                else:
                    arg[int(hipriorityindex[0])-delcounter] = hipriorityarg[0]
                    changeflag = True
        while('^' in actions):                                                   #Выполнение возведений в степень
            for i in actions:
                if i == '^':
                    ind = actions.index(i)
                    halfres = arg[ind:ind+2]
                    b = math.pow(halfres[0], halfres[1])
                    arg.pop(ind+1)
                    arg[ind] = b
                    actions.pop(actions.index(i))                               #Замена 2ух чисел на результат действия. Аналогично во всех действиях
        while('*' in actions or '/' in actions):                                #Выполнение умножений и делений
            for i in actions:
                if i == '*':
                    ind = actions.index(i)
                    halfres = arg[ind:ind + 2]
                    b = halfres[0] * halfres[1]
                    arg.pop(ind + 1)
                    arg[ind] = b
                    actions.pop(actions.index(i))
                elif i == '/':
                    ind = actions.index(i)
                    halfres = arg[ind:ind + 2]
                    b = halfres[0] / halfres[1]
                    arg.pop(ind + 1)
                    arg[ind] = b
                    actions.pop(actions.index(i))
        while('+' in actions or '-' in actions):                                #Выполнения сложений, вычитаний
            for i in actions:
                if i == '+':
                    ind = actions.index(i)
                    halfres = arg[ind:ind + 2]
                    b = halfres[0] + halfres[1]
                    arg.pop(ind + 1)
                    arg[ind] = b
                    actions.pop(actions.index(i))
                elif i == '-':
                    ind = actions.index(i)
                    halfres = arg[ind:ind + 2]
                    b = halfres[0] - halfres[1]
                    arg.pop(ind + 1)
                    arg[ind] = b
                    actions.pop(actions.index(i))
        print('Ответ: ', float(arg[0]))
    elif choise == 2:
        print('Решение квадратных уравнений')
        print('Введите квадратное урванение по форме a * x ^ 2 + b * x + c')
        func = input()
        funcforarg = func.split()
        arg = []
        flag = 0                                        #Введение флага для работы как ввода вида "X^2", так и "x ^ 2"
        minus = False
        for i in funcforarg:                            #Определение к-тов a, b и c, внесение их в список
            if i == '-':
                minus = True
            if i.isnumeric() == True:
                if minus == True:
                    arg.append(float('-'+i))
                    minus = False
                else:
                    if flag == '^':
                        continue
                    else:
                        arg.append(float(i))
            else:
                flag = i
                continue
        a, b, c = arg
        d = float()
        d = (math.pow(b, 2)) - (4*a*c)
        if d < 0:                                       #Решение уравнения
            print('Действительных решений нет =(')
        elif d == 0:
            x = (-b/a)
            print('x1,x2 = ', x)
        else:
            x1 = (-b + math.sqrt(d)) / a
            x2 = (-b - math.sqrt(d)) / a
            print('x1 = ', x1, 'x2 = ', x2)
    elif choise == 0:
        break