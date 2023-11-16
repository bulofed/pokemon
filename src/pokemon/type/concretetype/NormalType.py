from src.pokemon.type.Type import Type
from src.pokemon.type.CType import CType

class NormalType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.NORMAL
        self.weakness = []
        self.strength = []