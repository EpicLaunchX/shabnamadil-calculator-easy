import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_subtract_valid_operands(calculator):
    operands = operands_factory(3, 5)
    assert calculator.subtract(operands) == -2


def test_subtract_negative_operands(calculator):
    operands = operands_factory(-3, -5)
    assert calculator.subtract(operands) == 2


def test_subtract_zero_operands(calculator):
    operands = operands_factory(0, 5)
    assert calculator.subtract(operands) == -5


def test_subtract_mixed_operands(calculator):
    operands = operands_factory(3, -5)
    assert calculator.subtract(operands) == 8
