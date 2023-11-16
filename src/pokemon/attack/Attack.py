from src.pokemon.attack.IAttack import IAttack
from src.pokemon.attack.CCategory import CCategory
from src.pokemon.type.IType import IType
from src.pokemon.type.concretetype.NormalType import NormalType

class Attack(IAttack):
    def __init__(self) -> None:
        super().__init__()
        self.name:str = ""
        self.power:int = 0
        self.type:IType = NormalType()
        self.category:CCategory = CCategory.NONE
        self.precision:int = 0
        self.pp:int = 0
        self.max_pp:int = 0
        self.stage:int = 0
        
    # Getters
        
    def getName(self) -> str:return self.name
    def getPower(self) -> int:return self.power
    def getCategory(self) -> CCategory:return self.category
    def getType(self) -> IType:return self.type
    def getStage(self) -> int:return self.stage
    def getAccuracy(self) -> int:return self.precision
        
    def execute(self) -> None:
        '''Execute the attack'''
        self.pp -= 1