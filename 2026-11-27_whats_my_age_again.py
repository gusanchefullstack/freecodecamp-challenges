"""
What's My Age Again?
Date: 2026-11-27

Sources:
- X post: https://x.com/freeCodeCamp (daily coding challenge post, 2026-11-27)
- Challenge page: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-11-27

Challenge:
Given the date of someone's birthday in the format YYYY-MM-DD, return the
person's age as of November 27th, 2025.

- Assume all birthdays are valid dates before November 27th, 2025.
- Return the age as an integer.
- Be sure to account for whether the person has already had their birthday
  in 2025.

Note: the X post says "return their age as of today". The challenge page
uses November 27th, 2025 as "today", and the tests below use that date.

Examples / tests:
1. calculate_age("2000-11-20") should return 25.
2. calculate_age("2000-12-01") should return 24.
3. calculate_age("2014-10-25") should return 11.
4. calculate_age("1994-01-06") should return 31.
5. calculate_age("1994-12-14") should return 30.
"""


def calculate_age(birthday):
    """Return the age (int) on 2025-11-27 for a birthday string 'YYYY-MM-DD'."""
    pass


if __name__ == "__main__":
    tests = [
        ("2000-11-20", 25),
        ("2000-12-01", 24),
        ("2014-10-25", 11),
        ("1994-01-06", 31),
        ("1994-12-14", 30),
    ]
    for birthday, expected in tests:
        result = calculate_age(birthday)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: calculate_age({birthday!r}) = {result!r}, expected {expected!r}")

    for birthday, expected in tests:
        assert calculate_age(birthday) == expected, f"calculate_age({birthday!r}) should return {expected}"
    print("All tests passed!")
