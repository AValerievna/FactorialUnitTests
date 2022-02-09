import pytest

from proj.factorial import get_factorial
from proj.invalid_argument_error import InvalidArgumentError


class TestFactorial(object):
    @pytest.mark.parametrize("num, exp_result", [
        (0, 1),
        (1, 1),
        (4, 24),
        (21, 51090942171709440000),
        pytest.param("some", None, marks=pytest.mark.xfail(raises=InvalidArgumentError, reason="invalid args",
                                                           strict=True)),
        pytest.param(3.4, None, marks=pytest.mark.xfail(raises=InvalidArgumentError, reason="invalid args",
                                                        strict=True))

    ], ids=['0', '1', '4', '21', 'str', 'float'])
    def test_check_result(self, num, exp_result):
        """Check result with valid params"""
        result = get_factorial(num)
        assert result == exp_result

    @pytest.mark.parametrize("num", [
        "some", -199, 6.6, -13
    ], ids=['str', 'float', 'negative_int', 'bool'])
    def test_check_error(self, num):
        """Check result with valid params"""
        with pytest.raises(InvalidArgumentError):
            get_factorial(num)
