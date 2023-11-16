from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.stats.Stats import Stats
from src.pokemon.stats.BaseStats import BaseStats
from src.Const import GROUP, NATURE
from src.pokemon.type.concretetype.GrassType import GrassType
from random import choice

class Bulbasaur(Pokemon):
    def __init__(self,
                 name = "Bulbasaur",
                 level = 1,
                 exp = 0,
                 nature = None,
                 attacks = [TackleAttack],
                 stats = None,
                 isWild = True,
                 heldItem = None):
        if stats is None:
            stats = Stats(level, BaseStats(45, 49, 49, 65, 65, 45))
        if nature is None:
            nature = choice(list(NATURE.__dict__.values()))
        super().__init__(name, "Bulbasaur", level, exp, GROUP.MEDIUM_SLOW, 64, [GrassType()], nature, attacks, stats, isWild, heldItem)