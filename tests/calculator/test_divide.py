import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_divide_valid_operands(calculator):
    operands = operands_factory(6, 3)
    assert calculator.divide(operands) == 2


def test_divide_negative_operands(calculator):
    operands = operands_factory(-3, -5)
    assert calculator.divide(operands) == 0.6


def test_divide_zero_operands(calculator):
    operands = operands_factory(0, 5)
    assert calculator.divide(operands) == 0


def test_divide_by_zero(calculator):
    operands = operands_factory(5, 0)
    with pytest.raises(ZeroDivisionError):
        calculator.divide(operands)


def test_divide_mixed_operands(calculator):
    operands = operands_factory(3, -5)
    assert calculator.divide(operands) == -0.6
