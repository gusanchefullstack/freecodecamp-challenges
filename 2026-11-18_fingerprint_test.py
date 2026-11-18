"""
Fingerprint Test
================

Date: 2026-11-18 (freeCodeCamp daily coding challenge #99)

Sources:
- X post: https://x.com/freeCodeCamp/status/2122692387755459030
  ("For today's coding challenge, you'll get two strings representing
  fingerprints. Given a set of rules, you'll need to determine if they're
  a match. Check it out on the freeCodeCamp mobile app.")
- Challenge page: https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-17
  (challenge text and tests taken from the freeCodeCamp daily challenge API)

Challenge
---------
Given two strings representing fingerprints, determine if they are a match
using the following rules:

- Each fingerprint will consist only of lowercase letters (a-z).
- Two fingerprints are considered a match if:
  - They are the same length.
  - The number of differing characters does not exceed 10% of the
    fingerprint length.

Tests
-----
1. is_match("helloworld", "helloworld") should return True.
2. is_match("helloworld", "helloworlds") should return False.
3. is_match("helloworld", "jelloworld") should return True.
4. is_match("thequickbrownfoxjumpsoverthelazydog",
            "thequickbrownfoxjumpsoverthelazydog") should return True.
5. is_match("theslickbrownfoxjumpsoverthelazydog",
            "thequickbrownfoxjumpsoverthehazydog") should return True.
6. is_match("thequickbrownfoxjumpsoverthelazydog",
            "thequickbrownfoxjumpsoverthehazycat") should return False.
"""
import math


def is_match(fingerprint_a: str, fingerprint_b: str) -> bool:
    """Return True if the two fingerprints match, otherwise False."""
    if len(fingerprint_a) == len(fingerprint_b):
      words_length = len(fingerprint_a)
      max_errors = math.floor(len(fingerprint_a)/10)
      errors = 0
      for letter in range(words_length):
        if fingerprint_a[letter] != fingerprint_b[letter]:
          errors += 1
      return not errors > max_errors
    else: 
      return False


if __name__ == "__main__":
    tests = [
        (("helloworld", "helloworld"), True),
        (("helloworld", "helloworlds"), False),
        (("helloworld", "jelloworld"), True),
        (("thequickbrownfoxjumpsoverthelazydog",
          "thequickbrownfoxjumpsoverthelazydog"), True),
        (("theslickbrownfoxjumpsoverthelazydog",
          "thequickbrownfoxjumpsoverthehazydog"), True),
        (("thequickbrownfoxjumpsoverthelazydog",
          "thequickbrownfoxjumpsoverthehazycat"), False)
    ]

    passed = 0
    for i, (args, expected) in enumerate(tests, start=1):
        result = is_match(*args)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"Test {i}: {status} - is_match{args} -> {result!r} (expected {expected!r})")

    print(f"\n{passed}/{len(tests)} tests passed")
    assert passed == len(tests), "Some tests failed. Keep going!"
