from src.pokemon.attack.Attack import Attack
from src.Const import CATEGORY
from src.pokemon.type.IType import IType
from src.pokemon.type.concretetype.FireType import FireType

class EmberAttack(Attack):
    def __init__(self):
        super().__init__()
        self.name:str = "Ember"
        self.power:int = 40
        self.type:IType = FireType()
        self.category:CATEGORY = CATEGORY.SPECIAL
        self.precision:int = 100
        self.pp:int = 25
        self.max_pp:int = 25