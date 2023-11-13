from __future__ import annotations
from abc import ABC, abstractmethod

class IType(ABC):
    
    @abstractmethod
    def relation(self: IType, type: IType) -> bool:
        pass