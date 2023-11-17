from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class SteelType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.STEEL
        self.weakness = [CType.GRASS,CType.FIRE,CType.ELECTRIK,CType.STEEL]
        self.strength = [CType.FAIRY,CType.STEEL,CType.DIVINE]