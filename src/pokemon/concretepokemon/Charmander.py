from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.attack.concreteattack.EmberAttack import EmberAttack
from src.pokemon.stats.Stats import Stats
from src.pokemon.stats.BaseStats import BaseStats
from src.pokemon.type.concretetype.FireType import FireType
from src.Const import GROUP, NATURE
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
        if stats is None:
            stats = Stats(level, BaseStats(39, 52, 43, 60, 50, 65))
        if nature is None:
            nature = choice(list(NATURE.__dict__.values()))
        super().__init__(name, "Charmander", level, exp, GROUP.MEDIUM_SLOW, 65, [FireType()], nature, attacks, stats, isWild, heldItem)