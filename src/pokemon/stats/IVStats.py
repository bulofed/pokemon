from random import randint

from src.Const import STATS

class IVStats:
    def __init__(self,
                 hp=randint(0, 31),
                 attack=randint(0, 31),
                 defense=randint(0, 31),
                 special_attack=randint(0, 31),
                 special_defense=randint(0, 31),
                 speed=randint(0, 31)
                 ):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        
    def getHp(self):return self.hp
    def getAttack(self):return self.attack
    def getDefense(self):return self.defense
    def getSpecialAttack(self):return self.special_attack
    def getSpecialDefense(self):return self.special_defense
    def getSpeed(self):return self.speed
    def getStats(self):return { STATS.HP : self.hp,
                                STATS.ATTACK : self.attack,
                                STATS.SPECIAL_ATTACK : self.special_attack,
                                STATS.DEFENSE : self.defense,
                                STATS.SPECIAL_DEFENSE : self.special_defense,
                                STATS.SPEED : self.speed
                                }