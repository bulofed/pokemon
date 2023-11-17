from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType


class NormalType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.NORMAL
        self.weakness = [CType.ROCK,CType.STEEL]
        self.strength = [CType.LIGHT,CType.DEMONIC]
        self.immune = [CType.GHOST]
