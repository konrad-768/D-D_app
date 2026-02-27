from dataclasses import dataclass

from skills import Stat, Skill
from skills import Stat, Skill
from enum import Enum, auto

class CharacterClass(Enum):
    BARBARIAN = "Barbarian"
    FIGHTER = "Fighter"
    PALADIN = "Paladin"
    MONK = "Monk"
    ROGUE = "Rogue"
    RANGER = "Ranger"
    CLERIC = "Cleric"
    DRUID = "Druid"
    WIZARD = "Wizard"
    ARTIFICER = "Artificer"
    SORCERER = "Sorcerer"
    WITCH = "Witch"






CLASS_TEMPLATES = {
    "Barbarian": {
        "hit_die": 12,                                 # Самый большой запас здоровья в игре
        "saving_throws": [Stat.STR, Stat.CON],         # Спас броски через силу и телосложение
        "primary_stat": Stat.STR,                      # Основная характеристика для Вравара — Сила
        "recommended_stats": {                         # Наиболее важные характеристики для класса
            Stat.STR: 15, Stat.DEX: 13, Stat.CON: 14, 
            Stat.INT: 8, Stat.WIS: 12, Stat.CHA: 10
        },
        "skills_count": 2,
        "available_skills": [
            Skill.ANIMAL_HANDLING, 
            Skill.ATHLETICS, 
            Skill.INTIMIDATION, 
            Skill.NATURE, 
            Skill.PERCEPTION, 
            Skill.SURVIVAL
        ]
    },
    "Fighter": {                                       # Воин — класс, который специализируется на боевых навыках и может использовать широкий спектр оружия и брони
        "hit_die": 10,                                 # d10 — золотой стандарт бойца
        "saving_throws": [Stat.STR, Stat.CON],         # Спасброски: Сила и Телосложение — классические для воинов
        "primary_stat": Stat.STR,                      # Основная характеристика для Вравара — Сила
        "recommended_stats": {                         # Наиболее важные характеристики для класса
            Stat.STR: 15, Stat.DEX: 13, Stat.CON: 14, 
            Stat.INT: 8, Stat.WIS: 12, Stat.CHA: 10
        },
        "skills_count": 2,                             # Сколько навыков игрок может выбрать из списка ниже
        "available_skills": [
            Skill.ATHLETICS, 
            Skill.ACROBATICS, 
            Skill.HISTORY, 
            Skill.INSIGHT, 
            Skill.INTIMIDATION, 
            Skill.PERCEPTION, 
            Skill.SURVIVAL
        ]
    },
    "Paladin": {
        "hit_die": 10,
        "saving_throws": [Stat.WIS, Stat.CHA],         # Спасброски: Мудрость и Харизма
        "primary_stat": Stat.STR,                      # Основная характеристика для бойца — Сила
        "recommended_stats": {                         # Наиболее важные характеристики для класса
            Stat.STR: 15, Stat.DEX: 10, Stat.CON: 13, 
            Stat.INT:8, Stat.WIS: 12, Stat.CHA: 14
        },
        "skills_count": 2,
        "available_skills": [
            Skill.ATHLETICS, 
            Skill.INSIGHT, 
            Skill.INTIMIDATION, 
            Skill.MEDICINE, 
            Skill.PERCEPTION, 
            Skill.RELIGION
        ]
    },
    "Monk": {                                        # Монах — класс, который специализируется на боевых искусствах и духовной дисциплине, используя свою внутреннюю энергию (ки) для усиления своих атак и защиты
        "hit_die": 8,                                   
        "saving_throws": [Stat.WIS, Stat.DEX],       # Спасброски: Мудрость и Ловкость — классические для монахов
        "primary_stat": Stat.DEX,                    # Основная характеристика для Монаха — Ловкость, так как она влияет на атаки и навыки       
        "recommended_stats": {
            Stat.STR: 12, Stat.DEX: 15, Stat.CON: 13, 
            Stat.INT: 8, Stat.WIS: 14, Stat.CHA: 10
        },
        "skills_count": 2,
        "available_skills": [
            Skill.ANIMAL_HANDLING, 
            Skill.MEDICINE, 
            Skill.PERCEPTION, 
            Skill.RELIGION
        ]
    },
    "Rogue": {
        "hit_die": 8,                               # d8 — чуть меньше здоровья, чем у воина
        "saving_throws": [Stat.DEX, Stat.INT],      # Спасброски: Ловкость и Интеллект — идеально для ловкачей и хитрецов
        "primary_stat": Stat.DEX,                   # Основная характеристика для Рога — Ловкость, так как она влияет на атаки и навыки
        "recommended_stats": {
            Stat.STR: 13, Stat.DEX: 15, Stat.CON: 14, 
            Stat.INT: 12, Stat.WIS: 8, Stat.CHA: 10
        },
        "skills_count": 4,                          # Плут — мастер навыков, выбирает 4
        "available_skills": [
            Skill.ACROBATICS, 
            Skill.STEALTH, 
            Skill.SLEIGHT_OF_HAND, 
            Skill.INSIGHT, 
            Skill.INVESTIGATION, 
            Skill.DECEPTION, 
            Skill.PERSUASION
        ]
    },
    "Ranger": {                                     # Рейнджер — класс, который специализируется на выживании в дикой природе и охоте на монстров
        "hit_die": 10,
        "saving_throws": [Stat.STR, Stat.DEX],      # Спасброски: Сила и Ловкость — классические для рейнджеров
        "primary_stat": Stat.DEX,                   # Основная характеристика для Рейнджера — Ловкость, так как она влияет на атаки и навыки
        "recommended_stats": {
            Stat.STR: 12, Stat.DEX: 15, Stat.CON: 13, 
            Stat.INT: 8, Stat.WIS: 14, Stat.CHA: 10
        },
        "skills_count": 3,
        "available_skills": [
            Skill.ANIMAL_HANDLING, 
            Skill.ATHLETICS, 
            Skill.INSIGHT, 
            Skill.INVESTIGATION, 
            Skill.NATURE, 
            Skill.PERCEPTION, 
            Skill.SURVIVAL
        ]
    },
        "Cleric": {                                 # Клирик — класс, который черпает силу из божественной веры и может лечить и наносить урон божественной магией
        "hit_die": 8,
        "saving_throws": [Stat.WIS, Stat.CHA],      # Спасброски: Мудрость и Харизма — классические для клириков     
        "primary_stat": Stat.WIS,                   # Основная характеристика для Клирика — Мудрость, так как она влияет на заклинания и навыки
        "recommended_stats": {
            Stat.STR: 13, Stat.DEX: 10, Stat.CON: 14, 
            Stat.INT: 8, Stat.WIS: 15, Stat.CHA: 12
        },
        "skills_count": 2,
        "available_skills": [
            Skill.HISTORY, 
            Skill.INSIGHT, 
            Skill.MEDICINE, 
            Skill.PERCEPTION, 
            Skill.RELIGION, 
            Skill.SURVIVAL
        ]
    },
        "Druid": {                                  # Друид — класс, который черпает силу из природы и может превращаться в животных
        "hit_die": 8,
        "saving_throws": [Stat.WIS, Stat.INT],      # Спасброски: Мудрость и Интеллект — классические для друидов
        "primary_stat": Stat.WIS,                   # Основная характеристика для Друида — Мудрость, так как она влияет на заклинания и навыки
        "recommended_stats": {
            Stat.STR: 8, Stat.DEX: 13, Stat.CON: 14, 
            Stat.INT: 12, Stat.WIS: 15, Stat.CHA: 10
        },
        "skills_count": 2,
        "available_skills": [
            Skill.ARCANA, 
            Skill.ANIMAL_HANDLING, 
            Skill.INSIGHT, 
            Skill.MEDICINE, 
            Skill.NATURE, 
            Skill.PERCEPTION, 
            Skill.SURVIVAL
        ]
    },
    "Wizard": {                                     # Волшебник — класс, который специализируется на изучении и использовании магии, черпая силу из книг и знаний
        "hit_die": 6,                               # Мало здоровья, но много магии
        "saving_throws": [Stat.INT, Stat.WIS],      # Спасброски: Интеллект и Мудрость — классические для волшебников, так как они влияют на заклинания и знания
        "primary_stat": Stat.INT,                   # Основная характеристика для Волшебника — Интеллект, так как он влияет на заклинания и навыки
        "recommended_stats": {
            Stat.STR: 8, Stat.DEX: 13, Stat.CON: 14, 
            Stat.INT: 15, Stat.WIS: 12, Stat.CHA: 10
        },
        "skills_count": 2,
        "available_skills": [
            Skill.ARCANA, 
            Skill.HISTORY, 
            Skill.INSIGHT, 
            Skill.INVESTIGATION, 
            Skill.MEDICINE, 
            Skill.RELIGION
        ]
    },
    "Artificer": {                                  # Артифактор — класс, который сочетает магию и технологии, создавая уникальные предметы и устройства
        "hit_die": 8,
        "saving_throws": [Stat.INT, Stat.CON],      # Спасброски: Интеллект и Телосложение — классические для изобретателей, так как они влияют на заклинания и выносливость
        "primary_stat": Stat.INT,                   # Основная характеристика для Артифактора — Интеллект, так как он влияет на заклинания и навыки
        "recommended_stats": {
            Stat.STR: 8, Stat.DEX: 13, Stat.CON: 14, 
            Stat.INT: 15, Stat.WIS: 12, Stat.CHA: 10
        },
        "skills_count": 2,
        "available_skills": [
            Skill.ARCANA, 
            Skill.HISTORY, 
            Skill.INSIGHT, 
            Skill.INVESTIGATION, 
            Skill.MEDICINE, 
            Skill.RELIGION
        ]
    },
    "Sorcerer": {                                   # Чародей — класс, который черпает магию из внутреннего источника, а не из изучения книг
        "hit_die": 6,
        "saving_throws": [Stat.INT, Stat.CHA],      # Спасброски: Интеллект и Харизма — классические для Сорцерера, так как они влияют на заклинания и личное обаяние
        "primary_stat": Stat.CHA,                   # Основная характеристика для Сорцерера — Харизма, так как она влияет на заклинания и навыки
        "recommended_stats": {
            Stat.STR: 8, Stat.DEX: 13, Stat.CON: 14, 
            Stat.INT: 12, Stat.WIS: 15, Stat.CHA: 15
        },  
        "skills_count": 2,
        "available_skills": [
            Skill.ARCANA, 
            Skill.DECEPTION, 
            Skill.INSIGHT, 
            Skill.INTIMIDATION, 
            Skill.PERSUASION, 
            Skill.RELIGION
        ]
    },
    "Witch": {                                      # Колдун — класс, который черпает магию из темных источников и может использовать проклятия и заклинания контроля
        "hit_die": 8,
        "saving_throws": [Stat.INT, Stat.CHA],      # Спасброски: Интеллект и Харизма — классические для Ведьмы, так как они влияют на заклинания и личное обаяние
        "primary_stat": Stat.CHA,                   # Основная характеристика для Ведьмы — Харизма, так как она влияет на заклинания и навыки
        "recommended_stats": {
            Stat.STR: 8, Stat.DEX: 13, Stat.CON: 14, 
            Stat.INT: 10, Stat.WIS: 12, Stat.CHA: 15
        },  
        "skills_count": 2,
        "available_skills": [
            Skill.ARCANA, 
            Skill.DECEPTION, 
            Skill.INSIGHT, 
            Skill.INTIMIDATION,
            Skill.PERSUASION, 
            Skill.RELIGION, 
        ]
    },
}