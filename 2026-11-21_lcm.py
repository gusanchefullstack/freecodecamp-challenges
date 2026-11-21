"""
LCM
Date: 2026-11-21

Sources:
- X post: https://x.com/freeCodeCamp (daily coding challenge post, 2026-11-21)
- Challenge page: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-11-21

Challenge:
Given two integers, return the least common multiple (LCM) of the two numbers.

The LCM of two numbers is the smallest positive integer that is a multiple of
both numbers. For example, given 4 and 6, return 12 because:

- Multiples of 4 are 4, 8, 12 and so on.
- Multiples of 6 are 6, 12, 18 and so on.
- 12 is the smallest number that is a multiple of both.

Tests:
1. lcm(4, 6) should return 12.
2. lcm(9, 6) should return 18.
3. lcm(10, 100) should return 100.
4. lcm(13, 17) should return 221.
5. lcm(45, 70) should return 630.
"""

def get_multiples(number, max_multiple):
 multiples = []
 for item in range(number, max_multiple+1, number):
    multiples.append(item)
 return multiples

def lcm(a, b):
    """Return the least common multiple of the integers a and b."""
    max_multiple = a * b
    first = min(a, b)
    last = max(a,b)
    first_multiples = get_multiples(first, max_multiple)
    last_multiples = get_multiples(last, max_multiple)
    for first_multiple in first_multiples:
        for last_multiple in last_multiples:
            if first_multiple == last_multiple:
                return first_multiple

if __name__ == "__main__":
    tests = [
        ((4, 6), 12),
        ((9, 6), 18),
        ((10, 100), 100),
        ((13, 17), 221),
        ((45, 70), 630),
    ]
    for args, expected in tests:
        result = lcm(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: lcm{args} -> {result} (expected {expected})")

    for args, expected in tests:
        assert lcm(*args) == expected, f"lcm{args} should return {expected}"
    print("All tests passed!")
