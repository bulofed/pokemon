from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType

class RockType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.ROCK
        self.weakness = [CType.WATER,CType.GROUND,CType.ROCK,CType.DRAGON]
        self.strength = [CType.STEEL,CType.GROUND,CType.FIGHTING]