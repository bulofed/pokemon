from src.pokemon.type.Type import Type
from src.Const import TYPE

class GrassType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name:TYPE = TYPE.GRASS
        self.weakness:list[TYPE] = [TYPE.FIRE]
        self.strength:list[TYPE] = [TYPE.WATER]