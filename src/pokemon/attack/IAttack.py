from __future__ import annotations
from abc import ABC, abstractmethod
from src.Const import CATEGORY
from src.pokemon.type.IType import IType

class IAttack(ABC):
    @abstractmethod
    def getName(self: IAttack) -> str:pass
    @abstractmethod
    def getPower(self: IAttack) -> int:pass
    @abstractmethod
    def getCategory(self: IAttack) -> CATEGORY:pass
    @abstractmethod
    def getType(self: IAttack) -> IType:pass
    @abstractmethod
    def getStage(self: IAttack) -> int:pass
    @abstractmethod
    def getAccuracy(self: IAttack) -> int:pass
    @abstractmethod
    def execute(self: IAttack) -> None:pass