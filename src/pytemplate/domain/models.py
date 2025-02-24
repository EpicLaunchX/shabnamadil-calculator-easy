from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int

    def __post_init__(self):
        if not isinstance(self.first_operand, int):
            raise ValueError("First operand must be an integer")
        if not isinstance(self.second_operand, int):
            raise ValueError("Second operand must be an integer")


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    return Operands(first_operand, second_operand)
