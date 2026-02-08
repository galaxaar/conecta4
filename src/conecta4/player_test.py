from conecta4.board import Board
from conecta4.oracle import BaseOracle
from conecta4.player import Player, _is_in_column_range, _is_int, _not_full_column

def test_play():
    """
    Checkeamos que se juega en la primera columna disponible
    """
    before_tested = Board.from_list([["x", "x", "o", "x"],
                              [None, None, None, None],
                              ["o", "x", None, None],
                              ["x", "o", "o", "o"]])
    after_tested = Board.from_list([["x", "x", "o", "x"],
                              ["x", None, None, None],
                              ["o", "x", None, None],
                              ["x", "o", "o", "o"]])
    
    
    player = Player("Pupi", "x", oracle = BaseOracle())

    #jugamos
    player.play(before_tested)
    assert before_tested == after_tested

def test_valid_column():
    b = Board.from_list([["o", "x", None, None],
                         ["x", "o", "o", "x"],
                         ["o", "x", "x", "o"],
                         ["x", None, None, None]])
    assert _is_in_column_range(b, 0)
    assert _is_in_column_range(b, 1)
    assert _is_in_column_range(b, 2)
    assert _is_in_column_range(b, 3)
    assert _is_in_column_range(b, 6) == False
    assert _is_in_column_range(b, 20) == False
    assert _is_in_column_range(b, -3) == False

def test_not_full_column():
    b = Board.from_list([["o", "x", None, None],
                         ["x", "o", "o", "x"],
                         ["o", "x", "x", "o"],
                         ["x", None, None, None]])
    
    assert _not_full_column(b, 0)
    assert _not_full_column(b, 1) == False
    assert _not_full_column(b, 2) == False
    assert _not_full_column(b, 3)

def test_is_int():
    assert _is_int("0")
    assert _is_int(" ") == False
    assert _is_int("-12")
    assert _is_int("78")
    assert _is_int("pato") == False
    assert _is_int("4.28") == False
    assert _is_int("  42  ")