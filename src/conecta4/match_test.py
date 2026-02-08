from conecta4.player import Player
from conecta4.match import Match
pipu = Player("Pipulino")
brisa = Player("Michichi")

def test_different_chars():
    t = Match(pipu, brisa) #la class Match
    assert pipu._char != brisa._char #compruebo que el char de cada uno sea diferente a su oponente


def test_char_different_than_none(): #debemos cerciorarnos de que ningun jugador utilice NONE como char para sus jugadas
    t = Match(pipu, brisa)
    
    assert pipu._char != None and brisa._char != None

def test_next_player_is_round():
    t = Match(pipu, brisa)
    p1 = t.next_player
    p2 = t.next_player

    assert p1 != p2 #es decir, que en la proxima jugada no le toque al mismo

def test_players_are_opponents():
    t = Match(pipu, brisa)

    p1 = t.next_player
    p2 = t.next_player

    #comprobamos que cada player sepa quien es su oponente (p1, oponente p2 y así)
    assert p1.opponent == p2
    assert p2.opponent == p1
