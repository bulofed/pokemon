from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.stats.Stats import Stats
from src.Const import GROUP
from src.pokemon.type.concretetype.GrassType import GrassType

class Bulbasaur(Pokemon):
    def __init__(self,
                 name = "Bulbasaur",
                 level = 1,
                 exp = 0,
                 attacks = [TackleAttack],
                 stats = None,
                 isWild = True,
                 heldItem = None):
        if stats is None:
            stats = Stats(level, 45, 49, 49, 65, 65, 45)
        super().__init__(name, "Bulbasaur", level, exp, GROUP.MEDIUM_SLOW, 64, [GrassType()], attacks, stats, isWild, heldItem)