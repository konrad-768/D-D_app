from enum import Enum, auto 
from skills import Skill, Stat

class Size(Enum):
    TINY = "Tiny"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"

# Словарь с рассами в игре
RACE_TEMPLATES = {
    "Human": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": {Stat.STR: 1, Stat.DEX: 1, Stat.CON: 1, Stat.INT: 1, Stat.WIS: 1, Stat.CHA: 1}  # +1 Ко всем характеристикам
    },
    "Dragonborn": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": {Stat.STR: 2, Stat.CHA: 1}                                                      # +2 к силе и + 1 к харизме
    },
    "Aasimar": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": { Stat.DEX: 1, Stat.INT: 1, Stat.WIS: 1,}                                       # +1 к ловкости, интеллекту и мудрости 
    },
    "Elf": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": {Stat.DEX: 2}                                                                   # +2 к ловкости 
    },
#    "Dwarf": {
#        "size": Size.MEDIUM,
#        "speed": 25,
#        "bonuses": {Stat.CON: 2}                                                                   # +2 к конституции
#    },
#    "Gnome": {
#        "size": Size.SMALL,
#        "speed": 25,
#        "bonuses": {Stat.INT: 2}                                                                    # +2 к интеллекту
#    },
    "Goliath": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": {Stat.STR: 2, Stat.DEX: 1, Stat.CON: 1,}                                         # +2 к силе, +1 к ловкости и конституции
    },
    "Half-Elf": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": {Stat.DEX: 1, Stat.CHA: 2}                                                       # +1 к ловкости и +2 к харизме
    },
#    "Half-Orc": {
#        "size": Size.MEDIUM,
#        "speed": 30,
#        "bonuses": {Stat.STR: 2, Stat.CON: 1}                                                       # +2 к силе и +1 к конституции
#    },
 #   "Halfling": {
 #       "size": Size.SMALL,
 #       "speed": 25,
 #       "bonuses": {Stat.DEX: 2}                                                                    # +2 к ловкости
 #   },
    "Orc": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": {Stat.STR: 2, Stat.CON: 1}                                                       # +2 к силе и +1 к конституции
    },
    "Tiefling": {
        "size": Size.MEDIUM,
        "speed": 30,
        "bonuses": {Stat.INT: 1, Stat.CHA: 2}                                                       # +1 к интеллекту и +2 к харизме
    },
}