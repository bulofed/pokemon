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
                 stats = Stats(),
                 isWild = True,
                 heldItem = None):
        super().__init__(name, "Bulbasaur", 45, level, exp, GROUP.MEDIUM_SLOW, 64, [GrassType()], attacks, stats, isWild, heldItem)