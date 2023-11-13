from __future__ import annotations
from abc import ABC, abstractmethod

class IType(ABC):
    
    @abstractmethod
    def getRelation(self: IType, type: IType) -> bool:
        pass