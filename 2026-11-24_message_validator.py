"""
Message Validator
Date: 2026-11-24

Source:
- https://x.com/freeCodeCamp/status/2125224199962681377
- https://www.freecodecamp.org/learn/daily-coding-challenge/2025-11-24
  (freeCodeCamp lists this challenge under the date 2025-11-24)

Challenge:
Given a message string and a validation string, determine if the message
is valid.

- A message is valid if each word in the message starts with the
  corresponding letter in the validation string, in order.
- Letters are case-insensitive.
- Words in the message are separated by single spaces.

Tests:
1. is_valid_message("hello world", "hw") should return True.
2. is_valid_message("ALL CAPITAL LETTERS", "acl") should return True.
3. is_valid_message("Coding challenge are boring.", "cca")
   should return False.
4. is_valid_message("The quick brown fox jumps over the lazy dog.",
   "TQBFJOTLD") should return True.
5. is_valid_message("The quick brown fox jumps over the lazy dog.",
   "TQBFJOTLDT") should return False.
"""


def is_valid_message(message: str, validator: str) -> bool:
    """Return True if each word in message starts with the matching letter in validator."""
    pass


if __name__ == "__main__":
    tests = [
        (("hello world", "hw"), True),
        (("ALL CAPITAL LETTERS", "acl"), True),
        (("Coding challenge are boring.", "cca"), False),
        (("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"), True),
        (("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"), False),
    ]

    for i, (args, expected) in enumerate(tests, start=1):
        result = is_valid_message(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        print(f"  got:      {result}")
        print(f"  expected: {expected}")

    for args, expected in tests:
        assert is_valid_message(*args) == expected
    print("All tests passed!")
