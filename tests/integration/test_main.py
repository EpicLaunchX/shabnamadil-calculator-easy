from unittest import mock

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
        (["5", "0", "divide"], pytest.raises(ValueError, match="Error: Cannot divide by zero")),
        (["3", "Jhon", "add"], pytest.raises(ValueError, match="Error: Invalid input. Please enter a valid integer.")),
        (["Jhon", "0", "add"], pytest.raises(ValueError, match="Error: Invalid input. Please enter a valid integer.")),
        (["5", "6", "added"], pytest.raises(ValueError, match="Error: Invalid action.")),
        (["5", "6", "sub"], pytest.raises(ValueError, match="Error: Invalid action.")),
    ],
)
def test_main(inputs, expected_output):
    with mock.patch("builtins.input", side_effect=inputs):
        if isinstance(expected_output, type(pytest.raises(ValueError))):
            with expected_output:
                main()
        else:
            result = main()
            assert result == expected_output
