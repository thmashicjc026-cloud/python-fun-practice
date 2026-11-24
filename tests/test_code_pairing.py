import unittest

from practice.code_pairing import ProblemSolver


class TestProblemSolver(unittest.TestCase):
    def setUp(self):
        self.solver = ProblemSolver()

    # ==================================================================
    # Basic
    # ==================================================================
    def test_sum_even_numbers(self):
        self.assertEqual(self.solver.sum_even_numbers([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(self.solver.sum_even_numbers([]), 0)
        self.assertEqual(self.solver.sum_even_numbers([1, 3, 5]), 0)
        self.assertEqual(self.solver.sum_even_numbers([-2, -4, 3, 6]), 6)

    def test_sum_even_numbers_extra(self):
        self.assertEqual(self.solver.sum_even_numbers([0]), 0)
        self.assertEqual(self.solver.sum_even_numbers([-2, -4, -6]), 0)    # only negatives -> 0
        self.assertEqual(self.solver.sum_even_numbers([2]), 2)
        self.assertEqual(self.solver.sum_even_numbers([100, 200, 301]), 300)

    def test_count_vowels(self):
        self.assertEqual(self.solver.count_vowels("Hello World"), 3)
        self.assertEqual(self.solver.count_vowels("AEIOU"), 5)
        self.assertEqual(self.solver.count_vowels("xyz"), 0)
        self.assertEqual(self.solver.count_vowels(""), 0)

    def test_count_vowels_extra(self):
        self.assertEqual(self.solver.count_vowels("PyThOn"), 1)            # y is not a vowel
        self.assertEqual(self.solver.count_vowels("Why? Because!"), 4)     # punctuation ignored
        self.assertEqual(self.solver.count_vowels("aeiouAEIOU"), 10)
        self.assertEqual(self.solver.count_vowels("12345"), 0)

    def test_reverse_string(self):
        self.assertEqual(self.solver.reverse_string("hello"), "olleh")
        self.assertEqual(self.solver.reverse_string("Python"), "nohtyP")
        self.assertEqual(self.solver.reverse_string(""), "")
        self.assertEqual(self.solver.reverse_string("a"), "a")

    def test_reverse_string_extra(self):
        self.assertEqual(self.solver.reverse_string("racecar"), "racecar")   # palindrome
        self.assertEqual(self.solver.reverse_string("a b c"), "c b a")       # spaces preserved
        self.assertEqual(self.solver.reverse_string("AbC123!"), "!321CbA")   # case and symbols kept

    def test_is_positive(self):
        self.assertTrue(self.solver.is_positive(5))
        self.assertFalse(self.solver.is_positive(0))
        self.assertFalse(self.solver.is_positive(-3))
        self.assertTrue(self.solver.is_positive(1))

    def test_is_positive_extra(self):
        self.assertTrue(self.solver.is_positive(0.5))
        self.assertFalse(self.solver.is_positive(-0.5))
        self.assertFalse(self.solver.is_positive(-1))
        self.assertTrue(self.solver.is_positive(10 ** 12))

    def test_find_max(self):
        self.assertEqual(self.solver.find_max([1, 5, 3, 9, 2]), 9)
        self.assertEqual(self.solver.find_max([1]), 1)
        self.assertIsNone(self.solver.find_max([]))
        self.assertEqual(self.solver.find_max([-1, -5, -2]), -1)

    def test_find_max_extra(self):
        self.assertEqual(self.solver.find_max([4, 4, 4]), 4)
        self.assertEqual(self.solver.find_max([9, 1, 2]), 9)                 # max first
        self.assertEqual(self.solver.find_max([1, 2, 9]), 9)                 # max last
        self.assertEqual(self.solver.find_max([0, -1]), 0)                   # 0 is a real answer
        self.assertEqual(self.solver.find_max([1.5, 2.5, 0.5]), 2.5)

    def test_count_occurrences(self):
        self.assertEqual(self.solver.count_occurrences("banana", "a"), 3)
        self.assertEqual(self.solver.count_occurrences("hello", "l"), 2)
        self.assertEqual(self.solver.count_occurrences("test", "z"), 0)
        self.assertEqual(self.solver.count_occurrences("", "a"), 0)

    def test_count_occurrences_extra(self):
        self.assertEqual(self.solver.count_occurrences("Banana", "A"), 0)    # case-sensitive
        self.assertEqual(self.solver.count_occurrences("Banana", "B"), 1)
        self.assertEqual(self.solver.count_occurrences("aaa", "a"), 3)       # adjacent matches
        self.assertEqual(self.solver.count_occurrences("a b c", " "), 2)     # spaces are characters too

    # ==================================================================
    # Intermediate
    # ==================================================================
    def test_longest_word(self):
        self.assertEqual(self.solver.longest_word("The quick brown fox jumps."), "jumps")
        self.assertEqual(self.solver.longest_word(""), "")
        self.assertEqual(self.solver.longest_word("Hello, world!!"), "world")
        self.assertEqual(self.solver.longest_word("cat dog fox"), "fox")

    def test_longest_word_extra(self):
        self.assertEqual(self.solver.longest_word("Hello"), "Hello")
        self.assertEqual(self.solver.longest_word("a bb ccc"), "ccc")
        self.assertEqual(self.solver.longest_word("elephant is big"), "elephant")   # longest first
        self.assertEqual(self.solver.longest_word("!!! ???"), "")                   # only punctuation
        self.assertEqual(self.solver.longest_word("Wow, amazing!"), "amazing")      # punctuation not counted

    def test_is_palindrome(self):
        self.assertTrue(self.solver.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(self.solver.is_palindrome("race a car"))
        self.assertTrue(self.solver.is_palindrome(""))
        self.assertTrue(self.solver.is_palindrome("a"))

    def test_is_palindrome_extra(self):
        self.assertTrue(self.solver.is_palindrome("No 'x' in Nixon"))
        self.assertTrue(self.solver.is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(self.solver.is_palindrome("12321"))
        self.assertFalse(self.solver.is_palindrome("12345"))
        self.assertTrue(self.solver.is_palindrome("!!!"))                    # nothing left after cleaning
        self.assertFalse(self.solver.is_palindrome("ab"))
        self.assertTrue(self.solver.is_palindrome("Aa"))                     # case ignored

    def test_remove_duplicates(self):
        self.assertEqual(self.solver.remove_duplicates([1, 2, 2, 3, 1, 4]), [1, 2, 3, 4])
        self.assertEqual(self.solver.remove_duplicates([]), [])
        self.assertEqual(self.solver.remove_duplicates([1, 1, 1]), [1])
        self.assertEqual(self.solver.remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_remove_duplicates_extra(self):
        self.assertEqual(self.solver.remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])   # first appearance wins
        self.assertEqual(self.solver.remove_duplicates([-1, -1, 0, 0]), [-1, 0])
        self.assertEqual(self.solver.remove_duplicates([5]), [5])
        original = [1, 1, 2]
        self.solver.remove_duplicates(original)
        self.assertEqual(original, [1, 1, 2])                                         # input untouched

    def test_factorial(self):
        self.assertEqual(self.solver.factorial(5), 120)
        self.assertEqual(self.solver.factorial(0), 1)
        self.assertEqual(self.solver.factorial(1), 1)
        with self.assertRaises(ValueError):
            self.solver.factorial(-1)

    def test_factorial_extra(self):
        self.assertEqual(self.solver.factorial(2), 2)
        self.assertEqual(self.solver.factorial(10), 3628800)
        self.assertEqual(self.solver.factorial(20), 2432902008176640000)
        with self.assertRaises(ValueError):
            self.solver.factorial(-100)

    def test_capitalize_words(self):
        self.assertEqual(self.solver.capitalize_words("hello world"), "Hello World")
        self.assertEqual(self.solver.capitalize_words("the quick fox"), "The Quick Fox")
        self.assertEqual(self.solver.capitalize_words(""), "")
        self.assertEqual(self.solver.capitalize_words("a"), "A")

    def test_capitalize_words_extra(self):
        self.assertEqual(self.solver.capitalize_words("Hello World"), "Hello World")   # already capitalised
        self.assertEqual(self.solver.capitalize_words("hELLO wORLD"), "Hello World")   # rest is lower-cased
        self.assertEqual(self.solver.capitalize_words("single"), "Single")
        self.assertEqual(self.solver.capitalize_words("one two three four"), "One Two Three Four")

    def test_sum_of_squares(self):
        self.assertEqual(self.solver.sum_of_squares([1, 2, 3]), 14)
        self.assertEqual(self.solver.sum_of_squares([]), 0)
        self.assertEqual(self.solver.sum_of_squares([2]), 4)
        self.assertEqual(self.solver.sum_of_squares([-2, 3]), 13)

    def test_sum_of_squares_extra(self):
        self.assertEqual(self.solver.sum_of_squares([0, 0]), 0)
        self.assertEqual(self.solver.sum_of_squares([-1, -2, -3]), 14)       # negatives square to positives
        self.assertEqual(self.solver.sum_of_squares([10]), 100)
        self.assertEqual(self.solver.sum_of_squares([1] * 50), 50)

    # ==================================================================
    # Advanced
    # ==================================================================
    def _assert_valid_pairs(self, numbers, target, expected_count):
        """Helper: pairs must sum to target and no index may be used twice."""
        result = self.solver.find_pairs_with_sum(numbers, target)
        self.assertEqual(len(result), expected_count)
        flat = [i for pair in result for i in pair]
        self.assertEqual(len(flat), len(set(flat)), "an index was used more than once")
        for i, j in result:
            self.assertNotEqual(i, j)
            self.assertEqual(numbers[i] + numbers[j], target)

    def test_find_pairs_with_sum(self):
        self.assertEqual(self.solver.find_pairs_with_sum([2, 7, 11, 15], 9), [(0, 1)])
        self.assertEqual(self.solver.find_pairs_with_sum([1, 2, 3], 10), [])
        result = self.solver.find_pairs_with_sum([1, 4, 3, 2, 5], 7)
        self.assertEqual(len(result), 2)
        flat_indices = [i for pair in result for i in pair]
        self.assertEqual(len(set(flat_indices)), 4)
        nums = [1, 4, 3, 2, 5]
        for i, j in result:
            self.assertEqual(nums[i] + nums[j], 7)
        self.assertEqual(self.solver.find_pairs_with_sum([], 5), [])

    def test_find_pairs_with_sum_extra(self):
        self.assertEqual(self.solver.find_pairs_with_sum([3, 3], 6), [(0, 1)])      # duplicate values
        self.assertEqual(self.solver.find_pairs_with_sum([5], 10), [])              # one element can't pair with itself
        self._assert_valid_pairs([1, 1, 1], 2, 1)                                    # odd one out is left over
        self._assert_valid_pairs([3, 3, 3, 3], 6, 2)                                 # two disjoint pairs
        self._assert_valid_pairs([-1, 1, 0], 0, 1)                                   # negatives / zero target
        self._assert_valid_pairs([0, 0], 0, 1)
        self._assert_valid_pairs([1, 2, 3, 4, 5, 6], 100, 0)

    def test_max_subarray_sum(self):
        self.assertEqual(self.solver.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(self.solver.max_subarray_sum([1]), 1)
        self.assertEqual(self.solver.max_subarray_sum([-1, -2, -3]), -1)
        self.assertEqual(self.solver.max_subarray_sum([]), 0)

    def test_max_subarray_sum_extra(self):
        self.assertEqual(self.solver.max_subarray_sum([1, 2, 3, 4]), 10)            # all positive: whole list
        self.assertEqual(self.solver.max_subarray_sum([5, -9, 6]), 6)               # restart after a big dip
        self.assertEqual(self.solver.max_subarray_sum([0]), 0)
        self.assertEqual(self.solver.max_subarray_sum([-5]), -5)
        self.assertEqual(self.solver.max_subarray_sum([3, -1, 3]), 5)               # bridging a negative is worth it
        self.assertEqual(self.solver.max_subarray_sum([-3, 1, 2]), 3)

    def test_rotate_list(self):
        self.assertEqual(self.solver.rotate_list([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
        self.assertEqual(self.solver.rotate_list([1, 2, 3], 0), [1, 2, 3])
        self.assertEqual(self.solver.rotate_list([1], 5), [1])
        self.assertEqual(self.solver.rotate_list([], 3), [])

    def test_rotate_list_extra(self):
        self.assertEqual(self.solver.rotate_list([1, 2, 3], 3), [1, 2, 3])          # full turn
        self.assertEqual(self.solver.rotate_list([1, 2, 3], 1), [3, 1, 2])
        self.assertEqual(self.solver.rotate_list([1, 2, 3, 4, 5], 7), [4, 5, 1, 2, 3])  # k > len wraps (7 % 5 == 2)
        self.assertEqual(self.solver.rotate_list([1, 2, 3], 300), [1, 2, 3])
        original = [1, 2, 3]
        result = self.solver.rotate_list(original, 1)
        self.assertEqual(original, [1, 2, 3])                                        # input untouched
        self.assertIsNot(result, original)

    def test_is_valid_parentheses(self):
        self.assertTrue(self.solver.is_valid_parentheses("({[]})"))
        self.assertFalse(self.solver.is_valid_parentheses("(]"))
        self.assertTrue(self.solver.is_valid_parentheses(""))
        self.assertFalse(self.solver.is_valid_parentheses("([)]"))

    def test_is_valid_parentheses_extra(self):
        self.assertTrue(self.solver.is_valid_parentheses("()[]{}"))
        self.assertTrue(self.solver.is_valid_parentheses("{[()]}"))
        self.assertFalse(self.solver.is_valid_parentheses("("))                      # never closed
        self.assertFalse(self.solver.is_valid_parentheses(")"))                      # closed before opened
        self.assertFalse(self.solver.is_valid_parentheses(")("))                     # wrong order
        self.assertFalse(self.solver.is_valid_parentheses("((("))
        self.assertFalse(self.solver.is_valid_parentheses("{[}"))
        self.assertFalse(self.solver.is_valid_parentheses("]"))
        self.assertTrue(self.solver.is_valid_parentheses("((()))"))

    def test_merge_sorted_lists(self):
        self.assertEqual(self.solver.merge_sorted_lists([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(self.solver.merge_sorted_lists([], [1, 2]), [1, 2])
        self.assertEqual(self.solver.merge_sorted_lists([1], []), [1])
        self.assertEqual(self.solver.merge_sorted_lists([], []), [])

    def test_merge_sorted_lists_extra(self):
        self.assertEqual(self.solver.merge_sorted_lists([1, 1], [1]), [1, 1, 1])     # duplicates kept
        self.assertEqual(self.solver.merge_sorted_lists([-3, -1], [-2, 0]), [-3, -2, -1, 0])
        self.assertEqual(self.solver.merge_sorted_lists([1, 2, 3], [10, 20]), [1, 2, 3, 10, 20])  # all of one first
        self.assertEqual(self.solver.merge_sorted_lists([10, 20], [1, 2, 3]), [1, 2, 3, 10, 20])
        self.assertEqual(self.solver.merge_sorted_lists([1], [2, 3, 4, 5]), [1, 2, 3, 4, 5])      # uneven lengths
        a, b = [1, 3], [2]
        self.solver.merge_sorted_lists(a, b)
        self.assertEqual((a, b), ([1, 3], [2]))                                      # inputs untouched

    def test_fibonacci_up_to(self):
        self.assertEqual(self.solver.fibonacci_up_to(10), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(self.solver.fibonacci_up_to(1), [0, 1, 1])
        self.assertEqual(self.solver.fibonacci_up_to(0), [0])
        self.assertEqual(self.solver.fibonacci_up_to(-1), [])

    def test_fibonacci_up_to_extra(self):
        self.assertEqual(self.solver.fibonacci_up_to(2), [0, 1, 1, 2])
        self.assertEqual(self.solver.fibonacci_up_to(4), [0, 1, 1, 2, 3])
        self.assertEqual(self.solver.fibonacci_up_to(21), [0, 1, 1, 2, 3, 5, 8, 13, 21])  # n itself is included
        self.assertEqual(self.solver.fibonacci_up_to(20), [0, 1, 1, 2, 3, 5, 8, 13])      # n not a Fibonacci number
        self.assertEqual(self.solver.fibonacci_up_to(-100), [])


if __name__ == "__main__":
    unittest.main()
