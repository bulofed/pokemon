from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.attack.concreteattack.EmberAttack import EmberAttack
from src.pokemon.stats.Stats import Stats
from src.Const import TYPE, GROUP

class Charmander(Pokemon):
    def __init__(self, name:str = "Charmander", level:int = 1, exp:int = 0, expGroup:GROUP = GROUP.MEDIUM_SLOW, expYielded:int = 65, attacks:list = [TackleAttack(), EmberAttack()], stats:Stats = Stats()):
        super().__init__(name, "Charmander", 45, level, exp, expGroup, expYielded, [TYPE.FIRE], attacks, stats)