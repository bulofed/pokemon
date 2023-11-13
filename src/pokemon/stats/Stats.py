from __future__ import annotations
from random import randint

from src.Const import CATEGORY

class Stats:
    def __init__(self: Stats, level: int = 1) -> None:
        self.ivHp = randint(0, 31)
        self.ivAttack = randint(0, 31)
        self.ivDefense = randint(0, 31)
        self.ivSpecialAttack = randint(0, 31)
        self.ivSpecialDefense = randint(0, 31)
        self.ivSpeed = randint(0, 31)
        self.evHp = 1
        self.evAttack = 1
        self.evDefense = 1
        self.evSpecialAttack = 1
        self.evSpecialDefense = 1
        self.evSpeed = 1
        self.level = level
    
    def setIvHp(self: Stats, ivHp: int) -> None:
        self.ivHp = ivHp
        
    def setIvAttack(self: Stats, ivAttack: int) -> None:
        self.ivAttack = ivAttack
        
    def setIvDefense(self: Stats, ivDefense: int) -> None:
        self.ivDefense = ivDefense
    
    def setIvSpecialAttack(self: Stats, ivSpecialAttack: int) -> None:
        self.ivSpecialAttack = ivSpecialAttack
        
    def setIvSpecialDefense(self: Stats, ivSpecialDefense: int) -> None:
        self.ivSpecialDefense = ivSpecialDefense
        
    def setIvSpeed(self: Stats, ivSpeed: int) -> None:
        self.ivSpeed = ivSpeed
        
    def setEvHp(self: Stats, evHp: int) -> None:
        self.evHp = evHp
        
    def setEvAttack(self: Stats, evAttack: int) -> None:
        self.evAttack = evAttack
        
    def setEvDefense(self: Stats, evDefense: int) -> None:
        self.evDefense = evDefense
        
    def setEvSpecialAttack(self: Stats, evSpecialAttack: int) -> None:
        self.evSpecialAttack = evSpecialAttack
        
    def setEvSpecialDefense(self: Stats, evSpecialDefense: int) -> None:
        self.evSpecialDefense = evSpecialDefense
        
    def setEvSpeed(self: Stats, evSpeed: int) -> None:
        self.evSpeed = evSpeed
        
    def getIvHp(self: Stats) -> int:
        return self.ivHp

    def getIvAttack(self: Stats) -> int:
        return self.ivAttack
    
    def getIvDefense(self: Stats) -> int:
        return self.ivDefense
    
    def getIvSpecialAttack(self: Stats) -> int:
        return self.ivSpecialAttack
    
    def getIvSpecialDefense(self: Stats) -> int:
        return self.ivSpecialDefense
    
    def getIvSpeed(self: Stats) -> int:
        return self.ivSpeed
    
    def getEvHp(self: Stats) -> int:
        return self.evHp
    
    def getEvAttack(self: Stats) -> int:
        return self.evAttack
    
    def getEvDefense(self: Stats) -> int:
        return self.evDefense
    
    def getEvSpecialAttack(self: Stats) -> int:
        return self.evSpecialAttack
    
    def getEvSpecialDefense(self: Stats) -> int:
        return self.evSpecialDefense
    
    def getEvSpeed(self: Stats) -> int:
        return self.evSpeed
    
    def getDefense(self, category: CATEGORY) -> int:
        if category == CATEGORY.PHYSICAL:
            return self.getDefensePhysical()
        elif category == CATEGORY.SPECIAL:
            return self.getDefenseSpecial()
        else:
            return 0
        
    def getDefensePhysical(self: Stats) -> int:
        return int((2 * 45 + self.ivDefense + self.evDefense / 4) * self.level / 100 + 5)
    
    def getDefenseSpecial(self: Stats) -> int:
        return int((2 * 45 + self.ivSpecialDefense + self.evSpecialDefense / 4) * self.level / 100 + 5)
        
    def getAttack(self, category: CATEGORY) -> int:
        if category == CATEGORY.PHYSICAL:
            return self.getAttackPhysical()
        elif category == CATEGORY.SPECIAL:
            return self.getAttackSpecial()
        else:
            return 0
        
    def getAttackPhysical(self: Stats) -> int:
        return int((2 * 45 + self.ivAttack + self.evAttack / 4) * self.level / 100 + 5)
    
    def getAttackSpecial(self: Stats) -> int:
        return int((2 * 45 + self.ivSpecialAttack + self.evSpecialAttack / 4) * self.level / 100 + 5)