from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType

class GroundType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.GROUND
        self.weakness = [CType.GRASS,CType.BUG]
        self.strength = [CType.FIRE,CType.ELECTRIK,CType.POISON,CType.STEEL,CType.ROCK]
        self.immune = [CType.FLYING]