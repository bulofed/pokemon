from __future__ import annotations

from src.pokemon.elements.stats.CStats import CStats
from src.pokemon.elements.nature.CNature import CNature
from src.pokemon.elements.attack.CCategory import CCategory
from src.pokemon.elements.stats.BaseStats import BaseStats
from src.pokemon.elements.stats.IVStats import IVStats
from src.pokemon.elements.stats.EVStats import EVStats
from src.Formula import statFormula


class Stats():

    def __init__(self: Stats,
                 level: int,
                 nature: CNature,
                 base_stats: BaseStats,
                 iv_stats: IVStats = IVStats(),
                 ev_stats: EVStats = EVStats()
                 ) -> None:
        self.level = level
        self.nature = nature
        self.base_stats = base_stats
        self.iv_stats = iv_stats
        self.ev_stats = ev_stats
        self.stats = statFormula(self.base_stats.getStats(), self.ev_stats.getStats(
        ), self.iv_stats.getStats(), self.level, self.nature)

    def getLevel(self: Stats) -> int: return self.level
    def getBaseStats(self: Stats) -> BaseStats: return self.base_stats
    def getIVStats(self: Stats) -> IVStats: return self.iv_stats
    def getEVStats(self: Stats) -> EVStats: return self.ev_stats
    def getStats(self: Stats) -> dict[str, int]: return self.stats

    def getDefense(self, category: CCategory) -> int:
        """
        Returns the defense value based on the given category.

        Args:
            category: The category of defense. Possible values are PHYSICAL or SPECIAL.

        Returns:
            int: The defense value corresponding to the category. Returns 0 if the category is not recognized.
        """
        if category == CCategory.PHYSICAL:
            return self.stats[CStats.DEFENSE]
        elif category == CCategory.SPECIAL:
            return self.stats[CStats.SPECIAL_DEFENSE]
        else:
            return 0

    def getAttack(self, category: CCategory) -> int:
        """
        Returns the attack value based on the given category.

        Args:
            category: The category of attack. Possible values are PHYSICAL or SPECIAL.

        Returns:
            int: The attack value corresponding to the category. Returns 0 if the category is not recognized.
        """
        if category == CCategory.PHYSICAL:
            return self.stats[CStats.ATTACK]
        elif category == CCategory.SPECIAL:
            return self.stats[CStats.SPECIAL_ATTACK]
        else:
            return 0

    def setStats(self, stats: dict[str, int]) -> None:
        self.stats = stats
