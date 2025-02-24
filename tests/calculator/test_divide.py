import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_divide_valid_operands():
    assert Calculator().divide(operands_factory(6, 3)) == 2


def test_divide_negative_operands():
    assert Calculator().divide(operands_factory(-3, -5)) == 0.6


def test_divide_zero_operands():
    assert Calculator().divide(operands_factory(0, 5)) == 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(operands_factory(5, 0))


def test_divide_mixed_operands():
    assert Calculator().divide(operands_factory(3, -5)) == -0.6
