"""Common shared file for supplementary utils"""


def get_operand_input(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError as err:
        raise ValueError("Error: Invalid input. Please enter a valid integer.") from err


def get_action_input() -> str:
    action = input("Enter action (add, subtract, divide, multiply):")
    if action.lower() not in ["add", "subtract", "divide", "multiply"]:
        raise ValueError("Error: Invalid action.")
    return action.lower()
