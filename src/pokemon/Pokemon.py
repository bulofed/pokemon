from __future__ import annotations

from src.pokemon.IPokemon import IPokemon
from src.pokemon.attack.IAttack import IAttack
from src.pokemon.type.IType import IType
from src.item.helditem.IHeldItem import IHeldItem
from src.pokemon.status.IStatus import IStatus

from src.pokemon.stats.Stats import Stats

from src.Const import RELATION, GROUP

from src.Formula import expFormula, gainFormula, criticalFormula, hpFormula

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
                 attacks: list[IAttack],
                 stats: Stats = None,
                 isWild: bool = True,
                 heldItem: IHeldItem = None,
                 ):
        self.name = name
        self.specie = specie
        self.stats = stats if stats is not None else Stats(level)
        self.hpMax = hpFormula(self.stats.getBaseStats().get_hp(), self.stats.getEVStats().getHp(), self.stats.getIVStats().getHp(), level)
        self.hp = self.hpMax
        self.level = level
        self.exp = exp
        self.expGroup = expGroup
        self.expYielded = expYielded
        self.types = types
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
        
        attack.execute() # Remove 1 PP
        
        power = attack.getPower()
        a = self.stats.getAttack(attack.getCategory())
        d = target.stats.getDefense(attack.getCategory())
        stab = 1.5 if attack.getType() in self.types else 1
        critical_hit = criticalFormula(attack.getStage(), self.heldItem, self.status)
        type_multipliers = []

        for target_type in target.types:
            
            relation = attack.getType().getRelation(target_type)
            
            if relation == RELATION.STRONG:
                type_multipliers.append(2)
            elif relation == RELATION.WEAK:
                type_multipliers.append(0.5)
            elif relation == RELATION.IMMUNE:
                type_multipliers.append(0)
            else:
                type_multipliers.append(1)
        
        efficacityMessage = ""
        
        if 0 in type_multipliers:
            efficacityMessage = f"But it doesn't affect {target.getName()}"
        elif 2 in type_multipliers and 0.5 in type_multipliers:
            efficacityMessage = ""
        elif 2 in type_multipliers:
            efficacityMessage = "It's super effective !"
        elif 0.5 in type_multipliers:
            efficacityMessage = "It's not very effective..."

        
        type1, type2 = type_multipliers[:2] + [1] * (2 - len(type_multipliers))

        random = (randint(85, 100)/100)
        
        damage = int(((((2*self.level/5)+2)*power*(a/d)/50)+2)*stab*type1*type2*random)
        
        damage = damage * 2 if critical_hit else damage
        
        target.addHp(-damage)
        
        print(f'{self.getName()} used {attack.getName()}')
        
        if critical_hit:
            print("Critical hit !")
            
        print(efficacityMessage)
            
        if damage > 0:
            print(f'{target.getName()} took {damage} damage\n')
        
        if not target.isAlive():
            expYielded = gainFormula(target.wild, target.getExpYielded(), target.getLevel())
            oldLevel = self.addExp(expYielded)
            print(f'{target.getName()} fainted\n{self.getName()} gained {expYielded} exp.\n')
            if self.level > oldLevel:
                print(f'{self.getName()} grew to level {self.level} !\n')