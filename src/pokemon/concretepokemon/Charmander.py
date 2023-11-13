from src.pokemon.Pokemon import Pokemon
from src.pokemon.attack.concreteattack.TackleAttack import TackleAttack
from src.pokemon.attack.concreteattack.EmberAttack import EmberAttack
from src.pokemon.stats.Stats import Stats
from src.Const import TYPE

class Charmander(Pokemon):
    def __init__(self, name:str = "Charmander", exp:int = 0, attacks:list = [TackleAttack(), EmberAttack()], stats:Stats = Stats()):
        super().__init__(name, "Charmander", 45, exp, [TYPE.FIRE], attacks, stats)