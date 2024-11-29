from history.logs_script import *

def random_check(test_value):
    if (not test_value.isnumeric() and test_value != ' ' and
            test_value != '' and test_value != '-'):
        return True
    else:
        return False
def calc(query):
    logger.info(f'*Калькулятор* Введено: {query}')
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
    operations = ['+', '-', '*', '/', '^']
    actions = []
    actions_full = []
    action_current = ''

    if query.count('(') != query.count(')'):
        logger.error(f'Ошибка ввода. Закройте все скобки')
        return 'Ошибка ввода. Закройте все скобки'

    while query != 'exit':
        if query == 'exit':
            return 'Выход'
        else:
            step_left = 0
            for char in query:
                if char in nums:
                    if char != ',':
                        action_current += char
                    elif char == ',':
                        action_current += '.'
                elif char in operations or char in '()':
                    if action_current:
                        actions.append(action_current)
                        action_current = ''
                    actions.append(char)
            if action_current:
                actions.append(action_current)
            actions.insert(0, '(')
            actions.append(')')
            actions_full = actions.copy()
            while len(actions_full) != 1:
                step = 0
                bracket_flag = True
                while step < len(actions_full):
                    if bracket_flag:
                        if actions_full[step] == ')':
                            step_right = step
                            actions.clear()
                            step_sub = 0
                            while step_left + step_sub <= step_right:
                                actions.append(actions_full[step_left])
                                del actions_full[step_left]
                                step_sub += 1
                            bracket_flag = False
                            del actions[0]
                            del actions[step_right - step_left - 1]
                        elif actions_full[step] == '(':
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
                        try:
                            actions_copy[step - 1] = (float(actions_copy[step - 1]) /
                                                      float(actions_copy[step + 1]))
                            del actions_copy[step]
                            del actions_copy[step]
                            step -= 2
                        except ZeroDivisionError:
                            logger.error(f'*Калькулятор* Ошибка. Деление на 0')
                            return ('Ошибка. Деление на 0')
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
                    actions_full.insert(step_left, actions_copy[0])
                except IndexError:
                    logger.error(f'*Калькулятор* Ошибка ввода. '
                                 f'Введите выражение аналогично примеру')
                    return 'Ошибка ввода. Введите выражение аналогично примеру'
            res = float(actions_full[0])
            logger.info(f'*Калькулятор* Успешно. Результат: {res}')
            return res


def rand(rand_range, ban_list):

    logger.info(f'Введено: rand_range= {rand_range}, ban_list= {ban_list}')

    if len(rand_range.split()) > 2:
        logger.error('*Генератор* Ошибка ввода(введено больше двух чисел). '
                     'Введите диапазон согласно примеру')
        return ('Ошибка ввода(введено больше двух чисел). '
                'Введите диапазон согласно примеру')
    else:
        for i in rand_range:
            if random_check(i):
                logger.error('*Генератор* Ошибка ввода(получены не числовые значения). '
                             'Введите диапазон согласно примеру')
                return ('Ошибка ввода(получены не числовые значения). '
                        'Введите диапазон согласно примеру')

    for i in ban_list:
        if random_check(i):
            logger.error('*Генератор* Ошибка ввода(запрещённые числа). '
                         'Введите диапазон согласно примеру')
            return ('Ошибка ввода(запрещённые числа). '
                    'Введите диапазон согласно примеру')

    from random import randint

    try:
        res = randint(int(rand_range.split()[0]), int(rand_range.split()[1]))
    except:
        logger.error('*Генератор* Ошибка ввода. '
                     'Получен пустой диапазон.')
        return ('Ошибка ввода (Получен пустой диапазон). '
                'Расположите числа по возрастанию')

    counter_rand_range = 0
    counter_ban_list = 0

    for i in range(int(rand_range.split()[0]), int(rand_range.split()[1]) + 1):
        counter_rand_range += 1
        if i in list(map(int, ban_list.split())):
            counter_ban_list += 1

    if counter_rand_range == counter_ban_list:
        logger.error('*Генератор* Ошибка ввода. Запрещены все значения')
        return 'Ошибка ввода (Запрещены все значения)'

    while res in list(map(int, ban_list.split())):
        res = randint(int(rand_range.split()[0]), int(rand_range.split()[1]))

    logger.info(f'Успешно, число: {res}')
    return res


def mode_check(choise):
    if not choise.isnumeric():
        return False

    elif int(choise) >= 3:
        return False

    else:
        return int(choise)

