"""
Strings, Dicts & Sorting  (Python Programming Assessment)
=========================================================

Nine functions on strings, dictionaries, anagrams, primes and sorting.
Each function validates its input and raises ``TypeError`` with the exact
message shown in its docstring -- the tests check the messages.

Run just this section:
    pytest tests/test_strings_and_dicts.py -v
"""

from typing import Dict, List


def reverse_cases(sentence: str) -> str:
    """
    Reverse the case of the sentence.
    If the sentence contains anything other than letters and spaces, also reverse the string.

    Raises:
        TypeError("Sentence must be a string.") if ``sentence`` is not a str.

    Example:
        "Hello"          -> "hELLO"
        "12345"          -> "54321"
        "Coding is Fun!" -> "!NUf SI GNIDOc"
        "Group42"        -> "24PUORg"
    """
    pass


def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams (ignoring case and spaces).

    Raises:
        TypeError("Both inputs must be strings.") if either input is not a str.

    Example:
        is_anagram("listen", "silent") -> True
        is_anagram("hello", "world")   -> False
    """
    pass


def find_anagram_groups(words: List[str]) -> List[List[str]]:
    """
    Group words that are anagrams of each other.
    Groups appear in the order their first word appears in ``words``.

    Raises:
        TypeError("Input must be a list of strings.") if ``words`` is not a list
        or contains something that is not a str.

    Example:
        ["eat", "tea", "tan", "ate", "nat", "bat"]
            -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    pass


def dict_keys_to_sorted_list(d: Dict) -> List[str]:
    """
    Convert dictionary keys to a sorted list.

    Raises:
        TypeError("Input must be a dictionary.") if ``d`` is not a dict.

    Example:
        {"z": 1, "a": 2, "b": 3} -> ["a", "b", "z"]
    """
    pass


def merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict:
    """
    Merge two dictionaries into a new one. If keys overlap, sum their values.
    The input dictionaries must not be modified.

    Raises:
        TypeError("Both inputs must be dictionaries.") if either input is not a dict.

    Example:
        {"a": 1, "b": 2}, {"b": 3, "c": 4} -> {"a": 1, "b": 5, "c": 4}
    """
    pass


def count_vowels(s: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a string (case-insensitive).

    Raises:
        TypeError("Input must be a string.") if ``s`` is not a str.

    Example:
        "Hello World" -> 3
    """
    pass


def remove_vowels(s: str) -> str:
    """
    Remove all vowels from a string (case-insensitive).

    Raises:
        TypeError("Input must be a string.") if ``s`` is not a str.

    Example:
        "programming" -> "prgrmmng"
    """
    pass


def is_prime(n: int) -> bool:
    """
    Check if a number is prime. Numbers below 2 are not prime.

    Raises:
        TypeError("Input must be an integer.") if ``n`` is not an int.

    Example:
        7  -> True
        10 -> False
    """
    pass


def custom_sort(words: List[str]) -> List[str]:
    """
    Sort a list of strings by length first, then lexicographically.
    Returns a new list; the input list must not be modified.

    Raises:
        TypeError("Input must be a list of strings.") if ``words`` is not a list
        or contains something that is not a str.

    Example:
        ["banana", "apple", "cherry", "date"] -> ["date", "apple", "banana", "cherry"]
    """
    pass
