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
        
    def execute(self) -> None:
        self.pp -= 1
        
    def getPower(self: IAttack) -> int:
        return self.power
    
    def getCategory(self: IAttack) -> CATEGORY:
        return self.category
    
    def getType(self: IAttack) -> TYPE:
        return self.type