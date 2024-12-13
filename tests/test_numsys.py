import pytest

import errors.errors as er

errors = [er.InvalidNumberError]

test_cases = [
    ("decimal", "943", ['1110101111', '1657', '943', '3af']),
    ("decimal", "test", er.InvalidNumberError),
    ("binary", "1110101111", ['1110101111', '1657', '943', '3af']),
    ("binary", "test", er.InvalidNumberError),
    ("octal", "1657", ['1110101111', '1657', '943', '3af']),
    ("octal", "test", er.InvalidNumberError),
    ("hexadecimal", "3af", ['1110101111', '1657', '943', '3af']),
    ("hexadecimal", "test", er.InvalidNumberError),
    ("hexadecimal", "3HG", er.InvalidNumberError),
    ("hexadecimal", "3AF", ['1110101111', '1657', '943', '3af'])
]

@pytest.mark.parametrize("expression1, expression2, expected", test_cases)
def test_calc(expression1, expression2, expected):

    from service.service_functions import numsys
    if expected in errors:
        with pytest.raises(expected):
            numsys(expression1, expression2)
    else:
        assert numsys(expression1, expression2) == expected


