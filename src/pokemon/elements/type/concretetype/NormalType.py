from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType


class NormalType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.NORMAL
        self.weakness = [CType.ROCK,CType.STEEL]
        self.strength = [CType.LIGHT,CType.DEMONIC]
        self.immune = [CType.GHOST]
