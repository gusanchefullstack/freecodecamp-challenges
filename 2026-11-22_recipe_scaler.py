"""
Recipe Scaler
Date: 2026-11-22

Source:
- https://www.freecodecamp.org/learn/daily-coding-challenge/2026-11-22
- https://x.com/freeCodeCamp (daily coding challenge post)

Challenge:
Given an array of recipe ingredients and a number to scale the recipe,
return an array with the quantities scaled accordingly.

- Each item in the given array will be a string in the format:
  "quantity unit ingredient". For example "2 C Flour".
- Scale the quantity by the given number. Do not include any trailing zeros
  and do not convert any units.
- Return the scaled items in the same order they are given.

Tests:
1. scaleRecipe(["2 C Flour", "1.5 T Sugar"], 2)
   should return ["4 C Flour", "3 T Sugar"].
2. scaleRecipe(["4 T Flour", "1 C Milk", "2 T Oil"], 1.5)
   should return ["6 T Flour", "1.5 C Milk", "3 T Oil"].
3. scaleRecipe(["3 C Milk", "2 C Oats"], 0.5)
   should return ["1.5 C Milk", "1 C Oats"].
4. scaleRecipe(["2 C All-purpose Flour", "1 t Baking Soda", "1 t Salt",
   "1 C Butter", "0.5 C Sugar", "0.5 C Brown Sugar", "1 t Vanilla Extract",
   "2 C Chocolate Chips"], 2.5)
   should return ["5 C All-purpose Flour", "2.5 t Baking Soda", "2.5 t Salt",
   "2.5 C Butter", "1.25 C Sugar", "1.25 C Brown Sugar",
   "2.5 t Vanilla Extract", "5 C Chocolate Chips"].
"""


# def scale_recipe(ingredients: list[str], scale: float) -> list[str]:
def scale_recipe(recipe: list[str], scale: float):
    """Return a new list with each ingredient's quantity multiplied by scale."""
    result = []
    for i,ingredient in enumerate(recipe):
        words_array = ingredient.split(" ")
        for i,word in enumerate(words_array):
            if word[0].isdigit():
                words_array[i] = f"{(float(word)*scale):g}"
        ingredient = " ".join(words_array)
        result.append(ingredient)
    return result


if __name__ == "__main__":
    # scale_recipe(["2 C Flour", "1.5 T Sugar"],2)
    tests = [
        (
            (["2 C Flour", "1.5 T Sugar"], 2),
            ["4 C Flour", "3 T Sugar"],
        ),
        (
            (["4 T Flour", "1 C Milk", "2 T Oil"], 1.5),
            ["6 T Flour", "1.5 C Milk", "3 T Oil"],
        ),
        (
            (["3 C Milk", "2 C Oats"], 0.5),
            ["1.5 C Milk", "1 C Oats"],
        ),
        (
            (
                [
                    "2 C All-purpose Flour",
                    "1 t Baking Soda",
                    "1 t Salt",
                    "1 C Butter",
                    "0.5 C Sugar",
                    "0.5 C Brown Sugar",
                    "1 t Vanilla Extract",
                    "2 C Chocolate Chips",
                ],
                2.5,
            ),
            [
                "5 C All-purpose Flour",
                "2.5 t Baking Soda",
                "2.5 t Salt",
                "2.5 C Butter",
                "1.25 C Sugar",
                "1.25 C Brown Sugar",
                "2.5 t Vanilla Extract",
                "5 C Chocolate Chips",
            ],
        ),
    ]

    for i, (args, expected) in enumerate(tests, start=1):
        result = scale_recipe(*args)
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i}: {status}")
        print(f"  got:      {result}")
        print(f"  expected: {expected}")

    for args, expected in tests:
        assert scale_recipe(*args) == expected
    print("All tests passed!")
