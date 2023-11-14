from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.stats.Stats import Stats
from src.Const import GROUP
from src.item.helditem.HeldItem import HeldItem
from src.pokemon.type.concretetype.GrassType import GrassType

class Bulbasaur(Pokemon):
    def __init__(self,
                 name:str = "Bulbasaur",
                 level:int = 1,
                 exp:int = 0,
                 attacks:list = [TackleAttack()],
                 stats:Stats = Stats(),
                 isWild:bool = True,
                 heldItem:HeldItem = None):
        super().__init__(name, "Bulbasaur", 45, level, exp, GROUP.MEDIUM_SLOW, 64, [GrassType()], attacks, stats, isWild, heldItem, [])