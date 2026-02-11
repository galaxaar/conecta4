import pyfiglet
from enum import Enum, auto
from conecta4.player import Player, HumanPlayer
from conecta4.match import Match
from conecta4.board import Board
class RoundType(Enum):
    COMPUTER_VS_HUMAN = auto()
    COMPUTER_VS_COMPUTER = auto()

class LevelDifficulty(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()




class Game():

    def __init__(self, round_type = RoundType.COMPUTER_VS_COMPUTER, match = Match(Player("Ron"), Player("Whisky"))):
        self.round_type = round_type
        self.match = match

        #tablero sobre el que jugaremos (vacio)
        self.board = Board()

    def start(self):
        """
        Arranca el juego. Imprime el nombre
        del juego y su configuración.
        """
        self.print_logo()

        #metodo para preguntarle al usuario cual va ser el round_type 
        self._configure_by_user()

        #para comenzar el game loop
        self._start_game_loop():

    def print_logo(self):
        logo = pyfiglet.Figlet(font = "univers")
        print(logo.renderText("Coneta4"))
    
    def _start_game_loop(self):
        """
        Nuestro bucle infinito para hacer el juego en si
        """
        while True:
            #Obtenemos el jugador
            current_player = self.match.next_player
            #Juega
            current_player.play(self.board)
            #Mostramos la jugada
            self.display_move(current_player)
            #Imprimimos la jugada en el tablero
            self.display_board()
            #Si termina el juego
            if self._is_game_over():
                self.display_result() #muestro en pantalla el resultado
                break #salgo del bucle



    def _configure_by_user(self):
        """
        El usuario configura los valores de la partida
        """
        # tipo de partida (según seleccion del usuario)
        self.round_type = self._get_round_type()

        #creo la partida (creando el match)
        self.match = self._make_match()
    
    def _get_round_type(self):
        """
        Pedimos al usuario que elija el tipo de juego
        """
        print("""
              Select the opponents for the next round:
              1) Computer vs Computer
              2) Human vs Computer
              """)
        answer = ""
        while answer != "1" and answer != "2":
            answer = input("Please type either 1 or 2:  ")
        if answer == "1":
            result = RoundType.COMPUTER_VS_COMPUTER
        else:
            result = RoundType.COMPUTER_VS_HUMAN
        return result
    
    def _make_match(self):
        #Si la ronda seleccionada es IA VS IA....
        if self.round_type == RoundType.COMPUTER_VS_COMPUTER:
            player1 = Player("Buzz")
            player2 = Player("Zurg")
        else: #si es contra un humano...
            player1 = Player("Woody")  
            player2 = HumanPlayer(name = input("Introduce player name: "))
        return Match(player1, player2) #creamos la partida