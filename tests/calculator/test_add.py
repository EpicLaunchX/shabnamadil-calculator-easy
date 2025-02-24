import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_add_valid_operands(calculator):
    operands = operands_factory(3, 5)
    result = calculator.add(operands)
    assert result == 8


def test_add_negative_operands(calculator):
    operands = operands_factory(-3, -5)
    result = calculator.add(operands)
    assert result == -8


def test_add_zero_operands(calculator):
    operands = operands_factory(0, 5)
    result = calculator.add(operands)
    assert result == 5


def test_add_mixed_operands(calculator):
    operands = operands_factory(3, -5)
    result = calculator.add(operands)
    assert result == -2
