from __future__ import annotations
from random import randint

class Stats:
    def __init__(self: Stats) -> None:
        self.ivHp = randint(0, 31)
        self.ivAttack = randint(0, 31)
        self.ivDefense = randint(0, 31)
        self.ivSpecialAttack = randint(0, 31)
        self.ivSpecialDefense = randint(0, 31)
        self.ivSpeed = randint(0, 31)
        self.evHp = 0
        self.evAttack = 0
        self.evDefense = 0
        self.evSpecialAttack = 0
        self.evSpecialDefense = 0
        self.evSpeed = 0
    
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