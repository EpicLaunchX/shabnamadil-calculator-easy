from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main():
    try:
        first_operand = int(input("Enter first operand:"))
        second_operand = int(input("Enter second operand:"))
    except ValueError:
        return "Error: Invalid input. Please enter valid integers."

    action = input("Enter action (add, subtract, divide, multiply):")

    if action.lower() not in ["add", "subtract", "divide", "multiply"]:
        return "Error: Invalid action. Please enter one of the following actions: add, subtract, divide, multiply."

    try:
        if action.lower() == "add":
            return Calculator().add(operands_factory(first_operand, second_operand))

        if action.lower() == "subtract":
            return Calculator().subtract(operands_factory(first_operand, second_operand))

        if action.lower() == "divide":
            return Calculator().divide(operands_factory(first_operand, second_operand))

        if action.lower() == "multiply":
            return Calculator().multiply(operands_factory(first_operand, second_operand))

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

    except ValueError:
        return "Error: Invalid input. Please enter valid integers."
