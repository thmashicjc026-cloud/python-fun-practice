# 🐍 Python Practice Questions

A single, tidy project that combines four sets of Python practice exercises. Every function is an empty stub (`pass`) — **your job is to implement them until the tests go green.**

| | |
|---|---|
| **Questions** | 61 functions to implement |
| **Tests** | 130 automated tests (71 original + 59 added edge-case tests) |
| **Topics** | loops, strings, lists, dictionaries, sorting, recursion-free algorithms, text shapes, classes |
| **Requires** | Python 3.8+ (pytest optional) |

---

## 🚀 Quick start

```bash
# 1. (optional) create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. (optional) install pytest for nicer output
pip install -r requirements.txt

# 3. see where you stand
python progress.py
```

Example output on a fresh checkout:

```
   Revise Me        [░░░░░░░░░░░░░░░░░░░░]   0/14
   Code Pairing     [░░░░░░░░░░░░░░░░░░░░]   0/36
   Strings & Dicts  [█░░░░░░░░░░░░░░░░░░░]   1/30
   Loops & Shapes   [░░░░░░░░░░░░░░░░░░░░]   0/50

   Total: 1/130 tests passing (0%)
```

(A couple of tests pass by accident on empty stubs — e.g. `assertFalse(None)`. They'll keep passing once you've implemented things properly.)

## 🔁 How to work

1. Pick a section from the table below and open its file in `practice/`.
2. Read the docstring of a function — it has the rules and examples.
3. Replace `pass` with your solution.
4. Run that section's tests and fix whatever fails.
5. Repeat. Run `python progress.py -v` any time to list the tests still failing.

> **Don't edit the tests to make them pass** — they're the spec. (Adding your own extra tests is encouraged!)

## 🧪 Running the tests

```bash
pytest                                        # everything
pytest tests/test_revise_me.py                # one section
pytest tests/test_revise_me.py -k minimum     # one function
pytest -x                                     # stop at the first failure

# No pytest? The standard library works too:
python -m unittest                            # everything
python -m unittest tests.test_code_pairing    # one section
```

---

## 🗂 Project layout

```
python-practice/
├── practice/                    ← YOUR CODE GOES HERE
│   ├── revise_me.py             8 warm-up functions
│   ├── code_pairing.py          18 methods on a ProblemSolver class
│   ├── strings_and_dicts.py     9 functions with input validation
│   └── loops_and_shapes.py      25 functions: loops, algorithms, ASCII shapes
├── tests/
│   ├── test_revise_me.py
│   ├── test_code_pairing.py
│   ├── test_strings_and_dicts.py
│   └── test_loops_and_shapes.py
├── progress.py                  scoreboard across all sections
├── pyproject.toml               pytest config
└── requirements.txt
```

## 📚 The sections

Suggested order is easiest → hardest.

### 1. Revise Me — `practice/revise_me.py` · *beginner*
Lists, dictionaries, strings and printing.

`find_minimum` · `calculate_factorial` (iterative) · `unique_elements` · `find_number_of_even_numbers` · `generate_squared_dict` · `convert_to_word_list` · `letters_count_map` · `draw_square`

### 2. Code Pairing — `practice/code_pairing.py` · *beginner → advanced*
Written for pair programming (one drives, one reviews). Eighteen methods on the `ProblemSolver` class.

| Level | Methods |
|---|---|
| Basic | `sum_even_numbers` · `count_vowels` · `reverse_string` · `is_positive` · `find_max` · `count_occurrences` |
| Intermediate | `longest_word` · `is_palindrome` · `remove_duplicates` · `factorial` · `capitalize_words` · `sum_of_squares` |
| Advanced | `find_pairs_with_sum` · `max_subarray_sum` · `rotate_list` · `is_valid_parentheses` · `merge_sorted_lists` · `fibonacci_up_to` |

Hints worth knowing: Kadane's algorithm for `max_subarray_sum`, a stack for `is_valid_parentheses`, two pointers for `merge_sorted_lists`.

### 3. Strings & Dicts — `practice/strings_and_dicts.py` · *intermediate*
Nine functions that also **validate their input** and raise `TypeError` with an exact message (the tests check the text).

`reverse_cases` · `is_anagram` · `find_anagram_groups` · `dict_keys_to_sorted_list` · `merge_dictionaries` · `count_vowels` · `remove_vowels` · `is_prime` · `custom_sort`

### 4. Loops & Shapes — `practice/loops_and_shapes.py` · *beginner → hard*
Twenty-five functions in four groups.

| Group | Functions |
|---|---|
| Counting & basics | `count_items` · `sum_numbers` · `find_largest` · `count_even_numbers` · `sum_digits` · `count_vowels` · `multiply_list_elements` |
| Strings & sequences | `create_number_triangle` · `fibonacci_sequence` · `remove_vowels` · `create_multiplication_table` · `count_character_frequency` · `reverse_words` |
| Algorithms | `spiral_matrix` · `pascal_triangle` · `longest_common_subsequence` · `count_inversions` |
| Shapes | `create_hollow_square` · `create_diamond` · `create_hourglass` · `create_spiral_string` · `create_alphabet_diamond` · `create_number_spiral` · `create_pyramid` · `create_number_pyramid` |

Shape functions return a list of equal-width strings, top to bottom, so you can preview one with:

```python
from practice.loops_and_shapes import create_alphabet_diamond
print("\n".join(create_alphabet_diamond(4)))
```

---

## 📝 What changed when the projects were merged

The questions are the same as in the originals. These are the differences:

**Added tests (59).** Every function now has edge-case tests on top of the original ones — empty inputs, single elements, negatives, duplicates, "input must not be modified", boundary values, and so on. Added tests are in a clearly marked section at the bottom of each test file (`test_<name>_extra` / `_edge_cases`). `convert_to_word_list` previously had **no** tests at all.

**Fixed name clash.** `loopsTest` defined `create_number_triangle` twice (the later definition silently replaced the earlier one, in both the code and the tests). The second one — the centred, space-separated version — is now `create_number_pyramid`.

**Docstrings now match the tests.** In a few places the original docstring or README disagreed with the tests, and the tests won:

| Function | Original docs said | Tests (and docs now) require |
|---|---|---|
| `sum_even_numbers` | sum of all even numbers | only **positive** even numbers |
| `longest_word` | first word on ties | **last** word on ties |
| `generate_squared_dict` | 1…n | also handles `0` and negatives |
| `letters_count_map` | "count of each letter" | all 26 letters, lowercase, case-insensitive |
| `strings_and_dicts.*` | nothing about errors | specific `TypeError` messages |

**Small spec additions** (so the new tests have something to stand on): `calculate_factorial` raises `ValueError` for negatives (as `ProblemSolver.factorial` already did), `multiply_list_elements([])` is `1`, and `find_anagram_groups` / `custom_sort` reject lists containing non-strings.

**Housekeeping.** Removed two duplicated stubs in `Code Pairing`, restructured the four loose folders into one package (no more `from main import *`), switched the stdout test to `contextlib.redirect_stdout` (the original left `sys.stdout` hijacked for every test after it), and dropped the nested `.git`, `.pytest_cache` and `.vscode` folders.

## 💡 Tips

- Prefer clarity over cleverness first; refactor once the tests pass.
- Read the *failure message* — it shows both the expected and the actual value.
- Try a function in the REPL before running the tests: `python -c "from practice.revise_me import find_minimum; print(find_minimum([3, 1, 2]))"`.
- Stuck on a shape? Draw the expected output for `n = 1, 2, 3` on paper and look for the pattern in the number of spaces and symbols per row.
- Once you're done, try the extras: add your own tests, solve the problems *without* built-ins (`sum`, `max`, `sorted`), or re-solve them recursively.

Happy coding! 🎉
