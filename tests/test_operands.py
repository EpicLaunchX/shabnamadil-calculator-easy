import pytest

from src.pytemplate.domain.models import Operands


def test_valid_operands():
    op = Operands(5, 10)
    assert op.first_operand == 5
    assert op.second_operand == 10


def test_invalid_first_operand():
    with pytest.raises(ValueError):
        Operands("Jhon", 5)


def test_invalid_second_operand():
    with pytest.raises(ValueError):
        Operands(5, "Doe")
