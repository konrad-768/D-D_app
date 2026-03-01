from dataclasses import dataclass
from typing import List, Dict
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


@dataclass
class ClassTemplate:
    name: CharacterClass
    hit_die: int
    saving_throws: List[Stat]
    primary_stat: Stat
    recommended_stats: Dict[Stat, int]
    skills_count: int
    available_skills: List[Skill]

    def is_skill_available(self, skill: Skill) -> bool:
        return skill in self.available_skills

    def validate_skill_selection(self, selected_skills: List[Skill]) -> bool:
        if len(selected_skills) != self.skills_count:
            return False
        return all(skill in self.available_skills for skill in selected_skills)


# --- ОПРЕДЕЛЕНИЕ КЛАССОВ ---

BARBARIAN = ClassTemplate(
    name=CharacterClass.BARBARIAN,
    hit_die=12,                                 # Самый большой запас здоровья в игре
    saving_throws=[Stat.STR, Stat.CON],         # Спасброски: Сила и Телосложение
    primary_stat=Stat.STR,                      # Основная характеристика: Сила
    recommended_stats={
        Stat.STR: 15,
        Stat.DEX: 13,
        Stat.CON: 14,
        Stat.INT: 8,
        Stat.WIS: 12,
        Stat.CHA: 10,
    },
    skills_count=2,
    available_skills=[
        Skill.ANIMAL_HANDLING,
        Skill.ATHLETICS,
        Skill.INTIMIDATION,
        Skill.NATURE,
        Skill.PERCEPTION,
        Skill.SURVIVAL,    
    ],
)

FIGHTER = ClassTemplate(
    name=CharacterClass.FIGHTER,
    hit_die=10,                                 # d10 — золотой стандарт бойца
    saving_throws=[Stat.STR, Stat.CON],
    primary_stat=Stat.STR,
    recommended_stats={
        Stat.STR: 15,
        Stat.DEX: 13,
        Stat.CON: 14,
        Stat.INT: 8,
        Stat.WIS: 12,
        Stat.CHA: 10,
    },
    skills_count=2,
    available_skills=[
        Skill.ATHLETICS,
        Skill.ACROBATICS,
        Skill.HISTORY,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.PERCEPTION,
        Skill.SURVIVAL,
    ],
)

PALADIN = ClassTemplate(
    name=CharacterClass.PALADIN,
    hit_die=10,
    saving_throws=[Stat.WIS, Stat.CHA],
    primary_stat=Stat.STR,                      # Основная характеристика: Сила (и Харизма)
    recommended_stats={
        Stat.STR: 15,
        Stat.DEX: 10,
        Stat.CON: 13,
        Stat.INT: 8,
        Stat.WIS: 12,
        Stat.CHA: 14,
    },
    skills_count=2,
    available_skills=[
        Skill.ATHLETICS,
        Skill.INSIGHT,
        Skill.INTIMIDATION,
        Skill.MEDICINE,
        Skill.PERCEPTION,
        Skill.RELIGION,
    ],
)

MONK = ClassTemplate(
    name=CharacterClass.MONK,
    hit_die=8,
    saving_throws=[Stat.WIS, Stat.DEX],
    primary_stat=Stat.DEX,
    recommended_stats={
        Stat.STR: 12,
        Stat.DEX: 15,
        Stat.CON: 13,
        Stat.INT: 8,
        Stat.WIS: 14,
        Stat.CHA: 10,
    },
    skills_count=2,
    available_skills=[
        Skill.ANIMAL_HANDLING,
        Skill.MEDICINE,
        Skill.PERCEPTION,
        Skill.RELIGION,
    ], 
)

ROGUE = ClassTemplate(
    name=CharacterClass.ROGUE,
    hit_die=8,
    saving_throws=[Stat.DEX, Stat.INT],
    primary_stat=Stat.DEX,
    recommended_stats={
        Stat.STR: 13,
        Stat.DEX: 15,
        Stat.CON: 14,
        Stat.INT: 12,
        Stat.WIS: 8,
        Stat.CHA: 10,
    },
    skills_count=4,                             # Плут — мастер навыков, выбирает 4
    available_skills=[
        Skill.ACROBATICS, 
        Skill.STEALTH, 
        Skill.SLEIGHT_OF_HAND, 
        Skill.INSIGHT, 
        Skill.INVESTIGATION, 
        Skill.DECEPTION, 
        Skill.PERSUASION
    ],
)

RANGER = ClassTemplate(
    name=CharacterClass.RANGER,
    hit_die=10,
    saving_throws=[Stat.STR, Stat.DEX],
    primary_stat=Stat.DEX,
    recommended_stats={
        Stat.STR: 12,
        Stat.DEX: 15,
        Stat.CON: 13,
        Stat.INT: 8,
        Stat.WIS: 14,
        Stat.CHA: 10,
    },
    skills_count=3,
    available_skills=[
        Skill.ANIMAL_HANDLING, 
        Skill.ATHLETICS, 
        Skill.INSIGHT, 
        Skill.INVESTIGATION, 
        Skill.NATURE, 
        Skill.PERCEPTION, 
        Skill.SURVIVAL
    ],
)

CLERIC = ClassTemplate(
    name=CharacterClass.CLERIC,
    hit_die=8,
    saving_throws=[Stat.WIS, Stat.CHA],
    primary_stat=Stat.WIS,
    recommended_stats={
        Stat.STR: 13,
        Stat.DEX: 10,
        Stat.CON: 14,
        Stat.INT: 8,
        Stat.WIS: 15,
        Stat.CHA: 12,
    },
    skills_count=2,
    available_skills=[
        Skill.HISTORY, 
        Skill.INSIGHT, 
        Skill.MEDICINE, 
        Skill.PERCEPTION, 
        Skill.RELIGION, 
        Skill.SURVIVAL
    ],
)

DRUID = ClassTemplate(
    name=CharacterClass.DRUID,
    hit_die=8,
    saving_throws=[Stat.WIS, Stat.INT],
    primary_stat=Stat.WIS,
    recommended_stats={
        Stat.STR: 8,
        Stat.DEX: 13,
        Stat.CON: 14,
        Stat.INT: 12,
        Stat.WIS: 15,
        Stat.CHA: 10,
    },
    skills_count=2,
    available_skills=[
        Skill.ARCANA, 
        Skill.ANIMAL_HANDLING, 
        Skill.INSIGHT, 
        Skill.MEDICINE, 
        Skill.NATURE, 
        Skill.PERCEPTION, 
        Skill.SURVIVAL
    ],
)

WIZARD = ClassTemplate(
    name=CharacterClass.WIZARD,
    hit_die=6,                                  # Мало здоровья, но много магии
    saving_throws=[Stat.INT, Stat.WIS],
    primary_stat=Stat.INT,
    recommended_stats={
        Stat.STR: 8,
        Stat.DEX: 13,
        Stat.CON: 14,
        Stat.INT: 15,
        Stat.WIS: 12,
        Stat.CHA: 10,
    },
    skills_count=2,
    available_skills=[
        Skill.ARCANA, 
        Skill.HISTORY, 
        Skill.INSIGHT, 
        Skill.INVESTIGATION, 
        Skill.MEDICINE, 
        Skill.RELIGION
    ],
)

ARTIFICER = ClassTemplate(
    name=CharacterClass.ARTIFICER,
    hit_die=8,
    saving_throws=[Stat.INT, Stat.CON],
    primary_stat=Stat.INT,
    recommended_stats={
        Stat.STR: 8,
        Stat.DEX: 13,
        Stat.CON: 14,
        Stat.INT: 15,
        Stat.WIS: 12,
        Stat.CHA: 10,
    },
    skills_count=2,
    available_skills=[
        Skill.ARCANA, 
        Skill.HISTORY, 
        Skill.INSIGHT, 
        Skill.INVESTIGATION, 
        Skill.MEDICINE, 
        Skill.RELIGION
    ],
)

SORCERER = ClassTemplate(
    name=CharacterClass.SORCERER,
    hit_die=6,
    saving_throws=[Stat.INT, Stat.CHA],
    primary_stat=Stat.CHA,
    recommended_stats={
        Stat.STR: 8,
        Stat.DEX: 13,
        Stat.CON: 14,
        Stat.INT: 12,
        Stat.WIS: 15,
        Stat.CHA: 15,
    },  
    skills_count=2,
    available_skills=[
        Skill.ARCANA, 
        Skill.DECEPTION, 
        Skill.INSIGHT, 
        Skill.INTIMIDATION, 
        Skill.PERSUASION, 
        Skill.RELIGION
    ],
)

WITCH = ClassTemplate(
    name=CharacterClass.WITCH,
    hit_die=8,
    saving_throws=[Stat.INT, Stat.CHA],
    primary_stat=Stat.CHA,
    recommended_stats={
        Stat.STR: 8,
        Stat.DEX: 13,
        Stat.CON: 14,
        Stat.INT: 10,
        Stat.WIS: 12,
        Stat.CHA: 15,
    },  
    skills_count=2,
    available_skills=[
        Skill.ARCANA, 
        Skill.DECEPTION, 
        Skill.INSIGHT, 
        Skill.INTIMIDATION,
        Skill.PERSUASION, 
        Skill.RELIGION, 
    ],
)

# --- РЕЕСТР ВСЕХ КЛАССОВ ---

ALL_CLASSES = {
    CharacterClass.BARBARIAN: BARBARIAN,
    CharacterClass.FIGHTER: FIGHTER,
    CharacterClass.PALADIN: PALADIN,
    CharacterClass.MONK: MONK,
    CharacterClass.ROGUE: ROGUE,
    CharacterClass.RANGER: RANGER,
    CharacterClass.CLERIC: CLERIC,
    CharacterClass.DRUID: DRUID,
    CharacterClass.WIZARD: WIZARD,
    CharacterClass.ARTIFICER: ARTIFICER,
    CharacterClass.SORCERER: SORCERER,
    CharacterClass.WITCH: WITCH,
}