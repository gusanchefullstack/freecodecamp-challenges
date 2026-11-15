"""
GCD
Date: 2026-11-15

Sources:
- freeCodeCamp post on X: https://x.com/freeCodeCamp
- Challenge page: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-11-15

Challenge
---------
Given two positive integers, return their greatest common divisor (GCD).

The GCD of two integers is the largest number that divides evenly into both
numbers without leaving a remainder.

For example, the divisors of 4 are 1, 2, and 4. The divisors of 6 are 1, 2, 3,
and 6. So given 4 and 6, return 2, the largest number that appears in both sets
of divisors.

Tests
-----
1. gcd(4, 6) should return 2.
2. gcd(20, 15) should return 5.
3. gcd(13, 17) should return 1.
4. gcd(654, 456) should return 6.
5. gcd(3456, 4320) should return 864.
"""


def gcd(a, b):
    """Return the greatest common divisor of two positive integers a and b."""
    divisors_a = []
    divisors_b = []
    for number in range(1,a+1):
        if a%number == 0:
            divisors_a.append(number)
    for number in range(1,b+1):
        if b%number == 0:
            divisors_b.append(number)
    divisors_a.reverse()
    divisors_b.reverse()
    
    for divisor_a in divisors_a:
        for divisor_b in divisors_b:
            if divisor_a == divisor_b:
                return divisor_a               

if __name__ == "__main__":
    result = gcd(3456,4320)
    tests = [
        ((4, 6), 2),
        ((20, 15), 5),
        ((13, 17), 1),
        ((654, 456), 6),
        ((3456, 4320), 864),
    ]

    passed = 0
    for args, expected in tests:
        result = gcd(*args)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status}: gcd{args} -> {result!r} (expected {expected})")

    print(f"\n{passed}/{len(tests)} tests passed")
