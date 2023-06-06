from code_to_test import add


def test_add_two_positive_numbers() -> None:
    assert add(5, 10) == 15


def test_add_two_negative_numbers() -> None:
    assert add(-5, -10) == -15


def test_add_two_digits_str() -> None:
    assert add("5", "10") == 15


# si les param n'avaient pas été typés et qu'on voulait testet la levée d'une erreur :
# def test_add_wrong_types() -> None:
#     with pytest.raise(TypeError):
#         add(None, [])
