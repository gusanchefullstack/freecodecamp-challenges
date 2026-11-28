"""
BuzzFizz
Date: 2026-11-26

Sources:
- https://www.freecodecamp.org/learn/daily-coding-challenge/2026-11-26
- https://x.com/freeCodeCamp (daily coding challenge post)

Challenge:
Given an array, determine if it is a correct FizzBuzz sequence from 1 to the
last item in the array. A sequence is correct if:

- Numbers that are multiples of 3 are replaced with "Fizz"
- Numbers that are multiples of 5 are replaced with "Buzz"
- Numbers that are multiples of both 3 and 5 are replaced with "FizzBuzz"
- All other numbers remain as integers in ascending order, starting from 1.
- The array must start at 1 and have no missing or extra elements.

Examples (tests):
1. is_fizz_buzz([1, 2, "Fizz", 4]) should return True.
2. is_fizz_buzz([1, 2, 3, 4]) should return False.
3. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]) should return False.
4. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11,
   "Fizz", 13, "FizzBuzz"]) should return False.
5. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11,
   "Fizz", 13, "Fizz"]) should return False.
6. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11,
   "Fizz", 13, "Buzz"]) should return False.
7. is_fizz_buzz([1, 2, ..., 49, "Buzz"])  (a correct sequence from 1 to 50)
   should return True.
"""


def is_fizz_buzz(sequence):
    """Return True if `sequence` is a correct FizzBuzz sequence starting at 1,
    otherwise return False."""
    pass


if __name__ == "__main__":
    tests = [
        ([1, 2, "Fizz", 4], True),
        ([1, 2, 3, 4], False),
        ([1, 2, "Fizz", 4, "Buzz", 7], False),
        ([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "FizzBuzz"], False),
        ([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Fizz"], False),
        ([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"], False),
        (
            [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz",
             16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz",
             31, 32, "Fizz", 34, "Buzz", "Fizz", 37, 38, "Fizz", "Buzz", 41, "Fizz", 43, 44, "FizzBuzz",
             46, 47, "Fizz", 49, "Buzz"],
            True,
        ),
    ]

    passed = 0
    for i, (sequence, expected) in enumerate(tests, start=1):
        result = is_fizz_buzz(sequence)
        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"Test {i}: {status} (expected {expected}, got {result})")

    print(f"\n{passed}/{len(tests)} tests passed")
    assert passed == len(tests), "Some tests failed - keep going!"
