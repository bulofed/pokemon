from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class FightingType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.FIGHTING
        self.weakness = [CType.FAIRY,CType.BUG,CType.PSYCHIC,CType.FLYING,CType.POISON,CType.DIVINE]
        self.strength = [CType.ICE,CType.NORMAL,CType.ROCK,CType.STEEL,CType.DARK]
        self.immune = [CType.GHOST]