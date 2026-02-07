from conecta4.list_utils import *
from conecta4.board import *


VICTORY_STREAK = 3

def test_streak_at_beginning():
    assert find_streak(["x", "x", "x", "o"], "x", VICTORY_STREAK) 

def test_streak_breaks():
    assert find_streak(["o", "x", "x", "o"], "x", VICTORY_STREAK) == False

def test_streak_at_the_end():
    assert find_streak(["o", "x", "x", "x"], "x", VICTORY_STREAK) 

def test_streak_in_middle():
    assert find_streak(["o", "x", "x", "x", "o"], "x", VICTORY_STREAK)

def test_streak_with_non_existent_needle():
    assert find_streak(["x", "x", "x", "o"], "o", VICTORY_STREAK) == False

def test_streak_with_mixed_elements():
    assert find_streak([1, "x", "x", "o"], 1, VICTORY_STREAK) == False

def test_streak_with_more_than3():
    assert find_streak(["x", "x", "x", "x"], "x", VICTORY_STREAK) 

def test_streak_resets():
    assert find_streak(["x", "x", "o", "x", "x", "x"], "x", VICTORY_STREAK) 

def test_victory_invalid_streak():
    assert find_streak(["x", "x", "x"], "x", 0) == False
    
def test_victory_negative_streak():
    assert find_streak(["x", "x", "x"], "x", -1) == False

def test_find_else():
    assert find_streak(["o", "x", "o", "o"], "x", 2) == False

def test_transpose():
    original =  [[0, 7, 3], [4, 0, 1]]
    transposed = [[0, 4],[7, 0], [3, 1]]

    assert transpose(original) == transposed
    assert transpose(transpose(original)) == original

def test_displace_list():
    l1 = [1,2,3]

    assert displace_list(l1, 1, 7, None) == [None, 1, 2, 3, None, None, None]
    assert displace_list(l1, 3, 7, None) == [None, None, None, 1, 2, 3, None]

def test_displace_lol():
    lol = [[9], [12, 3], [5,8]]
    lol2 = [["x","o"], ["o","x"],["o", "o", "x"]]

    assert displace_lol(lol, 7, None) == ([[9, None, None, None, None, None, None],
                                            [None, 12, 3, None, None, None, None],
                                              [None, None, 5, 8, None, None, None]])
    
    assert displace_lol(lol2, 7, None) == ([["x","o", None, None, None, None, None],
                                            [None, "o", "x", None, None, None, None],
                                            [None, None, "o", "o", "x", None, None]])
    
def test_reversed_list():
    assert reversed_list([0, 1, 2, 3]) == [3, 2, 1, 0]
    assert reversed_list(["x", "y", "o", "x"]) == ["x", "o", "y", "x"]

def test_reversed_matrix():
    assert reversed_matrix([[1, 2, 3], [3, 2, 1]]) == [[3, 2, 1], [1, 2, 3]]
    assert reversed_matrix([["i", "h"], ["e", "r", "e", "h", "t"]]) == [["h", "i"], ["t", "h", "e", "r", "e"]]