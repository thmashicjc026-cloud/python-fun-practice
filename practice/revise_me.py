"""
Revise Me
=========

Eight warm-up functions covering lists, dictionaries, strings and printing.

Run just this section:
    pytest tests/test_revise_me.py -v
"""


def find_minimum(numbers: list) -> int:
    """Returns the smallest number in a list. Return None for an empty list.

    Example:
        find_minimum([4, 2, 9, 1]) -> 1
    """
    pass


def calculate_factorial(n: int) -> int:
    """Calculates the factorial of a non-negative integer iteratively (no recursion).

    Raises:
        ValueError if ``n`` is negative.

    Example:
        calculate_factorial(5) -> 120
        calculate_factorial(0) -> 1
    """
    pass


def unique_elements(items: list) -> list:
    """Returns a list of unique elements, maintaining the order of first appearance.

    Example:
        unique_elements([1, 2, 2, 3, 1]) -> [1, 2, 3]
    """
    pass


def find_number_of_even_numbers(numbers: list) -> int:
    """Returns the number of even numbers in a list (0 counts as even).

    Example:
        find_number_of_even_numbers([1, 2, 3, 4]) -> 2
    """
    pass


def generate_squared_dict(n: int) -> dict:
    """Generates a dictionary with the square of every integer from ``n`` towards 0.

    * n > 0  -> keys 1 .. n          (e.g. 3  -> {1: 1, 2: 4, 3: 9})
    * n == 0 -> empty dictionary
    * n < 0  -> keys n .. -1         (e.g. -3 -> {-3: 9, -2: 4, -1: 1})
    """
    pass


def convert_to_word_list(string: str) -> list:
    """Converts a string to a list of words.

    Words are separated by any amount of whitespace; leading/trailing whitespace is
    ignored and punctuation stays attached to its word.

    Example:
        convert_to_word_list("hello  big world") -> ["hello", "big", "world"]
        convert_to_word_list("") -> []
    """
    pass


def letters_count_map(string: str) -> dict:
    """Returns a dictionary with the count of each letter in a string.

    * The result always has all 26 lowercase letters 'a'..'z' as keys (count 0 if absent).
    * Counting is case-insensitive.
    * Digits, spaces and punctuation are ignored.

    Example:
        letters_count_map("Aab")["a"] -> 2
    """
    pass


def draw_square(height: int) -> None:
    """
    Draws a square pattern of asterisks (*) with the given height and width.

    Parameters:
        height (int): The height and width of the square. Must be a positive integer.

    Returns:
        None: Prints the square pattern directly to console, one row per line.

    Example:
        draw_square(2) prints:
            **
            **
    """
    pass
