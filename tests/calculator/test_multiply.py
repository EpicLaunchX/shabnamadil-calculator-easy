import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_multiply_valid_operands(calculator):
    operands = operands_factory(3, 5)
    result = calculator.multiply(operands)
    assert result == 15


def test_multiply_negative_operands(calculator):
    operands = operands_factory(-3, -5)
    result = calculator.multiply(operands)
    assert result == 15


def test_multiply_zero_operands(calculator):
    operands = operands_factory(0, 5)
    result = calculator.multiply(operands)
    assert result == 0


def test_multiply_mixed_operands(calculator):
    operands = operands_factory(3, -5)
    result = calculator.multiply(operands)
    assert result == -15
