from src.item.IItem import IItem

class Item(IItem):
    def __init__(self, name: str) -> None:
        self.name = name
        
    def getName(self) -> str:
        return self.name