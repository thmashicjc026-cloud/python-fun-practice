import unittest

from practice.loops_and_shapes import (
    count_items, sum_numbers, find_largest, count_even_numbers, sum_digits,
    count_vowels, multiply_list_elements, create_number_triangle,
    fibonacci_sequence, remove_vowels, create_multiplication_table,
    count_character_frequency, reverse_words, spiral_matrix, pascal_triangle,
    longest_common_subsequence, count_inversions, create_hollow_square,
    create_diamond, create_hourglass, create_spiral_string,
    create_alphabet_diamond, create_number_spiral, create_pyramid,
    create_number_pyramid,
)


class TestLoopsAndShapes(unittest.TestCase):

    # ------------------------------------------------------------------
    # Original tests
    # ------------------------------------------------------------------
    def test_count_items(self):
        self.assertEqual(count_items([1, 2, 3, 4, 5]), 5)
        self.assertEqual(count_items([]), 0)
        self.assertEqual(count_items(['a', 'b', 'c']), 3)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([-1, 0, 1]), 0)

    def test_find_largest(self):
        self.assertEqual(find_largest([1, 5, 3, 9, 2]), 9)
        self.assertEqual(find_largest([-5, -2, -10]), -2)
        self.assertEqual(find_largest([0]), 0)

    def test_count_even_numbers(self):
        self.assertEqual(count_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(count_even_numbers([1, 3, 5, 7, 9]), 0)
        self.assertEqual(count_even_numbers([2, 4, 6, 8]), 4)

    def test_sum_digits(self):
        self.assertEqual(sum_digits(123), 6)
        self.assertEqual(sum_digits(9999), 36)
        self.assertEqual(sum_digits(1000000), 1)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("AEIOU"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_multiply_list_elements(self):
        self.assertEqual(multiply_list_elements([1, 2, 3, 4]), 24)
        self.assertEqual(multiply_list_elements([2, 2, 2]), 8)
        self.assertEqual(multiply_list_elements([1, 0, 5]), 0)

    def test_create_number_triangle(self):
        self.assertEqual(create_number_triangle(3), ['1', '22', '333'])
        self.assertEqual(create_number_triangle(5), ['1', '22', '333', '4444', '55555'])
        self.assertEqual(create_number_triangle(1), ['1'])

    def test_fibonacci_sequence(self):
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci_sequence(2), [0, 1])

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("hello world"), "hll wrld")
        self.assertEqual(remove_vowels("AEIOU"), "")
        self.assertEqual(remove_vowels("rhythm"), "rhythm")

    def test_create_multiplication_table(self):
        expected = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        self.assertEqual(create_multiplication_table(3), expected)

    def test_count_character_frequency(self):
        self.assertEqual(count_character_frequency("hello"), {'h': 1, 'e': 1, 'l': 2, 'o': 1})
        self.assertEqual(count_character_frequency("aabbcc"), {'a': 2, 'b': 2, 'c': 2})

    def test_reverse_words(self):
        self.assertEqual(reverse_words("hello world"), "olleh dlrow")
        self.assertEqual(reverse_words("Python is awesome"), "nohtyP si emosewa")

    def test_spiral_matrix(self):
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(spiral_matrix(3), expected)

    def test_pascal_triangle(self):
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        self.assertEqual(pascal_triangle(5), expected)

    def test_longest_common_subsequence(self):
        self.assertEqual(longest_common_subsequence("ABCDGH", "AEDFHR"), 3)
        self.assertEqual(longest_common_subsequence("AGGTAB", "GXTXAYB"), 4)

    def test_count_inversions(self):
        self.assertEqual(count_inversions([1, 20, 6, 4, 5]), 5)
        self.assertEqual(count_inversions([1, 2, 3, 4, 5]), 0)

    def test_create_hollow_square(self):
        expected = ['***', '* *', '***']
        self.assertEqual(create_hollow_square(3), expected)

    def test_create_diamond(self):
        expected = [' * ', '***', ' * ']
        self.assertEqual(create_diamond(3), expected)

    def test_create_hourglass(self):
        expected = ['*****', ' *** ', '  *  ', ' *** ', '*****']
        self.assertEqual(create_hourglass(5), expected)

    def test_create_spiral_string(self):
        expected = "123\n894\n765"
        self.assertEqual(create_spiral_string(3), expected)

    def test_create_alphabet_diamond(self):
        expected = ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
        self.assertEqual(create_alphabet_diamond(3), expected)

    def test_create_number_spiral(self):
        expected = ['123', '894', '765']
        self.assertEqual(create_number_spiral(3), expected)

    def test_create_pyramid(self):
        expected = ['  *  ', ' *** ', '*****']
        self.assertEqual(create_pyramid(3), expected)
        expected = ['   *   ', '  ***  ', ' ***** ', '*******']
        self.assertEqual(create_pyramid(4), expected)

    def test_create_number_pyramid(self):
        expected = ['  1  ', ' 2 2 ', '3 3 3']
        self.assertEqual(create_number_pyramid(3), expected)
        expected = ['   1   ', '  2 2  ', ' 3 3 3 ', '4 4 4 4']
        self.assertEqual(create_number_pyramid(4), expected)

    # ------------------------------------------------------------------
    # Added edge-case tests
    # ------------------------------------------------------------------
    def test_count_items_edge_cases(self):
        self.assertEqual(count_items([None, None]), 2)
        self.assertEqual(count_items([[1, 2], [3]]), 2)  # nested lists count as one item each
        self.assertEqual(count_items(["x"] * 1000), 1000)

    def test_sum_numbers_edge_cases(self):
        self.assertEqual(sum_numbers([7]), 7)
        self.assertAlmostEqual(sum_numbers([0.5, 1.5, 0.25]), 2.25)
        self.assertEqual(sum_numbers([-3, -4]), -7)

    def test_find_largest_edge_cases(self):
        self.assertEqual(find_largest([7, 7, 7]), 7)
        self.assertEqual(find_largest([-1.5, -0.5, -2.5]), -0.5)
        self.assertEqual(find_largest([9, 1, 2, 3]), 9)   # largest first
        self.assertEqual(find_largest([1, 2, 3, 9]), 9)   # largest last

    def test_count_even_numbers_edge_cases(self):
        self.assertEqual(count_even_numbers([]), 0)
        self.assertEqual(count_even_numbers([0]), 1)              # zero is even
        self.assertEqual(count_even_numbers([-2, -3, -4]), 2)     # negatives work

    def test_sum_digits_edge_cases(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(7), 7)
        self.assertEqual(sum_digits(98765), 35)

    def test_count_vowels_edge_cases(self):
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("PyThOn"), 1)                # y is not a vowel
        self.assertEqual(count_vowels("Hello, World! 123"), 3)     # punctuation/digits ignored
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_multiply_list_elements_edge_cases(self):
        self.assertEqual(multiply_list_elements([]), 1)            # empty product
        self.assertEqual(multiply_list_elements([7]), 7)
        self.assertEqual(multiply_list_elements([-1, 2, -3]), 6)
        self.assertEqual(multiply_list_elements([-2, 3]), -6)

    def test_create_number_triangle_edge_cases(self):
        self.assertEqual(create_number_triangle(0), [])
        self.assertEqual(create_number_triangle(2), ['1', '22'])
        self.assertEqual(create_number_triangle(9)[-1], '9' * 9)

    def test_fibonacci_sequence_edge_cases(self):
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence(1), [0])
        result = fibonacci_sequence(10)
        self.assertEqual(len(result), 10)
        self.assertEqual(result[-1], 34)

    def test_remove_vowels_edge_cases(self):
        self.assertEqual(remove_vowels(""), "")
        self.assertEqual(remove_vowels("Hello, World!"), "Hll, Wrld!")  # keeps case, spaces, punctuation
        self.assertEqual(remove_vowels("aaa"), "")

    def test_create_multiplication_table_edge_cases(self):
        self.assertEqual(create_multiplication_table(1), [[1]])
        self.assertEqual(create_multiplication_table(0), [])
        self.assertEqual(
            create_multiplication_table(4),
            [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]],
        )

    def test_count_character_frequency_edge_cases(self):
        self.assertEqual(count_character_frequency(""), {})
        self.assertEqual(count_character_frequency("aA "), {'a': 1, 'A': 1, ' ': 1})  # case-sensitive
        self.assertEqual(count_character_frequency("a1a1!"), {'a': 2, '1': 2, '!': 1})

    def test_reverse_words_edge_cases(self):
        self.assertEqual(reverse_words(""), "")
        self.assertEqual(reverse_words("abc"), "cba")
        self.assertEqual(reverse_words("a"), "a")
        self.assertEqual(reverse_words("madam level"), "madam level")  # palindromic words unchanged

    def test_spiral_matrix_edge_cases(self):
        self.assertEqual(spiral_matrix(1), [[1]])
        self.assertEqual(spiral_matrix(2), [[1, 2], [4, 3]])
        self.assertEqual(
            spiral_matrix(4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]],
        )

    def test_pascal_triangle_edge_cases(self):
        self.assertEqual(pascal_triangle(0), [])
        self.assertEqual(pascal_triangle(1), [[1]])
        self.assertEqual(pascal_triangle(2), [[1], [1, 1]])
        self.assertEqual(pascal_triangle(6)[-1], [1, 5, 10, 10, 5, 1])

    def test_longest_common_subsequence_edge_cases(self):
        self.assertEqual(longest_common_subsequence("", "abc"), 0)
        self.assertEqual(longest_common_subsequence("abc", ""), 0)
        self.assertEqual(longest_common_subsequence("abc", "abc"), 3)   # identical
        self.assertEqual(longest_common_subsequence("abc", "xyz"), 0)   # nothing in common
        self.assertEqual(longest_common_subsequence("abc", "cba"), 1)
        self.assertEqual(
            longest_common_subsequence("AGGTAB", "GXTXAYB"),
            longest_common_subsequence("GXTXAYB", "AGGTAB"),            # symmetric
        )

    def test_count_inversions_edge_cases(self):
        self.assertEqual(count_inversions([]), 0)
        self.assertEqual(count_inversions([42]), 0)
        self.assertEqual(count_inversions([5, 4, 3, 2, 1]), 10)         # worst case: n(n-1)/2
        self.assertEqual(count_inversions([2, 2, 2]), 0)                # equal values are not inversions
        self.assertEqual(count_inversions([2, 1]), 1)

    def test_create_hollow_square_edge_cases(self):
        self.assertEqual(create_hollow_square(1), ['*'])
        self.assertEqual(create_hollow_square(2), ['**', '**'])
        self.assertEqual(
            create_hollow_square(5),
            ['*****', '*   *', '*   *', '*   *', '*****'],
        )

    def test_create_diamond_edge_cases(self):
        self.assertEqual(create_diamond(1), ['*'])
        self.assertEqual(
            create_diamond(5),
            ['  *  ', ' *** ', '*****', ' *** ', '  *  '],
        )

    def test_create_hourglass_edge_cases(self):
        self.assertEqual(create_hourglass(1), ['*'])
        self.assertEqual(create_hourglass(3), ['***', ' * ', '***'])

    def test_create_spiral_string_edge_cases(self):
        self.assertEqual(create_spiral_string(1), "1")
        self.assertEqual(create_spiral_string(2), "12\n43")

    def test_create_alphabet_diamond_edge_cases(self):
        self.assertEqual(create_alphabet_diamond(1), ['A'])
        self.assertEqual(create_alphabet_diamond(2), [' A ', 'B B', ' A '])
        self.assertEqual(
            create_alphabet_diamond(4),
            ['   A   ', '  B B  ', ' C   C ', 'D     D', ' C   C ', '  B B  ', '   A   '],
        )

    def test_create_number_spiral_edge_cases(self):
        self.assertEqual(create_number_spiral(1), ['1'])
        self.assertEqual(create_number_spiral(2), ['12', '43'])

    def test_create_pyramid_edge_cases(self):
        self.assertEqual(create_pyramid(1), ['*'])
        self.assertEqual(create_pyramid(2), [' * ', '***'])
        self.assertTrue(all(len(row) == 2 * 6 - 1 for row in create_pyramid(6)))  # constant width

    def test_create_number_pyramid_edge_cases(self):
        self.assertEqual(create_number_pyramid(1), ['1'])
        self.assertEqual(create_number_pyramid(2), [' 1 ', '2 2'])
        self.assertTrue(all(len(row) == 2 * 5 - 1 for row in create_number_pyramid(5)))


if __name__ == '__main__':
    unittest.main()
