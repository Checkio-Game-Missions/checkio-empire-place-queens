from checkio_referee import RefereeBase
from checkio_referee import covercodes, validators, representations, ENV_NAME


import settings_env
from tests import TESTS

from itertools import combinations

THREATS = {
    'h2': ['a2', 'b2', 'b8', 'c2', 'c7', 'd2', 'd6', 'e2', 'e5', 'f2', 'f4', 'g1', 'g2', 'g3', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'g2': ['a2', 'a8', 'b2', 'b7', 'c2', 'c6', 'd2', 'd5', 'e2', 'e4', 'f1', 'f2', 'f3', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h1', 'h2', 'h3'],
    'a4': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b3', 'b4', 'b5', 'c2', 'c4', 'c6', 'd1', 'd4', 'd7', 'e4',
           'e8', 'f4', 'g4', 'h4'],
    'h8': ['a1', 'a8', 'b2', 'b8', 'c3', 'c8', 'd4', 'd8', 'e5', 'e8', 'f6', 'f8', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'd8': ['a5', 'a8', 'b6', 'b8', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e7', 'e8', 'f6', 'f8',
           'g5', 'g8', 'h4', 'h8'],
    'g1': ['a1', 'a7', 'b1', 'b6', 'c1', 'c5', 'd1', 'd4', 'e1', 'e3', 'f1', 'f2', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6',
           'g7', 'g8', 'h1', 'h2'],
    'a7': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b6', 'b7', 'b8', 'c5', 'c7', 'd4', 'd7', 'e3', 'e7', 'f2',
           'f7', 'g1', 'g7', 'h7'],
    'a3': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b2', 'b3', 'b4', 'c1', 'c3', 'c5', 'd3', 'd6', 'e3', 'e7',
           'f3', 'f8', 'g3', 'h3'],
    'c3': ['a1', 'a3', 'a5', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd2', 'd3', 'd4', 'e1',
           'e3', 'e5', 'f3', 'f6', 'g3', 'g7', 'h3', 'h8'],
    'h1': ['a1', 'a8', 'b1', 'b7', 'c1', 'c6', 'd1', 'd5', 'e1', 'e4', 'f1', 'f3', 'g1', 'g2', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'b4': ['a3', 'a4', 'a5', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c3', 'c4', 'c5', 'd2', 'd4', 'd6', 'e1',
           'e4', 'e7', 'f4', 'f8', 'g4', 'h4'],
    'b2': ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'd2', 'd4', 'e2', 'e5',
           'f2', 'f6', 'g2', 'g7', 'h2', 'h8'],
    'g8': ['a2', 'a8', 'b3', 'b8', 'c4', 'c8', 'd5', 'd8', 'e6', 'e8', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6',
           'g7', 'g8', 'h7', 'h8'],
    'g6': ['a6', 'b1', 'b6', 'c2', 'c6', 'd3', 'd6', 'e4', 'e6', 'e8', 'f5', 'f6', 'f7', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h5', 'h6', 'h7'],
    'h7': ['a7', 'b1', 'b7', 'c2', 'c7', 'd3', 'd7', 'e4', 'e7', 'f5', 'f7', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'e1': ['a1', 'a5', 'b1', 'b4', 'c1', 'c3', 'd1', 'd2', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2',
           'g1', 'g3', 'h1', 'h4'],
    'h4': ['a4', 'b4', 'c4', 'd4', 'd8', 'e1', 'e4', 'e7', 'f2', 'f4', 'f6', 'g3', 'g4', 'g5', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'g4': ['a4', 'b4', 'c4', 'c8', 'd1', 'd4', 'd7', 'e2', 'e4', 'e6', 'f3', 'f4', 'f5', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h3', 'h4', 'h5'],
    'd7': ['a4', 'a7', 'b5', 'b7', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e6', 'e7', 'e8',
           'f5', 'f7', 'g4', 'g7', 'h3', 'h7'],
    'h5': ['a5', 'b5', 'c5', 'd1', 'd5', 'e2', 'e5', 'e8', 'f3', 'f5', 'f7', 'g4', 'g5', 'g6', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'f5': ['a5', 'b1', 'b5', 'c2', 'c5', 'c8', 'd3', 'd5', 'd7', 'e4', 'e5', 'e6', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g4', 'g5', 'g6', 'h3', 'h5', 'h7'],
    'f3': ['a3', 'a8', 'b3', 'b7', 'c3', 'c6', 'd1', 'd3', 'd5', 'e2', 'e3', 'e4', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g2', 'g3', 'g4', 'h1', 'h3', 'h5'],
    'b8': ['a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c7', 'c8', 'd6', 'd8', 'e5', 'e8', 'f4', 'f8',
           'g3', 'g8', 'h2', 'h8'],
    'b7': ['a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c6', 'c7', 'c8', 'd5', 'd7', 'e4', 'e7',
           'f3', 'f7', 'g2', 'g7', 'h1', 'h7'],
    'b3': ['a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c2', 'c3', 'c4', 'd1', 'd3', 'd5', 'e3',
           'e6', 'f3', 'f7', 'g3', 'g8', 'h3'],
    'g3': ['a3', 'b3', 'b8', 'c3', 'c7', 'd3', 'd6', 'e1', 'e3', 'e5', 'f2', 'f3', 'f4', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h2', 'h3', 'h4'],
    'c4': ['a2', 'a4', 'a6', 'b3', 'b4', 'b5', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd3', 'd4', 'd5', 'e2',
           'e4', 'e6', 'f1', 'f4', 'f7', 'g4', 'g8', 'h4'],
    'f7': ['a2', 'a7', 'b3', 'b7', 'c4', 'c7', 'd5', 'd7', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
           'f8', 'g6', 'g7', 'g8', 'h5', 'h7'],
    'f6': ['a1', 'a6', 'b2', 'b6', 'c3', 'c6', 'd4', 'd6', 'd8', 'e5', 'e6', 'e7', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g5', 'g6', 'g7', 'h4', 'h6', 'h8'],
    'e8': ['a4', 'a8', 'b5', 'b8', 'c6', 'c8', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f7', 'f8',
           'g6', 'g8', 'h5', 'h8'],
    'c8': ['a6', 'a8', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd7', 'd8', 'e6', 'e8', 'f5', 'f8',
           'g4', 'g8', 'h3', 'h8'],
    'e5': ['a1', 'a5', 'b2', 'b5', 'b8', 'c3', 'c5', 'c7', 'd4', 'd5', 'd6', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',
           'e8', 'f4', 'f5', 'f6', 'g3', 'g5', 'g7', 'h2', 'h5', 'h8'],
    'e4': ['a4', 'a8', 'b1', 'b4', 'b7', 'c2', 'c4', 'c6', 'd3', 'd4', 'd5', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7',
           'e8', 'f3', 'f4', 'f5', 'g2', 'g4', 'g6', 'h1', 'h4', 'h7'],
    'c2': ['a2', 'a4', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'e2', 'e4',
           'f2', 'f5', 'g2', 'g6', 'h2', 'h7'],
    'c5': ['a3', 'a5', 'a7', 'b4', 'b5', 'b6', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd4', 'd5', 'd6', 'e3',
           'e5', 'e7', 'f2', 'f5', 'f8', 'g1', 'g5', 'h5'],
    'a1': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'c1', 'c3', 'd1', 'd4', 'e1', 'e5', 'f1', 'f6',
           'g1', 'g7', 'h1', 'h8'],
    'c6': ['a4', 'a6', 'a8', 'b5', 'b6', 'b7', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd5', 'd6', 'd7', 'e4',
           'e6', 'e8', 'f3', 'f6', 'g2', 'g6', 'h1', 'h6'],
    'd2': ['a2', 'a5', 'b2', 'b4', 'c1', 'c2', 'c3', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3',
           'f2', 'f4', 'g2', 'g5', 'h2', 'h6'],
    'f1': ['a1', 'a6', 'b1', 'b5', 'c1', 'c4', 'd1', 'd3', 'e1', 'e2', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
           'g1', 'g2', 'h1', 'h3'],
    'g7': ['a1', 'a7', 'b2', 'b7', 'c3', 'c7', 'd4', 'd7', 'e5', 'e7', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h6', 'h7', 'h8'],
    'f4': ['a4', 'b4', 'b8', 'c1', 'c4', 'c7', 'd2', 'd4', 'd6', 'e3', 'e4', 'e5', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6',
           'f7', 'f8', 'g3', 'g4', 'g5', 'h2', 'h4', 'h6'],
    'c7': ['a5', 'a7', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd6', 'd7', 'd8', 'e5', 'e7',
           'f4', 'f7', 'g3', 'g7', 'h2', 'h7'],
    'c1': ['a1', 'a3', 'b1', 'b2', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'e1', 'e3', 'f1', 'f4',
           'g1', 'g5', 'h1', 'h6'],
    'e2': ['a2', 'a6', 'b2', 'b5', 'c2', 'c4', 'd1', 'd2', 'd3', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1',
           'f2', 'f3', 'g2', 'g4', 'h2', 'h5'],
    'a2': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'c2', 'c4', 'd2', 'd5', 'e2', 'e6', 'f2',
           'f7', 'g2', 'g8', 'h2'],
    'd6': ['a3', 'a6', 'b4', 'b6', 'b8', 'c5', 'c6', 'c7', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e5', 'e6',
           'e7', 'f4', 'f6', 'f8', 'g3', 'g6', 'h2', 'h6'],
    'a8': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b7', 'b8', 'c6', 'c8', 'd5', 'd8', 'e4', 'e8', 'f3', 'f8',
           'g2', 'g8', 'h1', 'h8'],
    'd3': ['a3', 'a6', 'b1', 'b3', 'b5', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e2', 'e3',
           'e4', 'f1', 'f3', 'f5', 'g3', 'g6', 'h3', 'h7'],
    'f8': ['a3', 'a8', 'b4', 'b8', 'c5', 'c8', 'd6', 'd8', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
           'g7', 'g8', 'h6', 'h8'],
    'd1': ['a1', 'a4', 'b1', 'b3', 'c1', 'c2', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'f1', 'f3',
           'g1', 'g4', 'h1', 'h5'],
    'a5': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b4', 'b5', 'b6', 'c3', 'c5', 'c7', 'd2', 'd5', 'd8', 'e1',
           'e5', 'f5', 'g5', 'h5'],
    'b1': ['a1', 'a2', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'd1', 'd3', 'e1', 'e4', 'f1', 'f5',
           'g1', 'g6', 'h1', 'h7'],
    'e6': ['a2', 'a6', 'b3', 'b6', 'c4', 'c6', 'c8', 'd5', 'd6', 'd7', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
           'f5', 'f6', 'f7', 'g4', 'g6', 'g8', 'h3', 'h6'],
    'a6': ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b5', 'b6', 'b7', 'c4', 'c6', 'c8', 'd3', 'd6', 'e2', 'e6',
           'f1', 'f6', 'g6', 'h6'],
    'd4': ['a1', 'a4', 'a7', 'b2', 'b4', 'b6', 'c3', 'c4', 'c5', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e3',
           'e4', 'e5', 'f2', 'f4', 'f6', 'g1', 'g4', 'g7', 'h4', 'h8'],
    'g5': ['a5', 'b5', 'c1', 'c5', 'd2', 'd5', 'd8', 'e3', 'e5', 'e7', 'f4', 'f5', 'f6', 'g1', 'g2', 'g3', 'g4', 'g5',
           'g6', 'g7', 'g8', 'h4', 'h5', 'h6'],
    'b5': ['a4', 'a5', 'a6', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c4', 'c5', 'c6', 'd3', 'd5', 'd7', 'e2',
           'e5', 'e8', 'f1', 'f5', 'g5', 'h5'],
    'b6': ['a5', 'a6', 'a7', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c5', 'c6', 'c7', 'd4', 'd6', 'd8', 'e3',
           'e6', 'f2', 'f6', 'g1', 'g6', 'h6'],
    'h3': ['a3', 'b3', 'c3', 'c8', 'd3', 'd7', 'e3', 'e6', 'f1', 'f3', 'f5', 'g2', 'g3', 'g4', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'h6': ['a6', 'b6', 'c1', 'c6', 'd2', 'd6', 'e3', 'e6', 'f4', 'f6', 'f8', 'g5', 'g6', 'g7', 'h1', 'h2', 'h3', 'h4',
           'h5', 'h6', 'h7', 'h8'],
    'f2': ['a2', 'a7', 'b2', 'b6', 'c2', 'c5', 'd2', 'd4', 'e1', 'e2', 'e3', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7',
           'f8', 'g1', 'g2', 'g3', 'h2', 'h4'],
    'd5': ['a2', 'a5', 'a8', 'b3', 'b5', 'b7', 'c4', 'c5', 'c6', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e4',
           'e5', 'e6', 'f3', 'f5', 'f7', 'g2', 'g5', 'g8', 'h1', 'h5'],
    'e3': ['a3', 'a7', 'b3', 'b6', 'c1', 'c3', 'c5', 'd2', 'd3', 'd4', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
           'f2', 'f3', 'f4', 'g1', 'g3', 'g5', 'h3', 'h6'],
    'e7': ['a3', 'a7', 'b4', 'b7', 'c5', 'c7', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f6',
           'f7', 'f8', 'g5', 'g7', 'h4', 'h7']}

Result = validators.ValidatorResult


def py_repr(test, f):
    return "{}({})".format(f, set(test["input"]))

py_cover = """def cover(func, data):
    res = func(set(data))
    if not isinstance(res, set):
        raise TypeError("The result should be a set")
    return list(res)
"""

# def checker(data, user_data):
#
#     placed, is_possible = set(data[0]), data[1]
#     user_set = set(user_data[0])
#     if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
#         return False, (1, "Wrong Coordinates", [])
#     threats = []
#     for f, s in combinations(user_set.union(placed), 2):
#         if s in THREATS[f]:
#             threats.append([f, s])
#     if not is_possible:
#         if user_set:
#             return False, (3, "Hm, how did you place them?", threats)
#         else:
#             return True, (10, "Great!", threats)
#     if not all(p in user_set for p in placed):
#         return False, (4, "You forgot about placed queens.", threats)
#     if is_possible and threats:
#         return False, (5, "I see some problems in this placement.", threats)
#     return True, (100, "Great!", threats)

class QueensValidator(validators.BaseValidator):

    COLS = "abcdefgh"
    ROWS = "12345678"

    ERR_WRONG_COORDINATES = "Wrong Coordinates"
    ERR_IS_IT_POSSIBLE = "Hm, how did you place them?"
    ERR_FORGOT = "You forgot about placed queens."
    ERR_THREAT = "I see some problems in this placement."

    def check_coordinate(self, coor):
        c, r = coor
        return c in self.COLS and r in self.ROWS

    def validate(self, outer_result):
        placed = self._test.get("input", [])
        is_possible = self._test.get("possible", True)

        user_set = set(outer_result)
        if not all(isinstance(c, str) and len(c) == 2 and
                   self.check_coordinate(c) for c in user_set):
            return Result(False, self.ERR_WRONG_COORDINATES)
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                return Result(False, self.ERR_IS_IT_POSSIBLE)
            else:
                return Result(True, None)
        if not all(p in user_set for p in placed):
            return Result(False, self.ERR_FORGOT)
        if is_possible and threats:
            return Result(False, self.ERR_THREAT)
        return Result(True, None)

class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    VALIDATOR = QueensValidator
    DEFAULT_FUNCTION_NAME = "place_queens"
    FUNCTION_NAMES = {
        ENV_NAME.JS_NODE: "placeQueens"
    }

    CALLED_REPRESENTATIONS = {
        ENV_NAME.PYTHON: py_repr,
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: py_cover,
    }
