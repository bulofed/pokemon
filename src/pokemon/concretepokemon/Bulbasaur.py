from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.stats.Stats import Stats
from src.pokemon.stats.BaseStats import BaseStats
from src.Const import NATURE_LIST
from src.pokemon.type.concretetype.GrassType import GrassType
from src.pokemon.exp.CGroup import CGroup
from random import choice

class Bulbasaur(Pokemon):
    def __init__(self,
                 name = "Bulbasaur",
                 level = 1,
                 exp = 0,
                 nature = None,
                 attacks=None,
                 stats = None,
                 isWild = True,
                 heldItem = None):
        if attacks is None:
            attacks = [TackleAttack]
        if nature is None:
            nature = choice(NATURE_LIST)
        if stats is None:
            stats = Stats(level, nature, BaseStats(45, 49, 49, 65, 65, 45))
        super().__init__(name, "Bulbasaur", level, exp, CGroup.MEDIUM_SLOW, 64, [GrassType()], nature, attacks, stats, isWild, heldItem)