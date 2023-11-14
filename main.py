from src.pokemon.concretepokemon.Bulbasaur import Bulbasaur
from src.pokemon.concretepokemon.Charmander import Charmander

if __name__ in "__main__":
    bulbasaur = Bulbasaur()
    charmander = Charmander()
    ember = charmander.getAttacks()[1]
    charmander.attack(bulbasaur, ember)