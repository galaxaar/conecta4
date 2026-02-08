
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
    
    def play(self, board: list[list]):
        """
        Elige de entre todas las columnas disponibles, la que contenga
        la mejor jugada (recomendada por el oráculo)
        """
        
        #Obtengo las recomendaciones (utilizo tupla, evito crear una clase para 2 valores)
        (best, recommendations) = self._ask_oracle(board)
        #Metemos ficha en la mejor opción (jugamos)
        self._play_on(board, best.index)
    
    def _play_on(self, board: list[list], position: int):
        """
        Jugamos en la posición dada (position)
        """
        board.add(self._char, position) #metemos el player_char en la posición
    
    def _ask_oracle(self, board):
        """
        Pregunta al oráculo y devuelve la mejor opción
        """
        recommendations = self._oracle.get_recommendation(board, self)
        best = self._choose(recommendations)
        return (best, recommendations) #refactorizado, mucho más sencillo
    
    def _choose(self, recommendations):
        """
        Se encarga de seleccionar la mejor jugada según 
        las recomendaciones
        """
        from conecta4.oracle import ColumnClassification
        #filtramos las columnas que ya estén llenas. Acá llamo a la property del atributo privado
        valid = list(filter(lambda x: x.classification != ColumnClassification.FULL, recommendations))
        #es decir, todas las columnas que no estén llenas, pasan el filtro
        return valid[0] #la primera que no esté llena
    #filter NO DEVUELVE UNA LISTA, por lo que lo convertimos manualmente a lista

#Funciones de validacion de índice de columna
def _not_full_column(board, num):
    """
    Nos ayuda a validar jugadas humanas. Identifica que 
    la columna seleccionada NO esté llena y avala la jugada.
    """
    #obtengo la columna especifica (num) y utilizamos is_full() para determinar si está llena o no
    return not board.is_full(num)
    
def _is_in_column_range(board, num):
    """
    Nos ayuda a validar jugadas humanas. Identifica que 
    la columna seleccionada esté dentro del rango de board.
    """
    return num >= 0 and num < len(board)

def _is_int(string)-> bool:
    """
    Nos ayuda a validar jugadas humanas. Identifica que 
    el string insertado represente un entero únicamente.
    """
    try:
        num = int(string)# convierte en un int "puro"
        return True
    except:
        return False #era cualquier otra cosa (otro string, un float, una función) y no la puede convertir a