from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class BugType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.BUG
        self.weakness = [CType.FIRE,CType.FLYING,CType.ROCK,CType.DARK,CType.STEEL,CType.FAIRY]
        self.strength = [CType.GRASS,CType.PSYCHIC,CType.DARK]