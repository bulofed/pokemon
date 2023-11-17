from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class FairyType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.FAIRY
        self.weakness = [CType.GRASS,CType.POISON,CType.STEEL]
        self.strength = [CType.DRAGON,CType.GHOST,CType.FIGHTING]