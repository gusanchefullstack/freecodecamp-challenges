"""
Character Count
Date: 2026-11-23

Source:
- https://x.com/freeCodeCamp/status/2124861807424573721
- https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-23
  (freeCodeCamp lists this challenge, #105, under the date 2025-11-23)

Challenge:
Given a sentence string, return an array with a count of each character
in alphabetical order.

- Treat upper and lowercase letters as the same letter when counting.
- Ignore numbers, spaces, punctuation, etc.
- Return the count and letter in the format "letter count".
  For instance, "a 3".
- All returned letters should be lowercase.
- Do not return a count of letters that are not in the given string.

Tests:
1. count_characters("hello world")
   should return ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"].
2. count_characters("I love coding challenges!")
   should return ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3",
   "n 2", "o 2", "s 1", "v 1"].
3. count_characters("// TODO: Complete this challenge ASAP!")
   should return ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3",
   "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"].
"""


def count_characters(sentence: str) -> list[str]:
    """Return a sorted list of "letter count" strings for each letter in sentence."""
    pass


if __name__ == "__main__":
    tests = [
        (
            "hello world",
            ["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"],
        ),
        (
            "I love coding challenges!",
            ["a 1", "c 2", "d 1", "e 3", "g 2", "h 1", "i 2", "l 3",
             "n 2", "o 2", "s 1", "v 1"],
        ),
        (
            "// TODO: Complete this challenge ASAP!",
            ["a 3", "c 2", "d 1", "e 4", "g 1", "h 2", "i 1", "l 3",
             "m 1", "n 1", "o 3", "p 2", "s 2", "t 3"],
        ),
    ]

    for i, (sentence, expected) in enumerate(tests, start=1):
        result = count_characters(sentence)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        print(f"  got:      {result}")
        print(f"  expected: {expected}")

    for sentence, expected in tests:
        assert count_characters(sentence) == expected
    print("All tests passed!")
