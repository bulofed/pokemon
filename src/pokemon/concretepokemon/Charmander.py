from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.attack.concreteattack.EmberAttack import EmberAttack
from src.pokemon.stats.Stats import Stats
from src.pokemon.type.concretetype.FireType import FireType
from src.Const import GROUP

class Charmander(Pokemon):
    def __init__(self,
                 name = "Charmander",
                 level = 1,
                 exp = 0,
                 attacks = [TackleAttack(), EmberAttack()],
                 stats = None,
                 isWild = True,
                 heldItem = None):
        if stats is None:
            stats = Stats(level, 39, 52, 43, 60, 50, 65)
        super().__init__(name, "Charmander", level, exp, GROUP.MEDIUM_SLOW, 65, [FireType()], attacks, stats, isWild, heldItem)