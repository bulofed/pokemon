from src.pokemon.type.IType import IType
from src.Const import TYPE

class WaterType(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name = TYPE.WATER
        self.weakness = [TYPE.GRASS]
        self.strength = [TYPE.FIRE]