from src.pokemon.concretepokemon.Bulbasaur import Bulbasaur
from src.pokemon.concretepokemon.Charmander import Charmander
from src.Const import NATURE_TABLE, NATURE

if __name__ in "__main__":
    print(NATURE_TABLE[NATURE.HARDY])
    bulbasaur = Bulbasaur(level=5, isWild=False)
    charmander = Charmander(level=5, isWild=False)
    ember = charmander.getAttacks()[1]
    charmander.attack(bulbasaur, ember)