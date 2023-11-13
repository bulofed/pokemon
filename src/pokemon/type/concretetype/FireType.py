from src.pokemon.type.Type import Type
from src.Const import TYPE, RELATION

class FireType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name:TYPE = TYPE.FIRE
        self.weakness:list[TYPE] = [TYPE.WATER]
        self.strength:list[TYPE] = [TYPE.GRASS]
        
    def relation(self, type: TYPE) -> RELATION:
        return super().relation(type)