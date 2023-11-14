from abc import ABC, abstractmethod
from src.item.Item import Item
from src.item.ItemType import ItemType

class IHeldItem(Item, ABC):
    @abstractmethod
    def getItemType(self) -> ItemType:pass
    @abstractmethod
    def getEffect(self) -> dict:pass