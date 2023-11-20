from src.pokemon.Pokemon import Pokemon
from src.pokemon.elements.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.elements.stats.Stats import Stats
from src.pokemon.elements.stats.BaseStats import BaseStats
from src.Const import NATURE_LIST
from src.pokemon.elements.type.concretetype.GrassType import GrassType
from src.pokemon.elements.type.concretetype.PoisonType import PoisonType
from src.pokemon.elements.exp.CGroup import CGroup
from random import choice


class Ivysaur(Pokemon):
    def __init__(self,
                 name="Ivysaur",
                 level=16,
                 exp=0,
                 nature=None,
                 attacks=None,
                 stats=None,
                 isWild=True,
                 heldItem=None):
        if attacks is None:
            attacks = [TackleAttack()]
        if nature is None:
            nature = choice(NATURE_LIST)
        if stats is None:
            stats = Stats(level, nature, BaseStats(60, 62, 63, 80, 80, 60))
        super().__init__(name, "Ivysaur", level, exp, CGroup.MEDIUM_SLOW,
                         64, [GrassType(), PoisonType()], nature, attacks, stats, isWild, heldItem)
