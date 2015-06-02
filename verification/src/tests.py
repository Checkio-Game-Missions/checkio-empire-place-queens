TESTS = {
    "Rank_01": [
        {
            "input": ["b2", "c4", "d6", "e8"],
            "possible": True,
            "show": '{"b2", "c4", "d6", "e8"}'
        },
        {
            "input": ["b2", "c4", "d6", "e8", "a7", "g5"],
            "possible": False,
            "show": '{"b2", "c4", "d6", "e8", "a7", "g5"}'
        },
        {
            "input": ["a5", "b7", "c1", "e2", "f8", "g6", "h3"],
            "possible": True,
            "show": '{"a5", "b7", "c1", "e2", "f8", "g6", "h3"}'
        },
        {
            "input": ["a1", "h8"],
            "possible": False,
            "show": '{"a1", "h8"}'
        },
        {
            "input": ["d5"],
            "possible": True,
            "show": '{"d5"}'
        },
        {
            "input": ["b2", "f7"],
            "possible": True,
            "show": '{"b2", "f7"}'
        },
        {
            "input": ["b3", "d4", "f5"],
            "possible": False,
            "show": '{"b3", "d4", "f5"}'
        },
        {
            "input": ["b3", "d2", "f5"],
            "possible": True,
            "show": '{"b3", "d2", "f5"}'
        },
        {
            "input": ["a4", "g8", "h2", "e1", "f6"],
            "possible": True,
            "show": '{"a4", "g8", "h2", "e1", "f6"}'
        },
        {
            "input": ["c3", "d3", "e3", "f3"],
            "possible": False,
            "show": '{"c3", "d3", "e3", "f3"}'
        },
        {
            "input": ["d5", "d7", "e1"],
            "possible": False,
            "show": '{"d5", "d7", "e1"}'
        },


    ]
}
