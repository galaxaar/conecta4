from conecta4.player import Player
from conecta4.match import Match


def test_different_chars():
    pipu = Player("Pipulino")
    brisa = Player("Michichi")
    t = Match(pipu, brisa) #la class Match
    
    assert pipu._char != brisa._char #compruebo que el char de cada uno sea diferente a su oponente


def test_char_different_than_none(): #debemos cerciorarnos de que ningun jugador utilice NONE como char para sus jugadas
    pipu = Player("Pipulino")
    brisa = Player("Michichi")
    t = Match(pipu, brisa)
    
    assert pipu._char != None and brisa._char != None

def test_next_player_is_round():
    pipu = Player("Pipulino")
    brisa = Player("Michichi")
    t = Match(pipu, brisa)
    p1 = t.next_player
    p2 = t.next_player

    assert p1 != p2 #es decir, que en la proxima jugada no le toque al mismo

def test_players_are_opponents():
    pipu = Player("Pipulino")
    brisa = Player("Michichi")
    t = Match(pipu, brisa)

    x = t.get_player("x")
    o = t.get_player("o")

    #comprobamos que cada player sepa quien es su oponente (p1, oponente p2 y así)
    assert x.opponent == o
    assert o.opponent == x
