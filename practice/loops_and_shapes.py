"""
Loops & Shapes
==============

25 exercises on loops, list/string manipulation, classic algorithms and
text-based shapes.  Implement every function (replace ``pass``) so that
``tests/test_loops_and_shapes.py`` goes green.

Run just this section:
    pytest tests/test_loops_and_shapes.py -v

Sections
    1. Counting & basics        (easy)
    2. Strings & sequences      (medium)
    3. Algorithms               (hard)
    4. Shapes                   (loops + string building)
"""

from typing import Dict, List


# ---------------------------------------------------------------------------
# 1. Counting & basics
# ---------------------------------------------------------------------------

def count_items(items: list) -> int:
    """Return the number of items in the list (without using ``len``).

    Example:
        count_items(['a', 'b', 'c']) -> 3
    """
    pass


def sum_numbers(numbers: List[float]) -> float:
    """Return the sum of all numbers in the list (0 for an empty list).

    Example:
        sum_numbers([1, 2, 3, 4, 5]) -> 15
    """
    pass


def find_largest(numbers: List[float]) -> float:
    """Return the largest number in the (non-empty) list.

    Example:
        find_largest([1, 5, 3, 9, 2]) -> 9
    """
    pass


def count_even_numbers(numbers: List[int]) -> int:
    """Return how many numbers in the list are even (0 counts as even).

    Example:
        count_even_numbers([1, 2, 3, 4, 5, 6]) -> 3
    """
    pass


def sum_digits(number: int) -> int:
    """Return the sum of the digits of a non-negative integer.

    Example:
        sum_digits(123) -> 6
    """
    pass


def count_vowels(string: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the string, ignoring case.

    Example:
        count_vowels("hello world") -> 3
    """
    pass


def multiply_list_elements(numbers: List[float]) -> float:
    """Return the product of all elements in the list.

    The product of an empty list is 1.

    Example:
        multiply_list_elements([1, 2, 3, 4]) -> 24
    """
    pass


# ---------------------------------------------------------------------------
# 2. Strings & sequences
# ---------------------------------------------------------------------------

def create_number_triangle(n: int) -> List[str]:
    """Return a left-aligned triangle where row ``i`` is the digit ``i`` repeated ``i`` times.

    Example:
        create_number_triangle(3) -> ['1', '22', '333']
    """
    pass


def fibonacci_sequence(n: int) -> List[int]:
    """Return the first ``n`` Fibonacci numbers, starting 0, 1, 1, 2, ...

    Example:
        fibonacci_sequence(5) -> [0, 1, 1, 2, 3]
    """
    pass


def remove_vowels(string: str) -> str:
    """Return the string with all vowels (any case) removed.

    Example:
        remove_vowels("hello world") -> "hll wrld"
    """
    pass


def create_multiplication_table(n: int) -> List[List[int]]:
    """Return an n x n multiplication table as a 2D list.

    Example:
        create_multiplication_table(3) -> [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
    """
    pass


def count_character_frequency(string: str) -> Dict[str, int]:
    """Return a dictionary mapping each character to how often it appears.

    Case-sensitive; every character (including spaces) is counted.

    Example:
        count_character_frequency("hello") -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    pass


def reverse_words(sentence: str) -> str:
    """Reverse the letters of each word but keep the word order.

    Example:
        reverse_words("hello world") -> "olleh dlrow"
    """
    pass


# ---------------------------------------------------------------------------
# 3. Algorithms
# ---------------------------------------------------------------------------

def spiral_matrix(n: int) -> List[List[int]]:
    """Return an n x n matrix filled with 1..n^2 in a clockwise spiral.

    Example:
        spiral_matrix(3) -> [[1, 2, 3],
                             [8, 9, 4],
                             [7, 6, 5]]
    """
    pass


def pascal_triangle(n: int) -> List[List[int]]:
    """Return the first ``n`` rows of Pascal's triangle.

    Example:
        pascal_triangle(4) -> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    """
    pass


def longest_common_subsequence(str1: str, str2: str) -> int:
    """Return the *length* of the longest common subsequence of two strings.

    Example:
        longest_common_subsequence("ABCDGH", "AEDFHR") -> 3   # "ADH"
    """
    pass


def count_inversions(arr: List[int]) -> int:
    """Return the number of inversions: pairs (i, j) with i < j and arr[i] > arr[j].

    Example:
        count_inversions([1, 20, 6, 4, 5]) -> 5
    """
    pass


# ---------------------------------------------------------------------------
# 4. Shapes   (every function returns a list of equal-width strings, top to bottom)
# ---------------------------------------------------------------------------

def create_hollow_square(n: int) -> List[str]:
    """Return a hollow square of side ``n`` drawn with ``*``.

    Example:
        create_hollow_square(3) -> ['***', '* *', '***']
    """
    pass


def create_diamond(n: int) -> List[str]:
    """Return a diamond of ``*`` whose widest row has width ``n`` (``n`` is odd).

    Example:
        create_diamond(3) -> [' * ', '***', ' * ']
    """
    pass


def create_hourglass(n: int) -> List[str]:
    """Return an hourglass of ``*`` whose widest rows have width ``n`` (``n`` is odd).

    Example:
        create_hourglass(5) -> ['*****', ' *** ', '  *  ', ' *** ', '*****']
    """
    pass


def create_spiral_string(n: int) -> str:
    """Return the n x n clockwise spiral of 1..n^2 as one string, rows joined by ``\\n``.

    (Tests only use sizes where every number is a single digit.)

    Example:
        create_spiral_string(3) -> "123\\n894\\n765"
    """
    pass


def create_alphabet_diamond(n: int) -> List[str]:
    """Return a diamond built from the first ``n`` letters of the alphabet.

    The diamond has ``2n - 1`` rows and ``2n - 1`` columns.

    Example:
        create_alphabet_diamond(3) -> ['  A  ', ' B B ', 'C   C', ' B B ', '  A  ']
    """
    pass


def create_number_spiral(n: int) -> List[str]:
    """Return the n x n clockwise spiral of 1..n^2 as a list of row strings.

    (Tests only use sizes where every number is a single digit.)

    Example:
        create_number_spiral(3) -> ['123', '894', '765']
    """
    pass


def create_pyramid(n: int) -> List[str]:
    """Return a centred pyramid of ``*`` with ``n`` rows (row widths 1, 3, 5, ...).

    Example:
        create_pyramid(3) -> ['  *  ', ' *** ', '*****']
    """
    pass


def create_number_pyramid(n: int) -> List[str]:
    """Return a centred pyramid where row ``i`` holds the digit ``i`` repeated ``i`` times, space-separated.

    Each row is padded so that all rows have width ``2n - 1``.

    Example:
        create_number_pyramid(3) -> ['  1  ', ' 2 2 ', '3 3 3']
    """
    pass
