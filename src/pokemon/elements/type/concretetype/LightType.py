from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType

class LightType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.LIGHT
        self.weakness = [CType.GRASS,CType.DIVINE,CType.LIGHT]
        self.strength = [CType.DARK,CType.FIGHTING,CType.DEMONIC]