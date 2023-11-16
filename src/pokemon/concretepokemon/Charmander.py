from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.attack.concreteattack.EmberAttack import EmberAttack
from src.pokemon.stats.Stats import Stats
from src.pokemon.stats.BaseStats import BaseStats
from src.pokemon.type.concretetype.FireType import FireType
from src.Const import GROUP, NATURE, NATURE_LIST
from random import choice

class Charmander(Pokemon):
    def __init__(self,
                 name = "Charmander",
                 level = 1,
                 exp = 0,
                 nature = None,
                 attacks=None,
                 stats = None,
                 isWild = True,
                 heldItem = None):
        if attacks is None:
            attacks = [TackleAttack(), EmberAttack()]
        if nature is None:
            nature = choice(NATURE_LIST)
        if stats is None:
            stats = Stats(level, nature, BaseStats(39, 52, 43, 60, 50, 65))
        super().__init__(name, "Charmander", level, exp, GROUP.MEDIUM_SLOW, 65, [FireType()], nature, attacks, stats, isWild, heldItem)