def calc(query):
    from history.logs_script import inputlog, outputlog

    inputlog(query)

    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
    operations = ['+', '-', '*', '/', '^']
    if query.count('(') != query.count(')'):
        return 'Ошибка ввода. Закройте все скобки.'
    for i in query:
        if (i not in nums and i not in operations and
                i != '(' and i != ')' and i != ' '):
            res = 'Ошибка ввода. Введите выражение аналогично примеру'
            outputlog(res)
            return res
    actions = []
    full_actions = []
    current_action = ''
    while query != 'exit':
        if query == 'exit':
            res = 'Выход'
            outputlog(res)
            return res
        else:
            step_left = 0
            for char in query:
                if char in nums:
                    if char != ',':
                        current_action += char
                    elif char == ',':
                        current_action += '.'
                elif char in operations or char in '()':
                    if current_action:
                        actions.append(current_action)
                        current_action = ''
                    actions.append(char)
            if current_action:
                actions.append(current_action)
            actions.insert(0, '(')
            actions.append(')')
            full_actions = actions.copy()
            while len(full_actions) != 1:
                step = 0
                bracket_flag = True
                while step < len(full_actions):
                    if bracket_flag:
                        if full_actions[step] == ')':
                            step_right = step
                            actions.clear()
                            substep = 0
                            while step_left + substep <= step_right:
                                actions.append(full_actions[step_left])
                                del full_actions[step_left]
                                substep += 1
                            bracket_flag = False
                            del actions[0]
                            del actions[step_right - step_left - 1]
                        elif full_actions[step] == '(':
                            step_left = step
                    step += 1
                actions_copy = actions
                step = 0
                while step < len(actions):
                    if actions[step] == '^':
                        actions_copy[step - 1] = (float(actions_copy[step - 1]) **
                                                  float(actions_copy[step + 1]))
                        del actions_copy[step]
                        del actions_copy[step]
                        step -= 2
                    step += 1
                step = 0
                actions = actions_copy
                while step < len(actions):
                    if actions[step] == '*':
                        actions_copy[step - 1] = (float(actions_copy[step - 1]) *
                                                  float(actions_copy[step + 1]))
                        del actions_copy[step]
                        del actions_copy[step]
                        step -= 2
                    elif actions[step] == '/':
                        if float(actions_copy[step + 1]) != 0:
                            actions_copy[step - 1] = (float(actions_copy[step - 1]) /
                                                      float(actions_copy[step + 1]))
                            del actions_copy[step]
                            del actions_copy[step]
                            step -= 2
                        else:
                            res = '*** Ошибка: деление на ноль ***'
                            outputlog(res)
                            return res
                    step += 1
                step = 0
                actions = actions_copy
                while step < len(actions):
                    if actions[step] == '+':
                        actions_copy[step - 1] = (float(actions_copy[step - 1]) +
                                                  float(actions_copy[step + 1]))
                        del actions_copy[step]
                        del actions_copy[step]
                        step -= 2
                    elif actions[step] == '-':
                        actions_copy[step - 1] = (float(actions_copy[step - 1]) -
                                                  float(actions_copy[step + 1]))
                        del actions_copy[step]
                        del actions_copy[step]
                        step -= 2
                    step += 1
                try:
                    full_actions.insert(step_left, actions_copy[0])
                except IndexError:
                    res = 'Ошибка ввода. Введите выражение аналогично примеру'
                    outputlog(res)
                    return res
            res = float(full_actions[0])
            outputlog(res)
            return res


def rand(randrange, banlist):
    from history.logs_script import inputlog, outputlog

    inputlog(randrange, banlist)

    if len(randrange.split()) > 2:
        res = 'Ошибка ввода(введено больше двух чисел). Введите диапазон согласно примеру'
        outputlog(res)
        return res
    else:
        for i in randrange:
            if not i.isnumeric() and i != ' ' and i != '' and i != '-':
                res = 'Ошибка ввода(получены не числовые значения). Введите диапазон согласно примеру'
                outputlog(res)
                return res
    for i in banlist:
        if not i.isnumeric() and i != ' ' and i != '' and i != '-':
            res = 'Ошибка ввода(запрещённые числа). Введите диапазон согласно примеру'
            outputlog(res)
            return res

    from random import randint
    try:
        res = randint(int(randrange.split()[0]), int(randrange.split()[1]))
    except:
        res = 'Ошибка ввода (Получен пустой диапазон). Расположите числа по возрастанию'
        outputlog(res)
        return res
    counter_range = 0
    counter_banlist = 0
    for i in range(int(randrange.split()[0]), int(randrange.split()[1]) + 1):
        counter_range += 1
        if i in list(map(int, banlist.split())):
            counter_banlist += 1
    if counter_range == counter_banlist:
        res = 'Ошибка ввода (Запрещены все значения)'
        outputlog(res)
        return res
    while res in list(map(int, banlist.split())):
        res = randint(int(randrange.split()[0]), int(randrange.split()[1]))
        outputlog(res)
    return res


def mode_check(choise):
    from history.logs_script import inputlog
    inputlog(choise)
    if not choise.isnumeric():
        return False

    elif int(choise) >= 3:
        return False

    else:
        return int(choise)
