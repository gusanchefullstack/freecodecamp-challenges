"""
100 Characters
==============

Date: 2026-11-19 (freeCodeCamp daily coding challenge #100, posted on X on
2026-11-18 Pacific Time)

Sources:
- X post: https://x.com/freeCodeCamp/status/2123049863893979138
  ("This is the 100th daily coding challenge in the series! Given a string,
  you'll need to repeat its characters until the result is exactly 100
  characters long. Check it out on the freeCodeCamp mobile app.")
- Challenge page: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-11-18

Challenge
---------
Welcome to the 100th Daily Coding Challenge!

Given a string, repeat its characters until the result is exactly 100
characters long. If your repetitions go over 100 characters, trim the extra
so it's exactly 100.

Tests (examples)
----------------
1. one_hundred("One hundred ") should return
   "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One ".
2. one_hundred("freeCodeCamp ") should return
   "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC".
3. one_hundred("daily challenges ") should return
   "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge".
4. one_hundred("!") should return "!" repeated 100 times.
"""


def one_hundred(chars: str):
    """Repeat `chars` until the result is exactly 100 characters long."""
    repetitions = 100 // len(chars)
    reminder = 100 % len(chars)
    result = ""
    for sentence in range(repetitions):
        result += chars
    for letter in range(reminder):
        result += chars[letter]
    return result



if __name__ == "__main__":
    one_hundred("freeCodeCamp ")
    tests = [
        ("One hundred ",
         "One hundred One hundred One hundred One hundred One hundred One hundred One hundred One hundred One "),
        ("freeCodeCamp ",
         "freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeCamp freeCodeC"),
        ("daily challenges ",
         "daily challenges daily challenges daily challenges daily challenges daily challenges daily challenge"),
        ("!", "!" * 100),
    ]

    for chars, expected in tests:
        result = one_hundred(chars)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: one_hundred({chars!r}) -> {result!r}")

    for chars, expected in tests:
        assert one_hundred(chars) == expected, f"one_hundred({chars!r}) failed"
    print("All tests passed!")
