from src.pokemon.elements.status.IStatus import IStatus


class Status(IStatus):
    def __init__(self, name: str, effect: dict, duration: int) -> None:
        self.name = name
        self.effect = effect
        self.duration = duration

    # Getters

    def getName(self) -> str: return self.name
    def getEffect(self) -> dict: return self.effect
    def getDuration(self) -> int: return self.duration
