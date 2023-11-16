from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType


class WaterType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.WATER
        self.weakness = [CType.GRASS]
        self.strength = [CType.FIRE]
