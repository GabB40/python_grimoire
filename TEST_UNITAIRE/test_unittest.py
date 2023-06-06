from unittest import TestCase

from code_to_test import add


class TestAddMethod(TestCase):
    def test_add_two_positive_numbers(self) -> None:
        self.assertEqual(add(5, 10), 15)

    def test_add_two_negative_numbers(self) -> None:
        self.assertEqual(add(-5, -10), -15)

    def test_add_two_digits_str(self) -> None:
        self.assertEqual(add("5", "10"), 15)

    # si les param n'avaient pas été typés et qu'on voulait testet la levée d'une erreur :
    # def test_add_wrong_types(self) -> None:
    #     with self.assertRaises(TypeError):
    #         add(None, [])
