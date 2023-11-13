from src.pokemon.type.Type import Type
from src.Const import TYPE, RELATION

class FireType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name:TYPE = TYPE.NORMAL
        self.weakness:list[TYPE] = []
        self.strength:list[TYPE] = []
        
    def relation(self, type: TYPE) -> RELATION:
        return super().relation(type)