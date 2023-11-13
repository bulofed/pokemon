from __future__ import annotations
from abc import ABC, abstractmethod
from src.Const import TYPE, CATEGORY

class IAttack(ABC):
    
    @abstractmethod
    def execute(self: IAttack) -> None:
        pass
    
    @abstractmethod
    def getPower(self: IAttack) -> int:
        pass
    
    @abstractmethod
    def getCategory(self: IAttack) -> CATEGORY:
        pass
    
    @abstractmethod
    def getType(self: IAttack) -> TYPE:
        pass