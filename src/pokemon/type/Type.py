from src.pokemon.type.IType import IType
from src.Const import RELATION, TYPE

class Type(IType):
    def __init__(self, name:str = "") -> None:
        super().__init__()
        self.name:TYPE = name
        self.weakness:list[TYPE] = []
        self.strength:list[TYPE] = []
        
    def getRelation(self, type) -> RELATION:
        Type = type.name
        if Type in self.weakness:
            return RELATION.WEAK
        elif Type in self.strength:
            return RELATION.STRONG
        else:
            return RELATION.NEUTRAL