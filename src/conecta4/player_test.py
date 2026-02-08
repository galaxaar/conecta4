from conecta4.board import Board
from conecta4.oracle import BaseOracle
from conecta4.player import Player

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