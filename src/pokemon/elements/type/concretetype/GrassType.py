from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType


class GrassType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.GRASS
        self.weakness = [CType.FIRE]
        self.strength = [CType.WATER]
