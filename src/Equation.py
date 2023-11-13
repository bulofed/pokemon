from src.Const import GROUP

def expEquation(expGroup: GROUP, level: int, exp: int) -> (int, int):
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

def gainEquation(isWild: bool, expYielded: int, level: int) -> int:
    '''Calculate the exp gained by a pokemon after defeating another pokemon
    
    args:
        isWild (bool): True if the defeated pokemon is wild, False otherwise
        expYielded (int): The exp yielded by the defeated pokemon
        level (int): The level of the pokemon
        
    returns:
        int: The exp gained by the pokemon'''
    multiplier = 1.5 if not isWild else 1
    return int(expYielded * level / 7 * multiplier)