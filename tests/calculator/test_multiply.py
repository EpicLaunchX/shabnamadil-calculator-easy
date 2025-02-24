import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_multiply_valid_operands():
    assert Calculator().multiply(operands_factory(3, 5)) == 15


def test_multiply_negative_operands():
    assert Calculator().multiply(operands_factory(-3, -5)) == 15


def test_multiply_zero_operands():
    assert Calculator().multiply(operands_factory(0, 5)) == 0


def test_multiply_mixed_operands():
    assert Calculator().multiply(operands_factory(3, -5)) == -15
