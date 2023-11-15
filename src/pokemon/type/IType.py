from __future__ import annotations
from abc import ABC, abstractmethod
from src.Const import TYPE

class IType(ABC):
    @abstractmethod
    def getRelation(self: IType, type: TYPE) -> bool:
        pass