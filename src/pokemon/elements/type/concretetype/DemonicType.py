from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class DemonicType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.DEMONIC
        self.weakness = [CType.DARK]
        self.strength = [CType.DIVINE,CType.LIGHT,CType.PSYCHIC,CType.FAIRY]