import pytest

import errors.errors as er

errors = [er.RangeError, er.InvalidNumberError, er.BanListRangeError, er.InputError, er.BanListError]

test_cases = [
    ("1", "2", "2", 1,),
    ("test", "test", "", er.InvalidNumberError),
    ("", "", "", er.InputError),
    ("1", "100", "test", er.BanListRangeError),
    ("1", "1", "", 1),
    ("1", "1", "1", er.BanListError),
    ("-5", "-4", "-5", -4),
    ("1", "10", "1 2 3 4 5 6 7 8 9", 10),
    ("-5", "-4", "-5 -4", er.BanListError),
]

@pytest.mark.parametrize("expression1, expression2, expression3, expected", test_cases)
def test_rand(expression1, expression2, expression3, expected):
    from service.service_functions import rand
    if expected in errors:
        with pytest.raises(expected):
            rand(expression1, expression2, expression3)
    else:
        assert rand(expression1, expression2, expression3) == expected
