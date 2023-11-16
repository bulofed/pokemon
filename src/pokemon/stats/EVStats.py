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
        
    def getHp(self):return self.hp
    def getAttack(self):return self.attack
    def getDefense(self):return self.defense
    def getSpecialAttack(self):return self.special_attack
    def getSpecialDefense(self):return self.special_defense
    def getSpeed(self):return self.speed
    def getStats(self):return {"HP" : self.hp,
                                 "ATK" : self.attack,
                                  "SP.ATK" : self.special_attack,
                                  "DEF" : self.defense,
                                  "SP.DEF" : self.special_defense,
                                  "SPD" : self.speed }