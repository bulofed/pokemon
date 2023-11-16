from src.pokemon.elements.attack.Attack import Attack
from src.pokemon.elements.attack.CCategory import CCategory
from src.pokemon.elements.type.IType import IType
from src.pokemon.elements.type.concretetype.NormalType import NormalType


class TackleAttack(Attack):
    def __init__(self):
        super().__init__()
        self.name: str = "Tackle"
        self.power: int = 40
        self.type: IType = NormalType()
        self.category: CCategory = CCategory.PHYSICAL
        self.precision: int = 100
        self.pp: int = 35
        self.max_pp: int = 35
