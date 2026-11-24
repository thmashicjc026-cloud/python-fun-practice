#!/usr/bin/env python3
"""Show how far through the practice questions you are.

Usage:
    python progress.py            # summary per section
    python progress.py -v         # also list every failing test
"""

import sys
import unittest

SECTIONS = [
    ("Revise Me",          "tests.test_revise_me"),
    ("Code Pairing",       "tests.test_code_pairing"),
    ("Strings & Dicts",    "tests.test_strings_and_dicts"),
    ("Loops & Shapes",     "tests.test_loops_and_shapes"),
]
BAR = 20


def run(module_name):
    suite = unittest.defaultTestLoader.loadTestsFromName(module_name)
    result = unittest.TestResult()
    suite.run(result)
    total = suite.countTestCases()
    # subtest ids look like "mod.Class.test_x (n=1)"; keep only the method name
    bad = [t.id().split(" ")[0].split(".")[-1] for t, _ in result.failures + result.errors]
    return total, sorted(set(bad))


def main():
    verbose = "-v" in sys.argv[1:]
    grand_total = grand_passed = 0
    print()
    for name, module in SECTIONS:
        total, bad = run(module)
        passed = total - len(bad)
        grand_total += total
        grand_passed += passed
        filled = round(BAR * passed / total) if total else 0
        mark = "✔" if passed == total else " "
        print(f" {mark} {name:<16} [{'█' * filled}{'░' * (BAR - filled)}] {passed:>3}/{total}")
        if verbose:
            for test in bad:
                print(f"       ✘ {test}")
    pct = 100 * grand_passed // grand_total if grand_total else 0
    print(f"\n   Total: {grand_passed}/{grand_total} tests passing ({pct}%)\n")
    return 0 if grand_passed == grand_total else 1


if __name__ == "__main__":
    sys.exit(main())
