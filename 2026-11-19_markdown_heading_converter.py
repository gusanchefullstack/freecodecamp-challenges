"""
Markdown Heading Converter
==========================

Date: 2026-11-19 (freeCodeCamp daily coding challenge, posted on X on
2026-11-19 Pacific Time)

Sources:
- X post: https://x.com/freeCodeCamp/status/2123412294705013243
  ("For today's coding challenge, you'll get a string representing a markdown
  heading. You'll need to return the equivalent HTML heading. See if you can
  solve it on the freeCodeCamp mobile app.")
- Challenge page: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-11-19

Challenge
---------
Given a string representing a Markdown heading, return the equivalent HTML
heading.

A valid Markdown heading must:

- Start with zero or more spaces, followed by
- 1 to 6 hash characters (#) in a row, then
- At least one space. And finally,
- The heading text.

The number of hash symbols determines the heading level. For example, one hash
symbol corresponds to an h1 tag, and six hash symbols correspond to an h6 tag.

If the given string doesn't have the exact format above, return
"Invalid format".

For example, given "# My level 1 heading", return
"<h1>My level 1 heading</h1>".

Tests (examples)
----------------
1. convert("# My level 1 heading") should return "<h1>My level 1 heading</h1>".
2. convert("My heading") should return "Invalid format".
3. convert("##### My level 5 heading") should return "<h5>My level 5 heading</h5>".
4. convert("#My heading") should return "Invalid format".
5. convert("  ###  My level 3 heading") should return "<h3>My level 3 heading</h3>".
6. convert("####### My level 7 heading") should return "Invalid format".
7. convert("## My #2 heading") should return "<h2>My #2 heading</h2>".
"""


def convert(heading: str) -> str:
    """Convert a Markdown heading string to an HTML heading, or return "Invalid format"."""
    pass


if __name__ == "__main__":
    tests = [
        ("# My level 1 heading", "<h1>My level 1 heading</h1>"),
        ("My heading", "Invalid format"),
        ("##### My level 5 heading", "<h5>My level 5 heading</h5>"),
        ("#My heading", "Invalid format"),
        ("  ###  My level 3 heading", "<h3>My level 3 heading</h3>"),
        ("####### My level 7 heading", "Invalid format"),
        ("## My #2 heading", "<h2>My #2 heading</h2>"),
    ]

    passed = 0
    for i, (heading, expected) in enumerate(tests, start=1):
        result = convert(heading)
        ok = result == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"{status} test {i}: convert({heading!r}) -> {result!r} (expected {expected!r})")

    print(f"\n{passed}/{len(tests)} tests passed")
    assert passed == len(tests), "Some tests failed - keep going!"
