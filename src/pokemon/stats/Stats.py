from __future__ import annotations
from random import randint

from src.Const import CATEGORY

class Stats():
    
    def __init__(self: Stats,
                 level: int,
                 baseHp: int,
                 baseAttack: int,
                 baseDefense: int,
                 baseSpecialAttack: int,
                 baseSpecialDefense:int,
                 baseSpeed: int,
                 ivHp: int = randint(0, 31),
                 ivAttack: int = randint(0, 31),
                 ivDefense: int = randint(0, 31),
                 ivSpecialAttack: int = randint(0, 31),
                 ivSpecialDefense: int = randint(0, 31),
                 ivSpeed: int = randint(0, 31),
                 evHp: int = randint(0, 31),
                 evAttack: int = randint(0, 31),
                 evDefense: int = randint(0, 31),
                 evSpecialAttack: int = randint(0, 31),
                 evSpecialDefense: int = randint(0, 31),
                 evSpeed: int = randint(0, 31),
                 ) -> None:
        
        self.baseHp = baseHp
        self.baseAttack = baseAttack
        self.baseDefense = baseDefense
        self.baseSpecialAttack = baseSpecialAttack
        self.baseSpecialDefense = baseSpecialDefense
        self.baseSpeed = baseSpeed
        self.ivHp = ivHp
        self.ivAttack = ivAttack
        self.ivDefense = ivDefense
        self.ivSpecialAttack = ivSpecialAttack
        self.ivSpecialDefense = ivSpecialDefense
        self.ivSpeed = ivSpeed
        self.evHp = evHp
        self.evAttack = evAttack
        self.evDefense = evDefense
        self.evSpecialAttack = evSpecialAttack
        self.evSpecialDefense = evSpecialDefense
        self.evSpeed = evSpeed
        self.level = level
    
    def getBaseHp(self: Stats) -> int:return self.baseHp
    def getBaseAttack(self: Stats) -> int:return self.baseAttack
    def getBaseDefense(self: Stats) -> int:return self.baseDefense
    def getBaseSpecialAttack(self: Stats) -> int:return self.baseSpecialAttack
    def getBaseSpecialDefense(self: Stats) -> int:return self.baseSpecialDefense
    def getBaseSpeed(self: Stats) -> int:return self.baseSpeed
    def getIvHp(self: Stats) -> int:return self.ivHp
    def getIvAttack(self: Stats) -> int:return self.ivAttack
    def getIvDefense(self: Stats) -> int:return self.ivDefense
    def getIvSpecialAttack(self: Stats) -> int:return self.ivSpecialAttack
    def getIvSpecialDefense(self: Stats) -> int:return self.ivSpecialDefense
    def getIvSpeed(self: Stats) -> int:return self.ivSpeed
    def getEvHp(self: Stats) -> int:return self.evHp
    def getEvAttack(self: Stats) -> int:return self.evAttack
    def getEvDefense(self: Stats) -> int:return self.evDefense
    def getEvSpecialAttack(self: Stats) -> int:return self.evSpecialAttack
    def getEvSpecialDefense(self: Stats) -> int:return self.evSpecialDefense
    def getEvSpeed(self: Stats) -> int:return self.evSpeed
    
    def getDefense(self, category: CATEGORY) -> int:
        if category == CATEGORY.PHYSICAL:
            return self.getDefensePhysical()
        elif category == CATEGORY.SPECIAL:
            return self.getDefenseSpecial()
        else:
            return 0
        
    def getDefensePhysical(self: Stats) -> int:
        return int((2 * self.baseDefense + self.ivDefense + self.evDefense / 4) * self.level / 100 + 5)
    
    def getDefenseSpecial(self: Stats) -> int:
        return int((2 * self.baseSpecialDefense + self.ivSpecialDefense + self.evSpecialDefense / 4) * self.level / 100 + 5)
        
    def getAttack(self, category: CATEGORY) -> int:
        if category == CATEGORY.PHYSICAL:
            return self.getAttackPhysical()
        elif category == CATEGORY.SPECIAL:
            return self.getAttackSpecial()
        else:
            return 0
        
    def getAttackPhysical(self: Stats) -> int:
        return int((2 * self.baseAttack + self.ivAttack + self.evAttack / 4) * self.level / 100 + 5)
    
    def getAttackSpecial(self: Stats) -> int:
        return int((2 * self.baseSpecialAttack + self.ivSpecialAttack + self.evSpecialAttack / 4) * self.level / 100 + 5)
    
    def printAllEVs(self: Stats) -> int:
        print('HP: ' + str(self.evHp))
        print('Attack: ' + str(self.evAttack))
        print('Defense: ' + str(self.evDefense))
        print('Special Attack: ' + str(self.evSpecialAttack))
        print('Special Defense: ' + str(self.evSpecialDefense))
        print('Speed: ' + str(self.evSpeed))