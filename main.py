from src.pokemon.concretepokemon.Bulbasaur import Bulbasaur
from src.pokemon.concretepokemon.Charmander import Charmander

if __name__ in "__main__":
    bulbasaur = Bulbasaur(level=100, isWild=False)
    charmander = Charmander(level=5, isWild=False)
    ember = charmander.getAttacks()[1]
    while bulbasaur.isAlive():
        charmander.attack(bulbasaur, ember)