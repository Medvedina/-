import errors.errors as er
import ipaddress


case_calc_negative = [
    ("test", er.InputError),
    ("(32+3", er.BracketError),
    ("12 / 0", er.DivZero),
    ("", er.InputError),
    ("-", er.InputError)
]

case_calc_positive = [
    ("12 + 15 / (3 + 2) * 4", 12 + 15 / (3 + 2) * 4),
    ("(2 + 3) * 5", (2 + 3) * 5),
    ("(8 / 4) + (3 * 2)", (8 / 4) + (3 * 2)),
    ("(10 + 2) / 3", (10 + 2) / 3),
    ("3 * (4 + 2) - 5", 3 * (4 + 2) - 5),
    ("((((31*12)-15/3)+2^3)-5)", ((((31*12)-15/3)+2**3)-5))
]

case_ipcalc_negative = [
    ("192.168.1.9", "255.255.255.0", "Префикс", er.PrefixError),
    ("192.168.1.9", "24", "Десятичный", ipaddress.NetmaskValueError),
    ("192/168/1/9", "24", "Префикс", ipaddress.AddressValueError),
    ("192/168/1/9", "255.255.255.0", "Десятичный", ipaddress.AddressValueError),
    ("test", "192.168.1.9", "Десятичный", ipaddress.AddressValueError),
    ("test", "33", "Префикс", er.PrefixError),
    ("test", "31", "Префикс", ipaddress.AddressValueError),
    ("300.300.300.300", "255.255.255.0", "Десятичный", ipaddress.AddressValueError),
    ("300.300.300.300", "24", "Префикс", ipaddress.AddressValueError),
    ("192.168.1.9", "192.168.1.9", "Десятичный", ipaddress.NetmaskValueError),
    ("192.168.1.9", "33", "Префикс", er.PrefixError),
    ("", "32", "Префикс", ipaddress.AddressValueError),
    ("", "255.255.255.0", "Десятичный", ipaddress.AddressValueError),
    ("", "", "Префикс", er.PrefixError),
    ("", "", "Десятичный", ipaddress.NetmaskValueError)
]

case_ipcalc_positive = [
    ("192.168.1.9", "24", "Префикс", 254),
    ("192.168.1.9", "255.255.255.0", "Десятичный", 254),
    ("192.168.1.9", "255.0.0.0", "Десятичный", 16777214),
    ("192.168.1.9", "8", "Префикс", 16777214)
]

case_numsys_negative = [
    ("decimal", "test", er.InvalidNumberError),
    ("binary", "test", er.InvalidNumberError),
    ("binary", "1243", er.InvalidNumberError),
    ("octal", "129", er.InvalidNumberError),
    ("octal", "test", er.InvalidNumberError),
    ("hexadecimal", "test", er.InvalidNumberError),
    ("hexadecimal", "3HG", er.InvalidNumberError)
]

case_numsys_positive = [
    ("decimal", "943", ['1110101111', '1657', '943', '3af']),
    ("binary", "1110101111", ['1110101111', '1657', '943', '3af']),
    ("octal", "1657", ['1110101111', '1657', '943', '3af']),
    ("hexadecimal", "3af", ['1110101111', '1657', '943', '3af']),
    ("hexadecimal", "3AF", ['1110101111', '1657', '943', '3af'])
]

case_rand_negative = [
    ("test", "test", "", er.InvalidNumberError),
    ("", "", "", er.InputError),
    ("1", "100", "test", er.BanListRangeError),
    ("1", "1", "1", er.BanListError),
    ("-5", "-4", "-5 -4", er.BanListError)
]

case_rand_positive = [
    ("1", "2", "2", 1,),
    ("1", "1", "", 1),
    ("-5", "-4", "-5", -4),
    ("1", "10", "1 2 3 4 5 6 7 8 9", 10),
]

