from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class DivineType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.DIVINE
        self.weakness = [CType.LIGHT,CType.NORMAL]
        self.strength = [CType.DEMONIC,CType.DARK,CType.GRASS,CType.FIRE,CType.WATER,CType.DIVINE]