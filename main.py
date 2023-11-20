from src.pokemon.concretepokemon.Bulbasaur import Bulbasaur
from src.pokemon.concretepokemon.Charmander import Charmander

if __name__ in "__main__":
    bulbasaur = Bulbasaur(name='Caca', level=15, isWild=False, exp=2000)
    charmander = Charmander(level=100, isWild=False)
    tackle = charmander.getAttacks()[0]
    while charmander.isAlive():
        bulbasaur.attack(charmander, tackle)