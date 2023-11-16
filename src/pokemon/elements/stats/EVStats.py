from src.pokemon.elements.stats.CStats import CStats


class EVStats:
    def __init__(self,
                 hp=1,
                 attack=1,
                 defense=1,
                 special_attack=1,
                 special_defense=1,
                 speed=1
                 ):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def getHp(self): return self.hp
    def getAttack(self): return self.attack
    def getDefense(self): return self.defense
    def getSpecialAttack(self): return self.special_attack
    def getSpecialDefense(self): return self.special_defense
    def getSpeed(self): return self.speed

    def getStats(self): return {CStats.HP: self.hp,
                                CStats.ATTACK: self.attack,
                                CStats.SPECIAL_ATTACK: self.special_attack,
                                CStats.DEFENSE: self.defense,
                                CStats.SPECIAL_DEFENSE: self.special_defense,
                                CStats.SPEED: self.speed
                                }
