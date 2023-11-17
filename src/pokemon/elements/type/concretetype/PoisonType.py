from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class PoisonType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.POISON
        self.weakness = [CType.ROCK,CType.GROUND,CType.GHOST,CType.POISON]
        self.strength = [CType.GRASS,CType.FAIRY]
        self.immune = [CType.STEEL,CType.POISON]