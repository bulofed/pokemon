from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType

class FlyingType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.FLYING
        self.weakness = [CType.ELECTRIK,CType.ROCK,CType.STEEL]
        self.strength = [CType.GRASS,CType.FIGHTING,CType.BUG,CType.STEEL]