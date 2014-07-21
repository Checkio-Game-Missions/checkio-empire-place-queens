"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["b1", "c4", "d6", "e8"],
            "answer": [["b1", "c4", "d6", "e8"], True],
            "show": '{"b1", "c4", "d6", "e8"}'
        },
        {
            "input": ["b1", "c4", "d6", "e8", "a7", "g5"],
            "answer": [["b1", "c4", "d6", "e8", "a7", "g5"], False],
            "show": '{"b1", "c4", "d6", "e8", "a7", "g5"}'
        },
    ],
    "Extra": [
        {
            "input": ["b1", "c4", "d6", "e8"],
            "answer": [["b1", "c4", "d6", "e8"], True],
            "show": '{"b1", "c4", "d6", "e8"}'
        },
    ]
}
