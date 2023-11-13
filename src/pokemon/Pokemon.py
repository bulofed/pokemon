from __future__ import annotations

from src.pokemon.IPokemon import IPokemon
from src.pokemon.attack.IAttack import IAttack
from src.pokemon.type.IType import IType

from src.pokemon.stats.Stats import Stats
from src.pokemon.type.Type import Type

from src.Const import RELATION

from random import randint

class Pokemon(IPokemon):
    def __init__(self, name: str, specie: str, hpMax: int, level: int, exp: int, types: list[IType], attacks: list[IAttack], stats: Stats = None):
        self.name = name
        self.specie = specie
        self.hpMax = hpMax
        self.hp = hpMax
        self.level = level
        self.exp = exp
        self.types = types
        self.attacks = attacks
        self.stats = stats if stats is not None else Stats(level)
        
    def getName(self) -> str:
        return self.name
    
    def getSpecie(self) -> str:
        return self.specie
    
    def getHpMax(self) -> int:
        return self.hpMax
    
    def getHp(self) -> int:
        return self.hp
    
    def getLevel(self) -> int:
        return self.level
    
    def getExp(self) -> int:
        return self.exp
    
    def getTypes(self) -> list[IType]:
        return self.types
    
    def getAttacks(self) -> list[IAttack]:
        return self.attacks
    
    def getStats(self) -> Stats:
        return self.stats
    
    def addHp(self, hp: int) -> None:
        self.hp += hp
        
    def setStats(self, stats: Stats) -> None:
        self.stats = stats
        
    def addExp(self, exp: int) -> None:
        self.exp += exp
        
    def isAlive(self) -> bool:
        return self.hp > 0

    def addAttack(self, attack: IAttack, attackToReplace: IAttack = None) -> None:
        self.attacks.append(attack)
        if attackToReplace is not None:
            self.attacks.remove(attackToReplace)
            
    def removeAttack(self, attack: IAttack) -> None:
        self.attacks.remove(attack)
        
    def attack(self, target: Pokemon, attack: IAttack) -> None:
        
        attack.execute()
        
        power = attack.getPower()
        a = self.stats.getAttack(attack.getCategory())
        d = target.stats.getDefense(attack.getCategory())
        stab = 1.5 if attack.getType() in self.types else 1
        type_multipliers = []

        for target_type in target.types:
            relation = Type(attack.getType()).getRelation(target_type)
            
            if relation == RELATION.STRONG:
                type_multipliers.append(2)
            elif relation == RELATION.WEAK:
                type_multipliers.append(0.5)
            else:
                type_multipliers.append(1)

        type1, type2 = type_multipliers[:2] + [1] * (2 - len(type_multipliers))

        random = (randint(85, 100)/100)
        
        damage = ((((2*self.level/5)+2)*power*(a/d)/50)+2)*stab*type1*type2*random
        
        target.addHp(-int(damage))