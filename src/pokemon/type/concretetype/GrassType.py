from src.pokemon.type.Type import Type
from src.Const import TYPE

class GrassType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = TYPE.GRASS
        self.weakness = [TYPE.FIRE]
        self.strength = [TYPE.WATER]