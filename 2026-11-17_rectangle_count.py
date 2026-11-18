"""
Rectangle Count
===============

Date: 2026-11-17 (freeCodeCamp daily coding challenge #98)

Sources:
- X post: https://x.com/freeCodeCamp (post from 2026-11-17: "today's coding
  challenge is sorta like that, but for rectangles")
- Challenge page: https://www.freecodecamp.org/learn/daily-coding-challenge
  (challenge text taken from the freeCodeCamp daily challenge API:
  https://api.freecodecamp.org/daily-coding-challenge/today)

Challenge
---------
Given two positive integers representing the width and height of a
rectangle, determine how many rectangles can fit in the given one.

- Only count rectangles with integer width and height.

For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2
rectangles, and one 1x3 rectangle.

Tests
-----
1. count_rectangles(1, 3) should return 6.
2. count_rectangles(3, 2) should return 18.
3. count_rectangles(1, 2) should return 3.
4. count_rectangles(5, 4) should return 150.
5. count_rectangles(11, 19) should return 12540.

"""


def count_rectangles(width, height):
    """Return how many integer-sized rectangles fit inside a width x height rectangle."""
    horizontal_pairs = width * (width + 1) // 2
    vertical_pairs = height * (height + 1) // 2
    return horizontal_pairs * vertical_pairs


if __name__ == "__main__":
    count_rectangles(5,4)
    tests = [
        ((1, 3), 6),
        ((3, 2), 18),
        ((1, 2), 3),
        ((5, 4), 150),
        ((11, 19), 12540),
    ]

    passed = 0
    for args, expected in tests:
        result = count_rectangles(*args)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: count_rectangles{args} -> {result!r} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
