from __future__ import annotations
from abc import ABC, abstractmethod

class IStatus(ABC):
    @abstractmethod
    def getName(self: IStatus) -> str: pass
    @abstractmethod
    def getEffect(self: IStatus) -> dict: pass
    @abstractmethod
    def getDuration(self: IStatus) -> int: pass