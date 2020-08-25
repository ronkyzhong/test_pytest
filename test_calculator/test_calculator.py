import pytest

from calculator.calculator import Calculator


class TestCalculator:
    @pytest.mark.parametrize('a,b,result', [(1, 1, 2),
                                            (0.1, 0.1, 0.2),
                                            (2, 0.1, 2.1),
                                            (-1, 2, 1),
                                            (-1, -2, -3),
                                            ],
                             ids=("int", "float", "int_and_float", "negative_and_int", "negative"))
    def test_add(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.add()

    @pytest.mark.parametrize('a,b,result', [(2, 1, 1),
                                            (0.2, 0.1, 0.1),
                                            (2.2, 0.1, 2.1),
                                            (-1, 2, -3),
                                            (-1, -2, 1),
                                            ],
                             ids=("int", "float", "int_and_float", "negative_and_int", "negative"))
    def test_sub(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.sub()

    @pytest.mark.parametrize('a,b,result', [(2, 1, 2),
                                            (0.2, 0.1, 0.02),
                                            (2.2, 0.1, 0.22),
                                            (-1, 2, -2),
                                            (-1, -2, 2),
                                            ],
                             ids=("int", "float", "int_and_float", "negative_and_int", "negative"))
    def test_mul(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.mul()

    @pytest.mark.parametrize('a,b,result', [(2, 1, 2),
                                            (0.2, 0.1, 2),
                                            (2.2, 0.1, 22),
                                            (-1, 2, -0.5),
                                            (-1, -2, 0.5),
                                            (-1, 0, 0),
                                            (-1, 0.0, 0)
                                            ],
                             ids=(
                             "int", "float", "int_and_float", "negative_and_int", "negative", "div is 0", "div is 0.0"))
    def test_div(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.div()
