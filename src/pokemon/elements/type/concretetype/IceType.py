from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType
class IceType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.ICE
        self.weakness = [CType.WATER,CType.STEEL,CType.FIRE,CType.ICE]
        self.strength = [CType.GRASS,CType.ICE,CType.GROUND,CType.FLYING,CType.LIGHT]