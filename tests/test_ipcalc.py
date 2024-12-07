import pytest
import ipaddress
import errors.errors as er

errors = [er.PrefixError, ipaddress.NetmaskValueError, ipaddress.AddressValueError]

test_cases = [
    ("192.168.1.9", "24", "prefix", 254),
    ("192.168.1.9", "255.255.255.0", "decimal", 254),
    ("192.168.1.9", "255.0.0.0", "decimal", 16777214),
    ("192.168.1.9", "8", "prefix", 16777214),
    ("192.168.1.9", "255.255.255.0", "prefix", er.PrefixError),
    ("192.168.1.9", "24", "decimal", ipaddress.NetmaskValueError),
    ("192/168/1/9", "24", "prefix", ipaddress.AddressValueError),
    ("192/168/1/9", "255.255.255.0", "decimal", ipaddress.AddressValueError),
    ("test", "192.168.1.9", "decimal", ipaddress.AddressValueError),
    ("test", "33", "prefix", er.PrefixError),
    ("test", "31", "prefix", ipaddress.AddressValueError),
    ("300.300.300.300", "255.255.255.0", "decimal", ipaddress.AddressValueError),
    ("300.300.300.300", "24", "prefix", ipaddress.AddressValueError),
    ("192.168.1.9", "192.168.1.9", "decimal", ipaddress.NetmaskValueError),
    ("192.168.1.9", "33", "prefix", er.PrefixError),
    ("", "32", "prefix", ipaddress.AddressValueError),
    ("", "255.255.255.0", "decimal", ipaddress.AddressValueError),
    ("", "", "prefix", er.PrefixError),
    ("", "", "decimal", ipaddress.NetmaskValueError)

]

@pytest.mark.parametrize("expression1, expression2, expression3, expected", test_cases)
def test_ipcalc(expression1, expression2, expression3, expected):
    from service.service_functions import IP
    if expected in errors:
        with pytest.raises(expected):
            IP(expression1, expression2, expression3)
    else:
        assert IP(expression1, expression2, expression3).host_count == expected