import pytest

import errors.errors as er

errors = [er.InputError, er.BracketError, er.DivZero]

test_cases = [
    ("12 + 15 / (3 + 2) * 4", 12 + 15 / (3 + 2) * 4),
    ("(2 + 3) * 5", (2 + 3) * 5),
    ("(8 / 4) + (3 * 2)", (8 / 4) + (3 * 2)),
    ("(10 + 2) / 3", (10 + 2) / 3),
    ("3 * (4 + 2) - 5", 3 * (4 + 2) - 5),
    ("test", er.InputError),
    ("(32+3", er.BracketError),
    ("12 / 0", er.DivZero),
    ("", er.InputError),
    ("((((31*12)-15/3)+2^3)-5)", ((((31*12)-15/3)+2**3)-5)),
    ("-", er.InputError)
]

@pytest.mark.parametrize("expression, expected", test_cases)
def test_calc(expression, expected):

    from service.service_functions import calc
    if expected in errors:
        with pytest.raises(expected):
            calc(expression)
    else:
        assert calc(expression) == expected


