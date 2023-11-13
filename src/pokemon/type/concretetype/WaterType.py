from src.pokemon.type.IType import IType
from src.Const import TYPE, RELATION

class WaterType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name:TYPE = TYPE.WATER
        self.weakness:list[TYPE] = [TYPE.GRASS]
        self.strength:list[TYPE] = [TYPE.FIRE]
        
    def relation(self, type: TYPE) -> RELATION:
        return super().relation(type)