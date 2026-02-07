from conecta4.oracle import *
from conecta4.board import *

def test_base_oracle():
    board = Board.from_list([[None, None, None, None],
                             ["x", "o", "x", "o"],
                             ["o","o", "x", "x"],
                             ["o", None, None, None]])
    expected = [ColumnRecommendation(0, ColumnClassification.MAYBE),
                ColumnRecommendation(1, ColumnClassification.FULL),
                ColumnRecommendation(2, ColumnClassification.FULL),
                ColumnRecommendation(3, ColumnClassification.MAYBE),
                ColumnRecommendation(4, ColumnClassification.MAYBE)]
    rappel = BaseOracle()

    assert len(rappel.get_recommendation(board, None)) == len(expected)
    assert rappel.get_recommendation(board, None) == expected