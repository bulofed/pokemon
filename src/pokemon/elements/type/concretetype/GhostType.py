from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType

class GhostType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.GHOST
        self.weakness = [CType.DARK]
        self.strength = [CType.GHOST,CType.PSYCHIC,CType.BUG,CType.STEEL]
        self.immune = [CType.NORMAL,CType.GHOST]