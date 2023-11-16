from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.CType import CType
from src.pokemon.elements.type.CRelation import CRelation


class Type(IType):
    def __init__(self, name: str = "") -> None:
        super().__init__()
        self.name: CType = name
        self.weakness: list[CType] = []
        self.strength: list[CType] = []

    def getRelation(self, type) -> CRelation:
        Type = type.name
        if Type in self.weakness:
            return CRelation.WEAK
        elif Type in self.strength:
            return CRelation.STRONG
        else:
            return CRelation.NEUTRAL
