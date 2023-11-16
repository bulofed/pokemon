from __future__ import annotations

from src.pokemon.IPokemon import IPokemon
from src.pokemon.attack.IAttack import IAttack
from src.pokemon.type.IType import IType
from src.item.helditem.IHeldItem import IHeldItem
from src.pokemon.status.IStatus import IStatus

from src.pokemon.stats.Stats import Stats
from src.pokemon.type.CRelation import CRelation

from src.Const import GROUP, NATURE

from src.Formula import expFormula, gainFormula, criticalFormula, hpFormula,statFormula

from random import randint

class Pokemon(IPokemon):
    def __init__(self,
                 name: str,
                 specie: str,
                 level: int,
                 exp: int,
                 expGroup:GROUP,
                 expYielded:int,
                 types: list[IType],
                 nature: NATURE,
                 attacks: list[IAttack],
                 stats: Stats = None,
                 isWild: bool = True,
                 heldItem: IHeldItem = None,
                 ):
        self.name = name
        self.specie = specie
        self.stats = stats if stats is not None else Stats(level, nature)
        self.hpMax = hpFormula(self.stats.getBaseStats().getHp(), self.stats.getEVStats().getHp(), self.stats.getIVStats().getHp(), level)
        self.hp = self.hpMax
        self.level = level
        self.exp = exp
        self.expGroup = expGroup
        self.expYielded = expYielded
        self.types = types
        self.nature = nature
        self.attacks = attacks
        self.wild = isWild
        self.heldItem = heldItem
        self.status:list[IStatus] = []
        
    # Getters
        
    def getName(self) -> str:return self.name
    def getSpecie(self) -> str:return self.specie
    def getHpMax(self) -> int:return self.hpMax
    def getHp(self) -> int:return self.hp
    def getLevel(self) -> int:return self.level
    def getExp(self) -> int:return self.exp
    def getExpGroup(self: IPokemon) -> GROUP:return self.expGroup
    def getExpYielded(self: IPokemon) -> int:return self.expYielded
    def getTypes(self) -> list[IType]:return self.types
    def getNature(self) -> NATURE:return self.nature
    def getAttacks(self) -> list[IAttack]:return self.attacks
    def getStats(self) -> Stats:return self.stats
    def getHeldItem(self) -> IHeldItem:return self.heldItem
    def getStatus(self) -> list[IStatus]:return self.status
    def isWild(self) -> bool:return self.wild
    
    def addHp(self, hp: int) -> None:
        '''Add hp to the pokemon and prevent it from exceeding the max hp
        
        args:
            hp (int): The hp to add'''
            
        self.hp += hp
        self.hp = min(self.hp, self.hpMax)
        
    def addExp(self, exp: int) -> None:
        '''Add exp to the pokemon and level it up if it has enough exp
        
        args:
            exp (int): The exp to add'''
        
        if self.level == 100:
            return self.level
        oldLevel = self.level
        newLevel, remainingExp = expFormula(self.expGroup, self.level, exp)
        self.level = newLevel
        self.stats.level = newLevel
        self.exp = remainingExp
        return oldLevel
        
    def isAlive(self) -> bool:
        '''Return True if the pokemon is alive, False otherwise'''
        
        return self.hp > 0

    def addAttack(self, attack: IAttack, attackToReplace: IAttack = None) -> None:
        '''Add an attack to the pokemon and remove the attackToReplace if it is not None
        
        args:
            attack (IAttack): The attack to add
            attackToReplace (IAttack): The attack to remove'''
            
        self.attacks.append(attack)
        if attackToReplace is not None:
            self.attacks.remove(attackToReplace)
            
    def removeAttack(self, attack: IAttack) -> None:
        '''Remove an attack from the pokemon
        
        args:
            attack (IAttack): The attack to remove'''
            
        self.attacks.remove(attack)
        
    def attack(self, target: Pokemon, attack: IAttack) -> None:
        '''Attack the target with the attack
        
        args:
            target (Pokemon): The pokemon to attack
            attack (IAttack): The attack to use'''

        self.consumePP(attack)
        power = attack.getPower()
        a = self.stats.getAttack(attack.getCategory())
        d = target.stats.getDefense(attack.getCategory())
        stab = self.calculateStabMultiplier(attack)
        critical_hit = criticalFormula(attack.getStage(), self.heldItem, self.status)
        type_multipliers = self.calculateTypeMultipliers(attack, target.types)

        type1, type2 = type_multipliers[:2] + [1] * (2 - len(type_multipliers))
        multiplier = self.calculateTotalMultiplier(type1, type2)

        efficacityMessage = self.calculateEfficacityMessage(multiplier, target)

        random_factor = self.calculateRandomFactor()

        damage = self.calculateDamage(power, a, d, stab, multiplier, random_factor, critical_hit)
        
        self.inflictDamage(target, damage, attack, critical_hit, efficacityMessage)

    def consumePP(self, attack: IAttack) -> None:
        '''Reduce PP of the attack'''
        attack.execute()

    def calculateStabMultiplier(self, attack: IAttack) -> float:
        '''Calculate STAB multiplier'''
        return 1.5 if attack.getType() in self.types else 1
        
    def calculateTypeMultipliers(self, attack: IAttack, target_types: list[str]) -> list[float]:
        '''Calculate type multipliers'''
        type_multipliers = []
        for target_type in target_types:
            relation = attack.getType().getRelation(target_type)
            type_multipliers.append(self.calculateTypeMultiplier(relation))
        return type_multipliers

    def calculateTypeMultiplier(self, relation: CRelation) -> float:
        '''Calculate individual type multiplier'''
        if relation == CRelation.STRONG:
            return 2
        elif relation == CRelation.WEAK:
            return 0.5
        elif relation == CRelation.IMMUNE:
            return 0
        else:
            return 1

    def calculateTotalMultiplier(self, type1: float, type2: float) -> float:
        '''Calculate total type multiplier'''
        return type1 * type2 if type2 is not None else type1

    def calculateEfficacityMessage(self, multiplier: float, target: Pokemon) -> str:
        '''Calculate the efficacy message based on multiplier'''
        if multiplier == 0:
            return f"It doesn't affect {target.getName()}"
        elif multiplier in {0.25, 0.5}:
            return "It's not very effective..."
        elif multiplier in {2, 4}:
            return "It's super effective !"
        else:
            return ""

    def calculateRandomFactor(self) -> float:
        '''Calculate a random factor for damage'''
        return randint(85, 100) / 100

    def calculateDamage(self, power: int, a: int, d: int, stab: float, multiplier: float, random_factor: float, critical_hit: bool) -> int:
        '''Calculate the damage inflicted'''
        base_damage = (((2 * self.level / 5) + 2) * power * (a / d) / 50) + 2
        damage = int(base_damage * stab * multiplier * random_factor)
        return damage * 2 if critical_hit else damage

    def inflictDamage(self, target: Pokemon, damage: int, attack: IAttack, critical_hit: bool, efficacityMessage: str) -> None:
        '''Inflict damage to the target and print the results'''
        target.addHp(-damage)
        print(f'{self.getName()} used {attack.getName()}')
        if critical_hit:
            print("Critical hit !")
        print(efficacityMessage)
        if damage > 0:
            print(f'{target.getName()} took {damage} damage\n')
        if not target.isAlive():
            self.handleFaintedTarget(target)

    def handleFaintedTarget(self, target: Pokemon) -> None:
        '''Handle actions when the target faints'''
        expYielded = gainFormula(target.wild, target.getExpYielded(), target.getLevel())
        oldLevel = self.addExp(expYielded)
        print(f'{target.getName()} fainted\n{self.getName()} gained {expYielded} exp.\n')
        if self.level > oldLevel:
            self.levelUp(target)

    def levelUp(self) -> None:
        '''Handle actions when the attacker levels up'''
        print(f'{self.getName()} grew to level {self.level} !\n')
        new_stat: dict[str, int] = statFormula(
            self.stats.getBaseStats().getStats(),
            self.stats.getEVStats().getStats(),
            self.stats.getIVStats().getStats(),
            self.level,
            self.nature
        )
        self.stats.setStats(new_stat)