def calc(query):
    from history.logs_script import inputlog

    inputlog(query)

    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
    operations = ['+', '-', '*', '/', '^']
    if query.count('(') != query.count(')'):
        return 'Ошибка ввода. Закройте все скобки.'
    for i in query:
        if (i not in nums and i not in operations and
                i != '(' and i != ')' and i != ' '):
            return 'Ошибка ввода. Введите выражение аналогично примеру'
    actions = []
    full_actions = []
    current_action = ''
    while query != 'exit':
        if query == 'exit':
            return 'Выход'
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
                            return '*** Ошибка: деление на ноль ***'
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
                    return 'Ошибка ввода. Введите выражение аналогично примеру'
            return float(full_actions[0])


def rand(randrange, banlist):
    from history.logs_script import inputlog

    inputlog(randrange, banlist)

    if len(randrange.split()) > 2:
        return 'Ошибка ввода(введено больше двух чисел). Введите диапазон согласно примеру'
    else:
        for i in randrange:
            if not i.isnumeric() and i != ' ' and i != '':
                return 'Ошибка ввода(получены не числовые значения). Введите диапазон согласно примеру'
    for i in banlist:
        if not i.isnumeric() and i != ' ' and i != '':
            return 'Ошибка ввода(запрещённые числа). Введите диапазон согласно примеру'

    from random import randint
    try:
        res = randint(int(randrange.split()[0]), int(randrange.split()[1]))
    except:
        return 'Ошибка ввода (Получен пустой диапазон). Расположите числа по возрастанию'
    while res in list(map(int, banlist.split())):
        res = randint(int(randrange.split()[0]), int(randrange.split()[1]))
    return res
