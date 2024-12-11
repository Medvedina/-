import pytest
import ipaddress
import errors.errors as er

errors = [er.PrefixError, ipaddress.NetmaskValueError, ipaddress.AddressValueError]

test_cases = [
    ("192.168.1.9", "24", "Префикс", 254),
    ("192.168.1.9", "255.255.255.0", "Десятичный", 254),
    ("192.168.1.9", "255.0.0.0", "Десятичный", 16777214),
    ("192.168.1.9", "8", "Префикс", 16777214),
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

@pytest.mark.parametrize("expression1, expression2, expression3, expected", test_cases)
def test_ipcalc(expression1, expression2, expression3, expected):
    from service.service_functions import IP
    if expected in errors:
        with pytest.raises(expected):
            IP(expression1, expression2, expression3)
    else:
        assert IP(expression1, expression2, expression3).host_count == expected
