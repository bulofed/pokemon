from __future__ import annotations
from abc import ABC, abstractmethod
from src.pokemon.type.IType import IType
from src.pokemon.attack.IAttack import IAttack
from src.pokemon.stats.Stats import Stats

from src.Const import GROUP

class IPokemon(ABC):
    @abstractmethod
    def getName(self: IPokemon) -> str:pass
    @abstractmethod
    def getSpecie(self: IPokemon) -> str:pass
    @abstractmethod
    def getHpMax(self: IPokemon) -> int:pass
    @abstractmethod
    def getHp(self: IPokemon) -> int:pass
    @abstractmethod
    def getLevel(self: IPokemon) -> int:pass
    @abstractmethod
    def getExp(self: IPokemon) -> int:pass
    @abstractmethod
    def getExpGroup(self: IPokemon) -> GROUP:pass
    @abstractmethod
    def getExpYielded(self: IPokemon) -> int:pass
    @abstractmethod
    def getTypes(self: IPokemon) -> list[IType]:pass
    @abstractmethod
    def getAttacks(self: IPokemon) -> list[IAttack]:pass
    @abstractmethod
    def getStats(self: IPokemon) -> Stats:pass