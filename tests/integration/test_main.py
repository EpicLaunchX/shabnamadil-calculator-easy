from unittest.mock import patch

import pytest

from src.pytemplate.entrypoints.cli.main import main

@pytest.mark.integration
@pytest.mark.parametrize(
    "inputs, expected_output",
    [
        (["3", "5", "add"], 8),
        (["10", "4", "subtract"], 6),
        (["6", "2", "divide"], 3),
        (["3", "7", "multiply"], 21),
        (["5", "0", "divide"], "Error: Cannot divide by zero"),
        (["3", "Jhon", "add"], "Error: Invalid input. Please enter valid integers."),
        (["Jhon", "0", "add"], "Error: Invalid input. Please enter valid integers."),
        (["5", "6", "added"], "Error: Invalid action. Please enter one of the following actions: add, subtract, divide, multiply."),
        (["5", "6", "sub"], "Error: Invalid action. Please enter one of the following actions: add, subtract, divide, multiply."),
    ],
)
def test_main(inputs, expected_output):
    with patch("builtins.input", side_effect=inputs):
        result = main()
        assert result == expected_output
