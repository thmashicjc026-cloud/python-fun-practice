import unittest
from contextlib import redirect_stdout
from io import StringIO
from math import factorial

from practice.revise_me import (
    find_minimum,
    calculate_factorial,
    unique_elements,
    find_number_of_even_numbers,
    generate_squared_dict,
    convert_to_word_list,
    letters_count_map,
    draw_square,
)

SENTENCE = (
    "There is only one to fear and his name is Death,"
    " and there is only one thing we say to Death: 'Not today!"
)


class TestChallenge(unittest.TestCase):

    # ------------------------------------------------------------------
    # Original tests
    # ------------------------------------------------------------------
    def test_find_minimum(self):
        self.assertEqual(find_minimum([4, 2, 9, 1]), 1)
        self.assertEqual(find_minimum([-5, -1, -10, 0]), -10)
        self.assertIsNone(find_minimum([]))

    def test_calculate_factorial(self):
        self.assertEqual(calculate_factorial(5), 120)
        self.assertEqual(calculate_factorial(0), 1)  # edge case: 0! is 1
        self.assertEqual(calculate_factorial(7), factorial(7))  # matches math.factorial

    def test_unique_elements(self):
        self.assertEqual(unique_elements([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(unique_elements(['a', 'b', 'a', 'c']), ['a', 'b', 'c'])
        self.assertEqual(unique_elements([]), [])

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_generate_squared_dict(self):
        cases = {
            5: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25},
            1: {1: 1},
            10: {i: i * i for i in range(1, 11)},
            0: {},
            2: {1: 1, 2: 4},
            -5: {-5: 25, -4: 16, -3: 9, -2: 4, -1: 1},
            -1: {-1: 1},
            -10: {i: i * i for i in range(-10, 0)},
            -2: {-2: 4, -1: 1},
            -3: {-3: 9, -2: 4, -1: 1},
            -6: {i: i * i for i in range(-6, 0)},
        }
        for n, expected in cases.items():
            with self.subTest(n=n):
                self.assertEqual(generate_squared_dict(n), expected)

    def test_letters_count_sentence(self):
        char_count = letters_count_map(SENTENCE)
        self.assertEqual(
            {'a': 8, 'b': 0, 'c': 0, 'd': 5, 'e': 11, 'f': 1, 'g': 1, 'h': 6, 'i': 5, 'j': 0, 'k': 0, 'l': 2, 'm': 1,
             'n': 9, 'o': 8, 'p': 0, 'q': 0, 'r': 3, 's': 5, 't': 9, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 4, 'z': 0},
            char_count)

    def test_4_square(self):
        # redirect_stdout restores sys.stdout afterwards (the original test left it captured)
        text_capture = StringIO()
        with redirect_stdout(text_capture):
            draw_square(4)
        self.assertEqual("****\n****\n****\n****\n", text_capture.getvalue())

    # ------------------------------------------------------------------
    # Added edge-case tests
    # ------------------------------------------------------------------
    def test_find_minimum_edge_cases(self):
        self.assertEqual(find_minimum([7]), 7)
        self.assertEqual(find_minimum([3, 3, 3]), 3)
        self.assertEqual(find_minimum([2.5, 1.5, 3.5]), 1.5)
        self.assertEqual(find_minimum([1, 2, 3]), 1)       # minimum first
        self.assertEqual(find_minimum([3, 2, 1]), 1)       # minimum last
        self.assertEqual(find_minimum([0]), 0)             # 0 is a real answer, not "empty"

    def test_calculate_factorial_edge_cases(self):
        self.assertEqual(calculate_factorial(1), 1)
        self.assertEqual(calculate_factorial(2), 2)
        self.assertEqual(calculate_factorial(10), 3628800)
        self.assertEqual(calculate_factorial(20), factorial(20))
        with self.assertRaises(ValueError):
            calculate_factorial(-1)

    def test_unique_elements_edge_cases(self):
        self.assertEqual(unique_elements([3, 1, 3, 2, 1]), [3, 1, 2])      # first appearance wins
        self.assertEqual(unique_elements([5, 5, 5]), [5])
        self.assertEqual(unique_elements([1, 2, 3]), [1, 2, 3])
        self.assertEqual(unique_elements([1, '1', 1]), [1, '1'])           # 1 and '1' are different
        original = [1, 1, 2]
        unique_elements(original)
        self.assertEqual(original, [1, 1, 2])                              # input untouched

    def test_find_number_of_even_numbers_edge_cases(self):
        self.assertEqual(find_number_of_even_numbers([]), 0)
        self.assertEqual(find_number_of_even_numbers([1, 3, 5]), 0)
        self.assertEqual(find_number_of_even_numbers([0]), 1)               # zero is even
        self.assertEqual(find_number_of_even_numbers([-2, -1, -4]), 2)      # negatives work
        self.assertEqual(find_number_of_even_numbers([2, 4, 6]), 3)

    def test_convert_to_word_list(self):
        self.assertEqual(convert_to_word_list("hello world"), ["hello", "world"])
        self.assertEqual(convert_to_word_list("single"), ["single"])
        self.assertEqual(convert_to_word_list(""), [])
        self.assertEqual(convert_to_word_list("   "), [])
        self.assertEqual(convert_to_word_list("  lots   of   space  "), ["lots", "of", "space"])
        self.assertEqual(convert_to_word_list("tabs\tand\nnewlines"), ["tabs", "and", "newlines"])
        self.assertEqual(convert_to_word_list("Hello, world!"), ["Hello,", "world!"])  # punctuation stays

    def test_letters_count_map_edge_cases(self):
        empty = letters_count_map("")
        self.assertEqual(len(empty), 26)
        self.assertTrue(all(count == 0 for count in empty.values()))
        self.assertEqual(sorted(empty), list("abcdefghijklmnopqrstuvwxyz"))

        abc = letters_count_map("abc")
        self.assertEqual((abc['a'], abc['b'], abc['c'], abc['d']), (1, 1, 1, 0))

        mixed = letters_count_map("AaBb")                                  # case-insensitive
        self.assertEqual((mixed['a'], mixed['b']), (2, 2))
        self.assertFalse(any(k.isupper() for k in mixed))                  # keys are lowercase only

        noisy = letters_count_map("a1 a!? 22")                             # digits/punct/space ignored
        self.assertEqual(noisy['a'], 2)
        self.assertEqual(sum(noisy.values()), 2)
        self.assertEqual(len(noisy), 26)

    def test_draw_square_edge_cases(self):
        for height in (1, 2, 3, 6):
            with self.subTest(height=height):
                out = StringIO()
                with redirect_stdout(out):
                    result = draw_square(height)
                self.assertIsNone(result)                                   # prints, does not return
                self.assertEqual(out.getvalue(), ("*" * height + "\n") * height)


if __name__ == "__main__":
    unittest.main()
