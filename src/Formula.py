from math import floor
from src.Const import GROUP
from src.item.helditem.HeldItem import HeldItem
from src.pokemon.status.Status import Status
from random import randint

def expFormula(expGroup: GROUP, level: int, exp: int) -> (int, int):
    '''Calculate the level and the remaining exp of a pokemon after gaining exp
    
    args:
        expGroup (GROUP): The group of the pokemon
        level (int): The level of the pokemon
        exp (int): The exp gained
        
    returns:
        (int, int): The level and the remaining exp of the pokemon'''
        
    expThresholds = {
        'Eratic': [
            (50, lambda lvl: lvl ** 3 * (100 - lvl) // 50),
            (68, lambda lvl: lvl ** 3 * (150 - lvl) // 100),
            (98, lambda lvl: lvl ** 3 * (1911 - 10 * lvl) // 500),
            (100, lambda lvl: lvl ** 3 * (160 - lvl) // 100)
        ],
        'Fast': [
            (100, lambda lvl: (lvl ** 3 * 4) // 5)
        ],
        'Medium Fast': [
            (100, lambda lvl: lvl ** 3)
        ],
        'Medium Slow': [
            (100, lambda lvl: (6/5) * lvl ** 3 - 15 * lvl ** 2 + 100 * lvl - 140)
        ],
        'Slow': [
            (100, lambda lvl: (5/4) * lvl ** 3)
        ],
        'Fluctuating': [
            (15, lambda lvl: lvl ** 3 * ((lvl + 1) // 3 + 24) // 50),
            (36, lambda lvl: lvl ** 3 * (lvl + 14) // 50),
            (100, lambda lvl: lvl ** 3 * ((lvl // 2) + 32) // 50)
        ]
    }
    
    expNeeded = next(threshold[1](level) for threshold in expThresholds[expGroup] if level < threshold[0])
    
    while exp >= expNeeded:
        if level == 100:
            exp = expNeeded
            return level, int(exp)
        level += 1
        exp -= expNeeded
        expNeeded = next(threshold[1](level) for threshold in expThresholds[expGroup] if level < threshold[0])
    
    return level, int(exp)

def gainFormula(isWild: bool, expYielded: int, level: int) -> int:
    '''Calculate the exp gained by a pokemon after defeating another pokemon
    
    args:
        isWild (bool): True if the defeated pokemon is wild, False otherwise
        expYielded (int): The exp yielded by the defeated pokemon
        level (int): The level of the pokemon
        
    returns:
        int: The exp gained by the pokemon'''
        
    multiplier = 1 if isWild else 1.5
    return floor(expYielded * level / 7 * multiplier)

def criticalFormula(attackStage: int, heldItem: HeldItem, status_list: list[Status]) -> bool:
    '''Calculate if the attack is critical or not
    
    args:
        attackStage (int): The stage of the attack
        heldItem (HeldItem): The held item of the pokemon
        status_list (list[Status]): The status list of the pokemon
        
    returns:
        bool: True if the attack is critical, False otherwise'''
        
    itemsOne = ['Scope Lens', 'Razor Claw']
    statusTwo = ['Focus Energy', 'Dire Hit']

    if heldItem is not None and heldItem.getName() in itemsOne:
        attackStage += 1
    for status in status_list:
        if status.getName() in statusTwo:
            attackStage += 2

    chance = max(16 // (2 * attackStage), 2) if attackStage > 0 else 16
    return randint(1, chance) == 1

def hpFormula(base: int, ev: int, iv: int, level: int) -> int:
    '''Calculate the max hp of a pokemon
    
    args:
        base (int): The base hp of the pokemon
        ev (int): The ev of the pokemon
        iv (int): The iv of the pokemon
        level (int): The level of the pokemon
        
    returns:
        int: The max hp of the pokemon'''
        
    return floor(0.01 * (2 * base + iv + floor(0.25 * ev)) * level + level + 10)