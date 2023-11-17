from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType

class DragonType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.DRAGON
        self.weakness = [CType.STEEL,CType.LIGHT]
        self.strength = [CType.DRAGON]
        self.immune = [CType.FAIRY]