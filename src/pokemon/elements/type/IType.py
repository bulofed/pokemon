from __future__ import annotations
from abc import ABC, abstractmethod
from src.pokemon.elements.type.CType import CType


class IType(ABC):
    @abstractmethod
    def getRelation(self: IType, type: CType) -> bool:
        pass
