from src.pokemon.type.Type import Type
from src.pokemon.type.CType import CType

class FireType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.FIRE
        self.weakness = [CType.WATER]
        self.strength = [CType.GRASS]