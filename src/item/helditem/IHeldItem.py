from abc import ABC, abstractmethod
from src.item.Item import Item
from src.item.CItemType import CItemType

class IHeldItem(Item, ABC):
    @abstractmethod
    def getItemType(self) -> CItemType:pass
    @abstractmethod
    def getEffect(self) -> dict:pass
    @abstractmethod
    def use(self) -> None:pass