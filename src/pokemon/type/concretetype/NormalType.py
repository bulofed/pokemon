from src.pokemon.type.Type import Type
from src.Const import TYPE

class NormalType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = TYPE.NORMAL
        self.weakness = []
        self.strength = []