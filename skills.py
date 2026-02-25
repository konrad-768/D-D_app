from enum import Enum, auto 

class Stat(Enum):
    STR = "Strength"
    DEX = "Dexterity"
    CON = "Constitution"
    INT = "Intelligence"
    WIS = "Wisdom"
    CHA = "Charisma"

class Skill(Enum):
    # Навык = (Отображаемое имя, Родная характеристика)
    # Strength (STR) Сила
    ATHLETICS = ("Athletics", Stat.STR) # Атлетика

    # Dexterity (DEX) Ловкость
    ACROBATICS = ("Acrobatics", Stat.DEX) # Акробатика
    SLEIGHT_OF_HAND = ("Sleight of Hand", Stat.DEX) # Ловкость рук
    STEALTH = ("Stealth", Stat.DEX) # Скрытность

    # Intelligence (INT)
    ARCANA = ("Arcana", Stat.INT) # Магия
    HISTORY = ("History", Stat.INT) # История
    INVESTIGATION = ("Investigation", Stat.INT) # Расследование
    NATURE = ("Nature", Stat.INT) # Природа
    RELIGION = ("Religion", Stat.INT) # Религия

    # Wisdom (WIS) Мудрость
    ANIMAL_HANDLING = ("Animal Handling", Stat.WIS) # Уход за животными
    INSIGHT = ("Insight", Stat.WIS) # Проницательность
    MEDICINE = ("Medicine", Stat.WIS) # Медицина
    PERCEPTION = ("Perception", Stat.WIS) # Восприятие
    SURVIVAL = ("Survival", Stat.WIS) # Выживание

    # Charisma (CHA) Харизма
    INTIMIDATION = ("Intimidation", Stat.CHA) # Запугивание
    PERFORMANCE = ("Performance", Stat.CHA) # Выступление
    PERSUASION = ("Persuasion", Stat.CHA) # Убеждение
    DECEPTION = ("Deception", Stat.CHA) # Обман

    def __init__(self, label, parent_stat):
        self.label = label
        self.parent_stat = parent_stat