import pytest

from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def test_add_valid_operands():
    assert Calculator().add(operands_factory(3, 5)) == 8


def test_add_negative_operands():
    assert Calculator().add(operands_factory(-3, -5)) == -8


def test_add_zero_operands():
    assert Calculator().add(operands_factory(0, 5)) == 5


def test_add_mixed_operands():
    assert Calculator().add(operands_factory(3, -5)) == -2
