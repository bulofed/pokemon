from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.stats.Stats import Stats
from src.Const import TYPE, GROUP

class Bulbasaur(Pokemon):
    def __init__(self, name:str = "Bulbasaur", level:int = 1, exp:int = 0, expGroup:GROUP = GROUP.MEDIUM_SLOW, expYielded:int = 64, attacks:list = [TackleAttack()], stats:Stats = Stats()):
        super().__init__(name, "Bulbasaur", 45, level, exp, expGroup, expYielded, [TYPE.GRASS], attacks, stats)