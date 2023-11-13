from src.pokemon.attack.IAttack import IAttack
from src.Const import TYPE, CATEGORY

class Attack(IAttack):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = ""
        self.power:int = 0
        self.type:TYPE = TYPE.NONE
        self.category:CATEGORY = CATEGORY.NONE
        self.precision:int = 0
        self.pp:int = 0
        self.max_pp:int = 0
        
    # Getters
        
    def getName(self) -> str:return self.name
    def getPower(self) -> int:return self.power
    def getCategory(self) -> CATEGORY:return self.category
    def getType(self) -> TYPE:return self.type
        
    def execute(self) -> None:
        '''Execute the attack'''
        self.pp -= 1