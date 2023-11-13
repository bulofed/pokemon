from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.stats.Stats import Stats
from src.Const import TYPE

class Bulbasaur(Pokemon):
    def __init__(self, name:str = "Bulbasaur", exp:int = 0, attacks:list = [TackleAttack()], stats:Stats = Stats()):
        super().__init__(name, "Bulbasaur", 45, exp, [TYPE.GRASS], attacks, stats)