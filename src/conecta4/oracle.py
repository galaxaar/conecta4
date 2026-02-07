from enum import Enum
from conecta4.board import Board
from conecta4.player import Player
from conecta4.settings import BOARD_COLUMNS, BOARD_ROWS
# Clases de columna
class ColumnClassification(Enum):
    FULL = -1 #imposible
    LOSE = 1 #derrota inminente
    BAD = 5 #Muy indeseable
    MAYBE = 10 #Indeseable
    WIN = 100 #Victoria inmediata 


# Recomendación de una columna: indice + clase
class ColumnRecommendation:
    """ 
    Clase que representa la recomendación del oráculo para
    una columna. Se compone del índice de dicha columna en
    el tablero y un valor de ColumnClassification.
    """

    def __init__(self, index: int, classification: ColumnClassification)-> None:
        self._index = index
        self._classification = classification
    
# Oráculos, de más tonto a más listo
# Los oráculos, deben de realizar un trabajo complejo: clasificar columnas
#en el caso más complejo, teniendo en cuenta errores del pasado.
#Usamos divide y venceras y cada oráculo, del más tonto al más listo
#se encargará de una parte.

class BaseOracle:
    """
    La clase base y el oráculo más tonto: clasifica las columnas en
    llena y no llenas.
    """
    #creamos un metodo

    def get_recommendation(self, board: Board, player: Player)-> list[ColumnRecommendation]:
        """
        
        """
        recommendations = []
        for index in range(BOARD_COLUMNS):
            recommendations.append(self._get_column_recommendation(board, index, player))
        return recommendations
    
    def _get_column_recommendation(self, board: Board, index: int, player: Player)-> ColumnRecommendation:
        """
        Método privado, que determina si una columna está llena, en cuyo
        caso la clasifica como FULL. Para todos los demás, MAYBE
        """
        result = ColumnRecommendation(index, ColumnClassification.MAYBE)
        #por cada columna del tablero
        for col in board._columns:
        #Si esa columna está llena, cambia la respuesta de MAYBE a FULL
            if self._is_full(col):
                result = ColumnRecommendation(index, ColumnClassification.FULL)
        return result
    
    def _is_full(col: list)-> bool:
        result = True
        for el in col:
            if el == None:
                result = False
                break
    
class SmartOracle(BaseOracle):
    """
    Refina la recomendacion del oraculo base, intentando afinar
    la clasificacion MAYBE a algo más preciso. En concreto a WIN: va
    a determinar qué jugadas nos llevan a ganas de inmedianto
    """
    def _get_column_recommendation(self, board: Board, index: int, player: Player):
        """
        Afina las recomendaciones. Las que hayan saludo como MAYBE,
        intento ver si hay algo má spreciso, en concreto una victoria
        para player.
        """
        #pido la clasificación básica
        basic_class = super()._get_column_recommendation(board, index, player)
        #Afino los maybe: juego como player en esa columna y compruebo si eso me da una victoria
        if basic_class._classification == ColumnClassification.MAYBE:
            #se puede mejorar
            #creo un tablero temporal a partir de board
            #juego en index
            #le pregunto al tablero temporal si es is_victory(player)
            #si es así, reclasifico a WIN 
            pass
        return basic_class
