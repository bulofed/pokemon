from src.pokemon.elements.type.Type import Type
from src.pokemon.elements.type.CType import CType

class PsychicType(Type):
    def __init__(self) -> None:
        super().__init__()
        self.name = CType.PSYCHIC
        self.weakness = [CType.PSYCHIC,CType.STEEL,CType.DIVINE]
        self.strength = [CType.FIGHTING,CType.POISON]
        self.immune = [CType.DARK]