# Relation

RELATION = type("RELATION", (), {})

RELATION.WEAK:str = "weak"
RELATION.NEUTRAL:str = "neutral"
RELATION.STRONG:str = "strong"

# Type

TYPE = type("TYPE", (), {})

TYPE.NONE:str = ""
TYPE.NORMAL:str = "Normal"
TYPE.FIRE:str = "Fire"
TYPE.WATER:str = "Water"
TYPE.GRASS:str = "Grass"

# Category

CATEGORY = type("CATEGORY", (), {})

CATEGORY.NONE:str = ""
CATEGORY.PHYSICAL:str = "Physical"
CATEGORY.SPECIAL:str = "Special"
CATEGORY.STATUS:str = "Status"