from __future__ import annotations
from abc import ABC, abstractmethod
from src.pokemon.attack.CCategory import CCategory
from src.pokemon.type.IType import IType

class IAttack(ABC):
    @abstractmethod
    def getName(self: IAttack) -> str:pass
    @abstractmethod
    def getPower(self: IAttack) -> int:pass
    @abstractmethod
    def getCategory(self: IAttack) -> CCategory:pass
    @abstractmethod
    def getType(self: IAttack) -> IType:pass
    @abstractmethod
    def getStage(self: IAttack) -> int:pass
    @abstractmethod
    def getAccuracy(self: IAttack) -> int:pass
    @abstractmethod
    def execute(self: IAttack) -> None:pass