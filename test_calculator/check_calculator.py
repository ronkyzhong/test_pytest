import json

import pytest
import yaml
import json

from calculator.calculator import Calculator

with open("../data/test_calculator_data.yml", 'r') as f:
    data = yaml.safe_load(f)


class CheckCalculator:
    @pytest.mark.parametrize('a,b,result', data['add'].values(),
                             ids=data['add'].keys())
    def check_add(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.add()

    @pytest.mark.parametrize('a,b,result', data['sub'].values(),
                             ids=data['sub'].keys())
    def test_sub(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.sub()

    @pytest.mark.parametrize('a,b,result', data['mul'].values(),
                             ids=data['mul'].keys())
    def test_mul(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.mul()

    @pytest.mark.parametrize('a,b,result', data['div'].values(),
                             ids=data['div'].keys())
    def test_div(self, a, b, result, calc):
        cal = Calculator(a, b)
        assert result == cal.div()
