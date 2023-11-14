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
            return level, int(exp)
        level += 1
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
        
    multiplier = 1.5 if not isWild else 1
    return int(expYielded * level / 7 * multiplier)

def criticalFormula(attackStage: int, heldItem: HeldItem, status_list: list[Status]) -> bool:
    '''Calculate if the attack is critical or not
    
    args:
        attackStage (int): The stage of the attack
        heldItem (HeldItem): The held item of the pokemon
        status_list (list[Status]): The status list of the pokemon
        
    returns:
        bool: True if the attack is critical, False otherwise'''
    
    if heldItem and (heldItem.getName() == 'Scope Lens' or heldItem.getName() == 'Razor Claw'):
        attackStage += 1
    if any(status.getName() == 'Focus Energy' for status in status_list):
        attackStage += 2
    if any(status.getName() == 'Dire Hit' for status in status_list):
        attackStage += 2
        
    if attackStage <= 0:
        chance = 16
    elif attackStage == 1:
        chance = 8
    elif attackStage == 2:
        chance = 4
    elif attackStage == 3:
        chance = 3
    else:
        chance = 2
    
    return randint(1, chance) == 1