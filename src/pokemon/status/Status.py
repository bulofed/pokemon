from src.pokemon.status.IStatus import IStatus
from src.pokemon.status.StatusType import StatusType

class Status(IStatus):
    def __init__(self, name: str, effect: dict, duration: int) -> None:
        self.name = name
        self.effect = effect
        self.duration = duration
        
    # Getters
        
    def getName(self) -> str:return self.name
    def getEffect(self) -> dict:return self.effect
    def getDuration(self) -> int:return self.duration