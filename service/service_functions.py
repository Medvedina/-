from history.logs_script import *
from errors.errors import *
import ipaddress


def notify_user(*args):
    return print(*args)


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
    countable = False

    for char in query:
        if char in nums:
            countable = True

    if countable is False:
        raise InputError

    if query.count('(') != query.count(')'):
        logger.error(f'Ошибка ввода. Закройте все скобки')
        raise BracketError

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
                            raise DivZero
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
                    raise InputError
            res = float(actions_full[0])
            logger.info(f'*Калькулятор* Успешно. Результат: {res}')
            return res


def rand(rand_range_start, rand_range_finish, ban_list):
    logger.info(f'Введено: Начало - {rand_range_start}, Конец - {rand_range_finish}, запрещено = {ban_list}')

    for i in rand_range_start:
        if random_check(i):
            logger.error('*Генератор* Ошибка ввода(получены не числовые значения). '
                         'Введите диапазон согласно примеру')
            raise InvalidNumberError
    for i in rand_range_finish:
        if random_check(i):
            logger.error('*Генератор* Ошибка ввода(получены не числовые значения). '
                         'Введите диапазон согласно примеру')
            raise InvalidNumberError
    for i in ban_list:
        if random_check(i):
            logger.error('*Генератор* Ошибка ввода(избегаемые числа). '
                         'Введите диапазон согласно примеру')
            raise BanListRangeError

    from random import randint

    try:
        res = randint(int(rand_range_start), int(rand_range_finish))
    except ValueError:
        logger.error('*Генератор* Ошибка ввода. '
                     'Получен пустой диапазон.')
        raise InputError

    counter_rand_range = 0
    counter_ban_list = 0

    for i in range(int(rand_range_start), int(rand_range_finish) + 1):
        counter_rand_range += 1
        if i in list(map(int, ban_list.split())):
            counter_ban_list += 1

    if counter_rand_range == counter_ban_list:
        logger.error('*Генератор* Ошибка ввода. Запрещены все значения')
        raise BanListError

    while res in list(map(int, ban_list.split())):
        res = randint(int(rand_range_start), int(rand_range_finish))

    logger.info(f'Успешно, число: {res}')
    return res

def numsys(original_system, number):
    logger.info(f'ВВОД: {original_system}, {number}')
    if original_system == 'decimal':
        try:
            decimal = int(number)
            binary = bin(int(number))[2:]
            octal = oct(int(number))[2:]
            hexadecimal = hex(int(number))[2:]
            logger.info(f'Результат: {[binary, octal, str(decimal), hexadecimal]}')
            return [binary, octal, str(decimal), hexadecimal]
        except:
            logger.error(f'Ошибка ввода. Введите корректное число {InvalidNumberError}')
            raise InvalidNumberError

    elif original_system == 'binary':
        try:
            binary = int(number, 2)
            decimal = 0
            for index, bit in enumerate(number[::-1]):
                decimal += int(bit) * (2 ** index)
            octal = oct(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
            logger.info(f'Результат: {[binary, octal, str(decimal), hexadecimal]}')
            return [binary, octal, str(decimal), hexadecimal]
        except:
            logger.error(f'Ошибка ввода. Введите корректное число {InvalidNumberError}')
            raise InvalidNumberError

    elif original_system == 'octal':
        try:
            octal = number
            decimal = 0
            for index, bit in enumerate(number[::-1]):
                decimal += int(bit) * (8 ** index)
            binary = bin(decimal)[2:]
            hexadecimal = hex(decimal)[2:]
            logger.info(f'Результат: {[binary, octal, str(decimal), hexadecimal]}')
            return [binary, octal, str(decimal), hexadecimal]
        except:
            logger.error(f'Ошибка ввода. Введите корректное число {InvalidNumberError}')
            raise InvalidNumberError

    elif original_system == 'hexadecimal':
        try:
            hexadecimal = number.lower()
            decimal = int(number, 16)
            binary = bin(decimal)[2:]
            octal = oct(decimal)[2:]
            logger.info(f'Результат: {[binary, octal, str(decimal), hexadecimal]}')
            return [binary, octal, str(decimal), hexadecimal]
        except:
            logger.error(f'Ошибка ввода. Введите корректное число {InvalidNumberError}')
            raise InvalidNumberError


class IP:
    def __init__(self, ip_address, subnet_mask, mask_flag):
        self.ip_address = ip_address
        if mask_flag == 'Префикс':
            self.subnet_mask_index = subnet_mask
            self.subnet_mask = self.prefix_to_decimal(self.subnet_mask_index)

        elif mask_flag == 'Десятичный':
            self.subnet_mask = subnet_mask
            self.subnet_mask_index = self.get_mask_index(subnet_mask)

        self.network_address = self.get_network_address(ip_address, subnet_mask)
        self.binary_address = self.convert_to_binary(ip_address)
        self.host_count = self.calculate_host_count(subnet_mask)
        logger.info(f'Успешный рассчёт ip-адреса: {self.ip_address}')
    def convert_to_binary(self, ip_address):
        try:
            octets = ip_address.split('.')
            binary_octets = [format(int(octet), '08b') for octet in octets]
            return '.'.join(binary_octets)
        except Exception as e:
            logger.error(f'Ошибка. Введите корректный IP-адрес ({e.__class__.__name__}')
            raise ipaddress.AddressValueError

    def calculate_host_count(self, subnet_mask):
        try:
            if subnet_mask.count('.') == 0:
                return 2**(32 - int(subnet_mask)) - 2
        except Exception as e:
            logger.error(f'Ошибка. Введите корректную маску подсети ({e.__class__.__name__}')
            raise ipaddress.NetmaskValueError
        else:
            mask_bits = sum(bin(int(octet)).count('1') for octet in subnet_mask.split('.'))
            return (2 ** (32 - mask_bits)) - 2

    def get_network_address(self, ip_address, subnet_mask):
        try:
            network = ipaddress.IPv4Network(f'{ip_address}/{subnet_mask}', strict=False)
            return str(network.network_address)
        except ipaddress.NetmaskValueError as e:
            logger.error(f'Ошибка. Введите корректную маску подсети ({e.__class__.__name__})')
            raise ipaddress.NetmaskValueError

        except ipaddress.AddressValueError as e:
            logger.error(f'Ошибка. Введите корректный IP-адрес ({e.__class__.__name__})')
            raise ipaddress.AddressValueError

    def get_mask_index(self, subnet_mask):
        if subnet_mask.count('.') < 3:
            logger.error(f'Ошибка. Введите корректную маску подсети (NetmaskValueError)')
            raise ipaddress.NetmaskValueError
        octets = subnet_mask.split('.')
        binary_octets = [format(int(octet), '08b') for octet in octets]
        return str(binary_octets).count('1')

    def prefix_to_decimal(self, prefix):
        try:
            int(prefix)
        except Exception as e:
            logger.error(f'Ошибка. Введите корректный префикс маски подсети ({e.__class__.__name__}')
            raise PrefixError

        if not (0 <= int(prefix) <= 32):
            logger.error(f'Ошибка. Префикс длиннее 32. (PrefixError)')
            raise PrefixError

        mask_bin = '1' * int(prefix) + '0' * (32 - int(prefix))
        mask_decimal = [str(int(mask_bin[i:i + 8], 2)) for i in range(0, 32, 8)]
        return '.'.join(mask_decimal)

    def __str__(self):
        return (f'IP-адрес: {self.ip_address}\nДвоичный адрес: {self.binary_address}\nМаска подсети: {self.subnet_mask}\nИндекс маски подсети: {self.subnet_mask_index}\n'
                f'Число хостов: {self.host_count}\nАдрес сети: {self.network_address}\n')
