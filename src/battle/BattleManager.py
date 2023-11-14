from typing import List
from random import randint
from src.Const import RELATION
from src.Formula import gainFormula, criticalFormula
from src.pokemon.IPokemon import IPokemon
from src.pokemon.attack.IAttack import IAttack
from src.pokemon.PokemonObserver import PokemonObserver

class BattleManager:
    def __init__(self) -> None:
        self.observers = []
        
    def addObserver(self, observer: PokemonObserver) -> None:
        self.observers.append(observer)
        
    def notifyObservers(self, pokemon: IPokemon, attack: IAttack) -> None:
        for observer in self.observers:
            observer.update(pokemon, attack)
            
    def calculateDamage(self, attacker: IPokemon, target: IPokemon, attack: IAttack) -> int:
        power = attack.getPower()
        a = attacker.getStats().getAttack(attack.getCategory())
        d = target.getStats().getDefense(attack.getCategory())
        stab = 1.5 if attack.getType() in attacker.getTypes() else 1
        critical_hit = criticalFormula(attack.getStage(), attacker.getHeldItem(), attacker.getStatus())
        type_multipliers = []
        
        for target_type in target.getTypes():
                
                relation = attack.getType().getRelation(target_type)
                
                if relation == RELATION.STRONG:
                    type_multipliers.append(2)
                elif relation == RELATION.WEAK:
                    type_multipliers.append(0.5)
                elif relation == RELATION.IMMUNE:
                    type_multipliers.append(0)
                else:
                    type_multipliers.append(1)
                    
        type1, type2 = type_multipliers[:2] + [1] * (2 - len(type_multipliers))
        