from __future__ import annotations

from src.pokemon.IPokemon import IPokemon

from src.pokemon.attack.IAttack import IAttack
from src.pokemon.type.IType import IType
from src.pokemon.stats.Stats import Stats

class Pokemon(IPokemon):
    def __init__(self: Pokemon, name: str, specie: str, hpMax: int, exp: int, types: list[IType], attacks: list[IAttack], stats: Stats = Stats()):
        self.name = name
        self.specie = specie
        self.hpMax = hpMax
        self.hp = hpMax
        self.exp = exp
        self.types = types
        self.attacks = attacks
        self.stats = stats
        
    def getName(self: Pokemon) -> str:
        return self.name
    
    def getSpecie(self: Pokemon) -> str:
        return self.specie
    
    def getHpMax(self: Pokemon) -> int:
        return self.hpMax
    
    def getHp(self: Pokemon) -> int:
        return self.hp
    
    def getExp(self: Pokemon) -> int:
        return self.exp
    
    def getTypes(self: Pokemon) -> list[IType]:
        return self.types
    
    def getAttacks(self: Pokemon) -> list[IAttack]:
        return self.attacks
    
    def getStats(self: Pokemon) -> Stats:
        return self.stats
    
    def addHp(self: Pokemon, hp: int) -> None:
        self.hp += hp
        
    def setStats(self: Pokemon, stats: Stats) -> None:
        self.stats = stats
        
    def addExp(self: Pokemon, exp: int) -> None:
        self.exp += exp
        
    def isAlive(self: Pokemon) -> bool:
        return self.hp > 0

    def addAttack(self: Pokemon, attack: IAttack, attackToReplace: IAttack = None) -> None:
        self.attacks.append(attack)
        if attackToReplace is not None:
            self.attacks.remove(attackToReplace)
            
    def removeAttack(self: Pokemon, attack: IAttack) -> None:
        self.attacks.remove(attack)
        
    def attack(self: Pokemon, target: Pokemon, attack: IAttack) -> None:
        attack.execute()
        target.hp -= attack.getPower()