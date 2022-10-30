import pytest
from test_data import REMOVE_PARENTHESES_DATA, IS_PRIME_DATA, IS_DIABOLIC_DATA, MULTIPLICATION_TABLE_DATA, CIPHER_DATA, DECIPHER_DATA


def _data_args(data):
    if not data:
        return
    size = len(data[0])
    names = []
    for entry in data:
        name = []
        for arg in range(size - 1):
            name.append(str(entry[arg]))
        names.append(", ".join(name))
    return names


@pytest.mark.parametrize("arg, expected_output", REMOVE_PARENTHESES_DATA, ids=_data_args(REMOVE_PARENTHESES_DATA))
def test_task_1_remove_parentheses(arg, expected_output):
    from task_1 import remove_parentheses
    assert remove_parentheses(arg) == expected_output


def test_task_2_inflation():
    file = open("task_2.py", "r", encoding="utf-8")
    assert file.readline() != "# Remove this comment to confirm that this task is done"


@pytest.mark.parametrize("arg, expected_output", IS_PRIME_DATA, ids=_data_args(IS_PRIME_DATA))
def test_task_3_is_prime(arg, expected_output):
    from task_3 import is_prime
    assert is_prime(arg) == expected_output


@pytest.mark.parametrize("arg, expected_output", IS_DIABOLIC_DATA, ids=_data_args(IS_DIABOLIC_DATA))
def test_task_3_is_diabolic(arg, expected_output):
    from task_3 import is_diabolic
    assert is_diabolic(arg) == expected_output


@pytest.mark.parametrize("x1, x2, y1, y2, expected_output", MULTIPLICATION_TABLE_DATA, ids=_data_args(MULTIPLICATION_TABLE_DATA))
def test_task_4_multiplication_table(capfd, x1, x2, y1, y2, expected_output):
    from task_4 import multiplication_table
    multiplication_table(x1, x2, y1, y2)
    out, _ = capfd.readouterr()
    assert out == expected_output


@pytest.mark.parametrize("text, shift, expected_output", CIPHER_DATA, ids=_data_args(CIPHER_DATA))
def test_task_5_cipher(text, shift, expected_output):
    from task_5 import cipher
    assert cipher(text, shift) == expected_output


@pytest.mark.parametrize("text, shift, expected_output", DECIPHER_DATA, ids=_data_args(DECIPHER_DATA))
def test_task_5_decipher(text, shift, expected_output):
    from task_5 import decipher
    assert decipher(text, shift) == expected_output
