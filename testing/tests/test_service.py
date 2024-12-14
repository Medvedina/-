import pytest
import testing.data.mock as mock
import service.service_functions as service


@pytest.mark.parametrize("expression, expected", mock.case_calc_negative)
def test_calc_neg(expression, expected):
    with pytest.raises(expected):
        assert service.calc(expression) == expected


@pytest.mark.parametrize("expression, expected", mock.case_calc_positive)
def test_calc_pos(expression, expected):
    assert service.calc(expression) == expected


@pytest.mark.parametrize("expression1, expression2, expression3, expected", mock.case_rand_negative)
def test_rand_neg(expression1, expression2, expression3, expected):
    with pytest.raises(expected):
        assert service.rand(expression1, expression2, expression3) == expected


@pytest.mark.parametrize("expression1, expression2, expression3, expected", mock.case_rand_positive)
def test_rand_pos(expression1, expression2, expression3, expected):
    assert service.rand(expression1, expression2, expression3) == expected


@pytest.mark.parametrize("expression1, expression2, expression3, expected", mock.case_ipcalc_negative)
def test_ipcalc_neg(expression1, expression2, expression3, expected):
    with pytest.raises(expected):
        assert service.IP(expression1, expression2, expression3).host_count == expected


@pytest.mark.parametrize("expression1, expression2, expression3, expected", mock.case_ipcalc_positive)
def test_ipcalc_pos(expression1, expression2, expression3, expected):
    assert service.IP(expression1, expression2, expression3).host_count == expected


@pytest.mark.parametrize("expression1, expression2, expected", mock.case_numsys_negative)
def test_numsys_neg(expression1, expression2, expected):
    with pytest.raises(expected):
        service.numsys(expression1, expression2)


@pytest.mark.parametrize("expression1, expression2, expected", mock.case_numsys_positive)
def test_numsys_pos(expression1, expression2, expected):
    assert service.numsys(expression1, expression2) == expected
