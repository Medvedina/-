import pytest

# Список тестовых примеров и ожидаемых результатов
test_cases = [
    ("4", False),
    ("3", 3),
    ("2", 2),
    ("0", 0),
    ("test", 0),
    ("", False),
]

@pytest.mark.parametrize("expression, expected", test_cases)
def test_calc(expression, expected):
    from service.service_functions import mode_check
    assert mode_check(expression) == expected