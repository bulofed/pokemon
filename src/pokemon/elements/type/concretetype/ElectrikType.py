from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class ElectrikType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.ELECTRIK
        self.weakness = [CType.GRASS,CType.ELECTRIK,CType.DRAGON,CType.LIGHT]
        self.strength = [CType.WATER,CType.FLYING]
        self.immune = [CType.GROUND]