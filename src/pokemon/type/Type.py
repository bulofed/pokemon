from src.pokemon.type.IType import IType
from src.pokemon.type.CType import CType
from src.Const import RELATION

class Type(IType):
    def __init__(self, name:str = "") -> None:
        super().__init__()
        self.name:CType = name
        self.weakness:list[CType] = []
        self.strength:list[CType] = []
        
    def getRelation(self, type) -> RELATION:
        Type = type.name
        if Type in self.weakness:
            return RELATION.WEAK
        elif Type in self.strength:
            return RELATION.STRONG
        else:
            return RELATION.NEUTRAL