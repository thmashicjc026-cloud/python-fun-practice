"""
Tests for practice/strings_and_dicts.py

The original assessment tests are kept as-is; extra edge-case tests were added
at the bottom of the class.
"""

import unittest

from practice.strings_and_dicts import (
    reverse_cases,
    is_anagram,
    find_anagram_groups,
    dict_keys_to_sorted_list,
    merge_dictionaries,
    count_vowels,
    remove_vowels,
    is_prime,
    custom_sort,
)


class TestPythonAssessment(unittest.TestCase):

    # ---------- reverse_cases ----------
    def test_reverse_cases(self):
        self.assertEqual(reverse_cases("Hello"), "hELLO")
        self.assertNotEqual(reverse_cases("Hello"), "OLLEh")
        self.assertEqual(reverse_cases("Coding is Fun"), "cODING IS fUN")
        self.assertEqual(reverse_cases("Coding is Fun!"), "!NUf SI GNIDOc")
        self.assertNotEqual(reverse_cases("Coding is Fun!"), "cODING IS fUN!")
        self.assertEqual(reverse_cases("12345"), "54321")
        self.assertEqual(reverse_cases("Group42"), "24PUORg")
        with self.assertRaisesRegex(TypeError, "Sentence must be a string."):
            reverse_cases(100)

    # ---------- is_anagram ----------
    def test_is_anagram_true(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Dormitory", "dirty room"))
        self.assertTrue(is_anagram("The eyes", "They see"))

    def test_is_anagram_false(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))

    def test_is_anagram_edge_cases(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("a", "b"))
        with self.assertRaisesRegex(TypeError, "Both inputs must be strings."):
            is_anagram("hello", 123)

    # ---------- find_anagram_groups ----------
    def test_find_anagram_groups_basic(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = find_anagram_groups(words)
        # Convert to sets for order-insensitive comparison inside each group
        self.assertEqual([set(g) for g in result], [set(g) for g in expected])

    def test_find_anagram_groups_single(self):
        self.assertEqual(find_anagram_groups(["hello"]), [["hello"]])

    def test_find_anagram_groups_empty(self):
        self.assertEqual(find_anagram_groups([]), [])
        with self.assertRaisesRegex(TypeError, "Input must be a list of strings."):
            find_anagram_groups("not a list")

    # ---------- dict_keys_to_sorted_list ----------
    def test_dict_keys_to_sorted_list(self):
        d = {"z": 1, "a": 2, "b": 3}
        self.assertEqual(dict_keys_to_sorted_list(d), ["a", "b", "z"])

    def test_dict_keys_to_sorted_list_empty(self):
        self.assertEqual(dict_keys_to_sorted_list({}), [])
        with self.assertRaisesRegex(TypeError, "Input must be a dictionary."):
            dict_keys_to_sorted_list("not a dict")

    # ---------- merge_dictionaries ----------
    def test_merge_dictionaries_overlap(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        expected = {"a": 1, "b": 5, "c": 4}
        self.assertEqual(merge_dictionaries(dict1, dict2), expected)

    def test_merge_dictionaries_no_overlap(self):
        dict1 = {"x": 10}
        dict2 = {"y": 20}
        self.assertEqual(merge_dictionaries(dict1, dict2), {"x": 10, "y": 20})

    def test_merge_dictionaries_empty(self):
        self.assertEqual(merge_dictionaries({}, {}), {})
        with self.assertRaisesRegex(TypeError, "Both inputs must be dictionaries."):
            merge_dictionaries("not a dict", {"b": 2})

    # ---------- count_vowels ----------
    def test_count_vowels_basic(self):
        self.assertEqual(count_vowels("Hello World"), 3)
        self.assertEqual(count_vowels("AEIOUaeiou"), 10)

    def test_count_vowels_no_vowels(self):
        self.assertEqual(count_vowels("rhythm"), 0)
        with self.assertRaisesRegex(TypeError, "Input must be a string."):
            count_vowels(123)

    # ---------- remove_vowels ----------
    def test_remove_vowels_basic(self):
        self.assertEqual(remove_vowels("programming"), "prgrmmng")
        self.assertEqual(remove_vowels("AEIOUaeiou"), "")

    def test_remove_vowels_no_vowels(self):
        self.assertEqual(remove_vowels("xyz"), "xyz")
        with self.assertRaisesRegex(TypeError, "Input must be a string."):
            remove_vowels(123)

    # ---------- is_prime ----------
    def test_is_prime_true(self):
        for n in [2, 3, 5, 7, 11, 13, 17]:
            self.assertTrue(is_prime(n))

    def test_is_prime_false(self):
        for n in [0, 1, 4, 6, 8, 9, 10, 12]:
            self.assertFalse(is_prime(n))
        with self.assertRaisesRegex(TypeError, "Input must be an integer."):
            is_prime("10")

    # ---------- custom_sort ----------
    def test_custom_sort_basic(self):
        words = ["banana", "apple", "cherry", "date"]
        expected = ["date", "apple", "banana", "cherry"]
        self.assertEqual(custom_sort(words), expected)

    def test_custom_sort_same_length(self):
        words = ["dog", "bat", "ant"]
        expected = ["ant", "bat", "dog"]
        self.assertEqual(custom_sort(words), expected)

    def test_custom_sort_empty(self):
        self.assertEqual(custom_sort([]), [])
        with self.assertRaisesRegex(TypeError, "Input must be a list of strings."):
            custom_sort("not a list")

    # ==================================================================
    # Added edge-case tests
    # ==================================================================
    def test_reverse_cases_extra(self):
        self.assertEqual(reverse_cases(""), "")
        self.assertEqual(reverse_cases("ABC def"), "abc DEF")        # letters + space: only swap case
        self.assertEqual(reverse_cases("a1"), "1A")                  # contains digit: swap + reverse
        self.assertEqual(reverse_cases("!!"), "!!")
        self.assertEqual(reverse_cases("Hello World"), "hELLO wORLD")
        for bad in (None, 3.14, ["a"]):
            with self.assertRaisesRegex(TypeError, "Sentence must be a string."):
                reverse_cases(bad)

    def test_is_anagram_extra(self):
        self.assertTrue(is_anagram("Listen", "SILENT"))              # case-insensitive
        self.assertTrue(is_anagram("a b c", "cba"))                  # spaces ignored
        self.assertFalse(is_anagram("abc", "abcd"))                  # different length
        self.assertFalse(is_anagram("aab", "abb"))                   # same letters, different counts
        self.assertTrue(is_anagram("night", "thing"))
        with self.assertRaisesRegex(TypeError, "Both inputs must be strings."):
            is_anagram(123, "abc")
        with self.assertRaisesRegex(TypeError, "Both inputs must be strings."):
            is_anagram("abc", None)

    def test_find_anagram_groups_extra(self):
        # every word on its own, order preserved
        self.assertEqual(find_anagram_groups(["abc", "def", "ghi"]), [["abc"], ["def"], ["ghi"]])
        # everything is an anagram of everything else -> one group
        result = find_anagram_groups(["abc", "bca", "cab"])
        self.assertEqual(len(result), 1)
        self.assertEqual(set(result[0]), {"abc", "bca", "cab"})
        # groups are ordered by first appearance
        result = find_anagram_groups(["bat", "tab", "cat", "act", "bat"])
        self.assertEqual(sorted(len(g) for g in result), [2, 3])
        self.assertIn("bat", result[0])
        self.assertIn("cat", result[1])
        # the input is not modified
        words = ["eat", "tea"]
        find_anagram_groups(words)
        self.assertEqual(words, ["eat", "tea"])
        # list must contain only strings
        with self.assertRaisesRegex(TypeError, "Input must be a list of strings."):
            find_anagram_groups(["ok", 5])

    def test_dict_keys_to_sorted_list_extra(self):
        self.assertEqual(dict_keys_to_sorted_list({"only": 1}), ["only"])
        self.assertEqual(dict_keys_to_sorted_list({"b": 1, "B": 2, "a": 3}), ["B", "a", "b"])  # uppercase sorts first
        self.assertEqual(dict_keys_to_sorted_list({"banana": 0, "apple": 0, "cherry": 0}),
                         ["apple", "banana", "cherry"])
        for bad in (None, ["a", "b"], 5):
            with self.assertRaisesRegex(TypeError, "Input must be a dictionary."):
                dict_keys_to_sorted_list(bad)

    def test_merge_dictionaries_extra(self):
        self.assertEqual(merge_dictionaries({"a": 1}, {}), {"a": 1})
        self.assertEqual(merge_dictionaries({}, {"a": 1}), {"a": 1})
        self.assertEqual(merge_dictionaries({"a": 1}, {"a": -1}), {"a": 0})      # cancels to 0, key kept
        self.assertEqual(merge_dictionaries({"a": 1.5}, {"a": 2.5}), {"a": 4.0})
        self.assertEqual(merge_dictionaries({"a": 1, "b": 1}, {"a": 1, "b": 1}), {"a": 2, "b": 2})
        # inputs are not modified
        d1, d2 = {"a": 1, "b": 2}, {"b": 3}
        merge_dictionaries(d1, d2)
        self.assertEqual(d1, {"a": 1, "b": 2})
        self.assertEqual(d2, {"b": 3})
        with self.assertRaisesRegex(TypeError, "Both inputs must be dictionaries."):
            merge_dictionaries({"a": 1}, [("b", 2)])

    def test_count_vowels_extra(self):
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("sky"), 0)                      # y is not a vowel
        self.assertEqual(count_vowels("Why? Because!"), 4)            # punctuation ignored
        self.assertEqual(count_vowels("aaaa"), 4)
        for bad in (None, ["a"], 1.5):
            with self.assertRaisesRegex(TypeError, "Input must be a string."):
                count_vowels(bad)

    def test_remove_vowels_extra(self):
        self.assertEqual(remove_vowels(""), "")
        self.assertEqual(remove_vowels("HELLO"), "HLL")
        self.assertEqual(remove_vowels("Hello, World!"), "Hll, Wrld!")   # keeps case/punctuation/spaces
        self.assertEqual(remove_vowels("a e i o u"), "    ")             # only the vowels go
        for bad in (None, ["a"]):
            with self.assertRaisesRegex(TypeError, "Input must be a string."):
                remove_vowels(bad)

    def test_is_prime_extra(self):
        self.assertTrue(is_prime(97))
        self.assertTrue(is_prime(7919))                               # 1000th prime
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(91))                                # 7 * 13
        self.assertFalse(is_prime(-7))                                # negatives are not prime
        self.assertFalse(is_prime(25))                                # square of a prime
        for bad in (7.0, None, [7]):
            with self.assertRaisesRegex(TypeError, "Input must be an integer."):
                is_prime(bad)

    def test_custom_sort_extra(self):
        self.assertEqual(custom_sort(["b", "a", "c"]), ["a", "b", "c"])
        self.assertEqual(custom_sort(["ccc", "a", "bb", "aa", "b"]), ["a", "b", "aa", "bb", "ccc"])
        self.assertEqual(custom_sort(["a", "a", "aa"]), ["a", "a", "aa"])       # duplicates kept
        self.assertEqual(custom_sort(["x"]), ["x"])
        # a new list is returned; the input is left alone
        words = ["bb", "a"]
        result = custom_sort(words)
        self.assertEqual(words, ["bb", "a"])
        self.assertIsNot(result, words)
        with self.assertRaisesRegex(TypeError, "Input must be a list of strings."):
            custom_sort(["ok", 5])
        with self.assertRaisesRegex(TypeError, "Input must be a list of strings."):
            custom_sort(None)


if __name__ == "__main__":
    unittest.main()
