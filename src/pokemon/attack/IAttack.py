from __future__ import annotations
from abc import ABC, abstractmethod

class IAttack(ABC):
    
    @abstractmethod
    def execute(self: IAttack) -> None:
        pass
    
    @abstractmethod
    def getPower(self: IAttack) -> int:
        pass