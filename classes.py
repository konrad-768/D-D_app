from skills import Stat, Skill

CLASS_TEMPLATES = {
    "Fighter": {
        "hit_die": 10,  # d10 — золотой стандарт бойца
        "saving_throws": [Stat.STR, Stat.CON],  # Спасброски: Атлетика и Стойкость
        "skills_count": 2,  # Сколько навыков игрок может выбрать из списка ниже
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
    "Rogue": {
        "hit_die": 8,   # d8 — чуть меньше здоровья, чем у воина
        "saving_throws": [Stat.DEX, Stat.INT],
        "skills_count": 4,  # Плут — мастер навыков, выбирает 4
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
    "Barbarian": {
        "hit_die": 12,  # Самый большой запас здоровья в игре
        "saving_throws": [Stat.STR, Stat.CON],
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
    "Wizard": {
        "hit_die": 6,   # Мало здоровья, но много магии
        "saving_throws": [Stat.INT, Stat.WIS],
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
    "Cleric": {
        "hit_die": 8,
        "saving_throws": [Stat.WIS, Stat.CHA],
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
    "Paladin": {
        "hit_die": 10,
        "saving_throws": [Stat.WIS, Stat.CHA],
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
    "Ranger": {
        "hit_die": 10,
        "saving_throws": [Stat.STR, Stat.DEX],
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
}