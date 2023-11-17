from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType

class DarkType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.DARK
        self.weakness = [CType.FIGHTING,CType.DARK]
        self.strength = [CType.PSYCHIC,CType.GHOST,CType.LIGHT]