from src.pokemon.attack.Attack import Attack
from src.Const import CATEGORY
from src.pokemon.type.IType import IType
from src.pokemon.type.concretetype.NormalType import NormalType

class TackleAttack(Attack):
    def __init__(self):
        super().__init__()
        self.name:str = "Tackle"
        self.power:int = 40
        self.type:IType = NormalType()
        self.category:CATEGORY = CATEGORY.PHYSICAL
        self.precision:int = 100
        self.pp:int = 35
        self.max_pp:int = 35