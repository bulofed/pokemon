# Relation

RELATION = type("RELATION", (), {})

RELATION.WEAK:str = "weak"
RELATION.NEUTRAL:str = "neutral"
RELATION.STRONG:str = "strong"
RELATION.IMMUNE:str = "immune"

# Type

TYPE = type("TYPE", (), {})

TYPE.NORMAL:str = "Normal"
TYPE.GRASS:str = "Grass"
TYPE.FIRE:str = "Fire"
TYPE.WATER:str = "Water"

# Category

CATEGORY = type("CATEGORY", (), {})

CATEGORY.NONE:str = ""
CATEGORY.PHYSICAL:str = "Physical"
CATEGORY.SPECIAL:str = "Special"
CATEGORY.STATUS:str = "Status"

# Experience Groups

GROUP = type("GROUP", (), {})

GROUP.MEDIUM_FAST = "Medium Fast"
GROUP.ERATIC = "Eratic"
GROUP.FLUCTUATING = "Fluctuating"
GROUP.MEDIUM_SLOW = "Medium Slow"
GROUP.FAST = "Fast"
GROUP.SLOW = "Slow"

# Stats

STATS = type("STATS", (), {})
STATS.HP = "HP"
STATS.ATTACK = "ATK"
STATS.DEFENSE = "DEF"
STATS.SPECIAL_ATTACK = "SP.ATK"
STATS.SPECIAL_DEFENSE = "SP.DEF"
STATS.SPEED = "SPD"