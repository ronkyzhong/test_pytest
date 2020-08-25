import json

import pytest
import yaml
import json
from calculator.calculator import Calculator

with open("../data/test_calculator_data.yaml", 'r') as f:
    data = yaml.safe_load(f)


class TestCalculator:
    @pytest.mark.parametrize('a,b,result', data['add'],
                             ids=("int", "float", "int_and_float", "negative_and_int", "negative"))
    def test_add(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.add()

    @pytest.mark.parametrize('a,b,result', data['sub'],
                             ids=("int", "float", "int_and_float", "negative_and_int", "negative"))
    def test_sub(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.sub()

    @pytest.mark.parametrize('a,b,result', data['mul'],
                             ids=("int", "float", "int_and_float", "negative_and_int", "negative"))
    def test_mul(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.mul()

    @pytest.mark.parametrize('a,b,result', data['div'],
                             ids=(
                                     "int", "float", "int_and_float", "negative_and_int", "negative", "div is 0",
                                     "div is 0.0"))
    def test_div(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.div()
