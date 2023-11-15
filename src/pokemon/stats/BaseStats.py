class BaseStats:
    def __init__(self, hp, attack, defense, special_attack, special_defense, speed):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        
    def get_hp(self):return self.hp
    def get_attack(self):return self.attack
    def get_defense(self):return self.defense
    def get_special_attack(self):return self.special_attack
    def get_special_defense(self):return self.special_defense
    def get_speed(self):return self.speed
    def getHp(self):return self.hp
    def getAttack(self):return self.attack
    def getDefense(self):return self.defense
    def getSpecialAttack(self):return self.special_attack
    def getSpecialDefense(self):return self.special_defense
    def getSpeed(self):return self.speed