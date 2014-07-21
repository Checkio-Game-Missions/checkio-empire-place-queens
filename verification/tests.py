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
            "input": ["b2", "c4", "d6", "e8"],
            "answer": [["b2", "c4", "d6", "e8"], True],
            "show": '{"b2", "c4", "d6", "e8"}'
        },
        {
            "input": ["b2", "c4", "d6", "e8", "a7", "g5"],
            "answer": [["b2", "c4", "d6", "e8", "a7", "g5"], False],
            "show": '{"b2", "c4", "d6", "e8", "a7", "g5"}'
        },
    ],
    "Extra": [
        {
            "input": ["a5", "b7", "c1", "e2", "f8", "g6", "h3"],
            "answer": [["a5", "b7", "c1", "e2", "f8", "g6", "h3"], True],
            "show": '{"a5", "b7", "c1", "e2", "f8", "g6", "h3"}'
        },
        {
            "input": ["a1", "h8"],
            "answer": [["a1", "h8"], False],
            "show": '{"a1", "h8"}'
        },
        {
            "input": ["d5"],
            "answer": [["d5"], True],
            "show": '{"d5"}'
        },
        {
            "input": ["b2", "f7"],
            "answer": [["b2", "f7"], True],
            "show": '{"b2", "f7"}'
        },
        {
            "input": ["b3", "d4", "f5"],
            "answer": [["b3", "d4", "f5"], False],
            "show": '{"b3", "d4", "f5"}'
        },
        {
            "input": ["b3", "d2", "f5"],
            "answer": [["b3", "d2", "f5"], True],
            "show": '{"b3", "d2", "f5"}'
        },
        {
            "input": ["a4", "g8", "h2", "e1", "f6"],
            "answer": [["a4", "g8", "h2", "e1", "f6"], True],
            "show": '{"a4", "g8", "h2", "e1", "f6"}'
        },
        {
            "input": ["c3", "d3", "e3", "f3"],
            "answer": [["c3", "d3", "e3", "f3"], False],
            "show": '{"c3", "d3", "e3", "f3"}'
        },
        {
            "input": ["d5", "d7", "e1"],
            "answer": [["d5", "d7", "e1"], False],
            "show": '{"d5", "d7", "e1"}'
        },


    ]
}
