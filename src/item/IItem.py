from __future__ import annotations
from abc import ABC, abstractmethod

class IItem(ABC):
    @abstractmethod
    def getName(self:IItem) -> str:pass