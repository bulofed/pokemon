from src.pokemon.stats.CStats import CStats
from src.pokemon.nature.CNature import CNature

NATURE_LIST = [getattr(CNature, attr) for attr in dir(CNature) if not callable(
    getattr(CNature, attr)) and not attr.startswith("__")]

NATURE_TABLE = {
    CNature.HARDY: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.LONELY: {CStats.ATTACK: 1.1, CStats.DEFENSE: 0.9, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.BRAVE: {CStats.ATTACK: 1.1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 0.9},

    CNature.ADAMANT: {CStats.ATTACK: 1.1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 0.9, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.NAUGHTY: {CStats.ATTACK: 1.1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 0.9, CStats.SPEED: 1},

    CNature.BOLD: {CStats.ATTACK: 0.9, CStats.DEFENSE: 1.1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.DOCILE: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.RELAXED: {CStats.ATTACK: 1, CStats.DEFENSE: 1.1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 0.9},

    CNature.IMPISH: {CStats.ATTACK: 1, CStats.DEFENSE: 1.1, CStats.SPECIAL_ATTACK: 0.9, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.LAX: {CStats.ATTACK: 1, CStats.DEFENSE: 1.1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 0.9, CStats.SPEED: 1},

    CNature.TIMID: {CStats.ATTACK: 0.9, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1.1},

    CNature.HASTY: {CStats.ATTACK: 1, CStats.DEFENSE: 0.9, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1.1},

    CNature.SERIOUS: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.JOLLY: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 0.9, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1.1},

    CNature.NAIVE: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 0.9, CStats.SPEED: 1.1},

    CNature.MODEST: {CStats.ATTACK: 0.9, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1.1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.MILD: {CStats.ATTACK: 1, CStats.DEFENSE: 0.9, CStats.SPECIAL_ATTACK: 1.1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.QUIET: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1.1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 0.9},

    CNature.BASHFUL: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},

    CNature.RASH: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1.1, CStats.SPECIAL_DEFENSE: 0.9, CStats.SPEED: 1},

    CNature.CALM: {CStats.ATTACK: 0.9, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1.1, CStats.SPEED: 1},

    CNature.GENTLE: {CStats.ATTACK: 1, CStats.DEFENSE: 0.9, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1.1, CStats.SPEED: 1},

    CNature.SASSY: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1.1, CStats.SPEED: 0.9},

    CNature.CAREFUL: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 0.9, CStats.SPECIAL_DEFENSE: 1.1, CStats.SPEED: 1},

    CNature.QUIRKY: {CStats.ATTACK: 1, CStats.DEFENSE: 1, CStats.SPECIAL_ATTACK: 1, CStats.SPECIAL_DEFENSE: 1, CStats.SPEED: 1},
}