
class Player:
    """
    Representa a un jugador, con un nombre y un caracter, con 
    el que juega, en un tablero con la recomendación del oráculo.
    """

    def __init__(self, name: str, char:str, oracle = None)-> None:
        #importo dentro de la función debido a que me generaba un circular import
        if oracle is None:
            from conecta4.oracle import BaseOracle
            oracle = BaseOracle()
        self._name = name
        self._char = char
        self._oracle = oracle
    
    def play(self, board):
        """
        Elige de entre todas las columnas disponibles, la que contenga
        la mejor jugada (recomendada por el oráculo)
        """
        
        #Obtengo las recomendaciones
        recomm = self._oracle.get_recommendation(board, self)
        #Selecciona la mejor
        best = self._choose(recomm)
        #Metemos ficha (jugamos)
        board.play(self._char, best.index)
    
    def _choose(self, recommendations):
        """
        Se encarga de seleccionar la mejor jugada según 
        las recomendaciones
        """
        from conecta4.oracle import ColumnClassification
        #filtramos las columnas que ya estén llenas
        valid = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommendations))
        #es decir, todas las columnas que no estén llenas, pasan el filtro
        return valid[0] #la primera que no esté llena
    
    #filter NO DEVUELVE UNA LISTA, por lo que lo convertimos manualmente a lista