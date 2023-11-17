from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class DarkType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.DARK
        self.weakness = [CType.FIGHTING,CType.DARK]
        self.strength = [CType.PSYCHIC,CType.GHOST,CType.LIGHT]