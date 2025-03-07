import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_subtract_valid_operands():
    assert Calculator().subtract(operands_factory(3, 5)) == -2


def test_subtract_negative_operands():
    assert Calculator().subtract(operands_factory(-3, -5)) == 2


def test_subtract_zero_operands():
    assert Calculator().subtract(operands_factory(0, 5)) == -5


def test_subtract_mixed_operands():
    assert Calculator().subtract(operands_factory(3, -5)) == 8
