from src.pokemon.type.IType import IType
from src.Const import RELATION, TYPE

class Type(IType):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = "Type"
        self.weakness:list[TYPE] = []
        self.strength:list[TYPE] = []
        
    def relation(self, type: TYPE) -> RELATION:
        if type in self.weakness:
            return RELATION.WEAK
        elif type in self.strength:
            return RELATION.STRONG
        else:
            return RELATION.NEUTRAL