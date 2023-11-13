from src.pokemon.attack.Attack import Attack
from src.Const import TYPE, CATEGORY

class EmberAttack(Attack):
    def __init__(self):
        super().__init__()
        self.name:str = "Ember"
        self.power:int = 40
        self.type:TYPE = TYPE.FIRE
        self.category:CATEGORY = CATEGORY.SPECIAL
        self.precision:int = 100
        self.pp:int = 25
        self.max_pp:int = 25
        
    def execute(self) -> None:
        super().execute()