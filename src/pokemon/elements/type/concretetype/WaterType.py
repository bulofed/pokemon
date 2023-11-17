from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType


class WaterType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.WATER
        self.weakness = [CType.GRASS]
        self.strength = [CType.FIRE]
