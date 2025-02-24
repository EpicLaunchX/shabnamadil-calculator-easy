import pytest

from src.pytemplate.domain.models import Operands, operands_factory


def test_operands_factory_valid():
    operands = operands_factory(5, 10)
    assert isinstance(operands, Operands)
    assert operands.first_operand == 5
    assert operands.second_operand == 10


def test_operands_factory_invalid():
    with pytest.raises(ValueError):
        operands_factory("5", 10)

    with pytest.raises(ValueError):
        operands_factory(5, "10")

    with pytest.raises(ValueError):
        operands_factory("5", "10")

    with pytest.raises(ValueError):
        operands_factory(5.5, 10)

    with pytest.raises(ValueError):
        operands_factory(5, 10.5)
