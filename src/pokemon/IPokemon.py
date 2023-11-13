from __future__ import annotations
from abc import ABC, abstractmethod
from src.pokemon.type.IType import IType
from src.pokemon.attack.IAttack import IAttack
from src.pokemon.stats.Stats import Stats

class IPokemon(ABC):
    
    @abstractmethod
    def getName(self: IPokemon) -> str:
        pass
    
    @abstractmethod
    def getSpecie(self: IPokemon) -> str:
        pass
    
    @abstractmethod
    def getHpMax(self: IPokemon) -> int:
        pass
    
    @abstractmethod
    def getHp(self: IPokemon) -> int:
        pass
    
    @abstractmethod
    def getExp(self: IPokemon) -> int:
        pass
    
    @abstractmethod
    def getTypes(self: IPokemon) -> list[IType]:
        pass
    
    @abstractmethod
    def getAttacks(self: IPokemon) -> list[IAttack]:
        pass
    
    @abstractmethod
    def getStats(self: IPokemon) -> Stats:
        pass
    
    @abstractmethod
    def addHp(self: IPokemon, hp: int) -> None:
        pass
    
    @abstractmethod
    def setStats(self: IPokemon, stats: Stats) -> None:
        pass
    
    @abstractmethod
    def addExp(self: IPokemon, exp: int) -> None:
        pass
    
    @abstractmethod
    def isAlive(self: IPokemon) -> bool:
        pass
    
    @abstractmethod
    def addAttack(self: IPokemon, attack: IAttack, attackToReplace: IAttack = None) -> None:
        pass
    
    @abstractmethod
    def removeAttack(self: IPokemon, attack: IAttack) -> None:
        pass