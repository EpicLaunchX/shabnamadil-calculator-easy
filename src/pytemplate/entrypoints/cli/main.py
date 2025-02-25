from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator
from pytemplate.utils.common import get_action_input, get_operand_input


def main():
    first_operand = get_operand_input("Enter first operand:")
    second_operand = get_operand_input("Enter second operand:")
    action = get_action_input()

    try:
        operations = {
            "add": Calculator().add,
            "subtract": Calculator().subtract,
            "divide": Calculator().divide,
            "multiply": Calculator().multiply,
        }

        return operations[action](operands_factory(first_operand, second_operand))

    except ZeroDivisionError as err:
        raise ValueError("Error: Cannot divide by zero") from err

    except ValueError as err:
        raise ValueError("Error: Invalid input. Please enter a valid integer.") from err
