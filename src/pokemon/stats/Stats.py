from __future__ import annotations
from math import floor

from src.Const import CATEGORY
from src.pokemon.stats.BaseStats import BaseStats
from src.pokemon.stats.IVStats import IVStats
from src.pokemon.stats.EVStats import EVStats
from src.Formula import statFormula

class Stats():
    
    def __init__(self: Stats,
                 level: int,
                 base_stats: BaseStats,
                 iv_stats: IVStats = IVStats(),
                 ev_stats: EVStats = EVStats()
                 ) -> None:
        self.level = level
        self.base_stats = base_stats
        self.iv_stats = iv_stats
        self.ev_stats = ev_stats
        self.stats = statFormula(self.base_stats.getStats(), self.ev_stats.getStats(), self.iv_stats.getStats(), self.level)
        
    def getLevel(self: Stats) -> int:return self.level
    def getBaseStats(self: Stats) -> BaseStats:return self.base_stats
    def getIVStats(self: Stats) -> IVStats:return self.iv_stats
    def getEVStats(self: Stats) -> EVStats:return self.ev_stats
    def getStats(self: Stats) -> dict[str,int]:return self.stats
    
    def getDefense(self, category: CATEGORY) -> int:
        """
        Returns the defense value based on the given category.

        Args:
            category: The category of defense. Possible values are PHYSICAL or SPECIAL.

        Returns:
            int: The defense value corresponding to the category. Returns 0 if the category is not recognized.
        """
        if category == CATEGORY.PHYSICAL:
            return self.getDefensePhysical()
        elif category == CATEGORY.SPECIAL:
            return self.getDefenseSpecial()
        else:
            return 0
        
    def getDefensePhysical(self: Stats) -> int:
        """
        Returns the physical defense value of the Stats object.

        Returns:
            int: The calculated physical defense value based on the Stats object's attributes.
        """
        return floor((2 * self.base_stats.defense + self.iv_stats.defense + self.ev_stats.defense / 4) * self.level / 100 + 5)
    
    def getDefenseSpecial(self: Stats) -> int:
        """
        Returns the special defense value of the Stats object.

        Returns:
            int: The calculated special defense value based on the Stats object's attributes.
        """
        return floor((2 * self.base_stats.special_defense + self.iv_stats.special_defense + self.ev_stats.special_defense / 4) * self.level / 100 + 5)
        
    def getAttack(self, category: CATEGORY) -> int:
        """
        Returns the attack value based on the given category.

        Args:
            category: The category of attack. Possible values are PHYSICAL or SPECIAL.

        Returns:
            int: The attack value corresponding to the category. Returns 0 if the category is not recognized.
        """
        if category == CATEGORY.PHYSICAL:
            return self.getAttackPhysical()
        elif category == CATEGORY.SPECIAL:
            return self.getAttackSpecial()
        else:
            return 0
        
    def getAttackPhysical(self: Stats) -> int:
        """
        Returns the physical attack value of the Stats object.

        Returns:
            int: The calculated physical attack value based on the Stats object's attributes.
        """
        return floor((2 * self.base_stats.attack + self.iv_stats.attack + self.ev_stats.attack / 4) * self.level / 100 + 5)
    
    def getAttackSpecial(self: Stats) -> int:
        """
        Returns the special attack value of the Stats object.

        Returns:
            int: The calculated special attack value based on the Stats object's attributes.
        """
        return floor((2 * self.base_stats.special_attack + self.iv_stats.special_attack + self.ev_stats.special_attack / 4) * self.level / 100 + 5)
    
    def setStats (self,stats : dict[str,int]) -> None:
        self.stats = stats