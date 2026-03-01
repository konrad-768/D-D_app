from dataclasses import dataclass, field
from typing import Dict, List, Optional
from skills import Stat, Skill
from enum import Enum

class DamageType(Enum):
    SLASHING = "Рубящий"
    PIERCING = "Колющий"
    BLUDGEONING = "Дробящий"
    FIRE = "Огонь"
    POISON = "Яд"
    # Можно добавить магические типы урона потом

@dataclass
class Action:
    name: str
    description: str
    is_attack: bool = False
    hit_bonus: int = 0              # Бонус к попаданию (например, +4)
    damage_dice: str = ""           # Формула урона (например, "1d6 + 2")
    damage_type: Optional[DamageType] = None

@dataclass
class EnemyTemplate:
    name: str
    description: str
    challenge_rating: float         # Уровень опасности (CR), например 0.25 или 1
    armor_class: int                # Класс брони (AC)
    hit_points: int                 # Среднее здоровье (HP)
    hit_dice: str                   # Формула кубиков здоровья (например, "2d6")
    speed: int                      # Скорость (в футах или метрах)
    
    # Характеристики (Сила, Ловкость и т.д.)
    stats: Dict[Stat, int]
    
    # Навыки, в которых враг хорош (сразу готовый бонус, чтобы не считать)
    skills: Dict[Skill, int] = field(default_factory=dict)
    
    # Список атак и способностей
    actions: List[Action] = field(default_factory=list)

    def get_modifier(self, stat: Stat) -> int:
        """Вспомогательный метод для расчета модификатора характеристики"""
        return (self.stats[stat] - 10) // 2
    
# --- БЕСТИАРИЙ ---

GOBLIN = EnemyTemplate(
    name="Гоблин",
    description="Маленький, злобный гуманоид, предпочитающий нападать из засады.",
    challenge_rating=0.25,
    armor_class=15, # Кожаная броня + щит
    hit_points=7,
    hit_dice="2d6",
    speed=30,
    stats={
        Stat.STR: 8,
        Stat.DEX: 14,
        Stat.CON: 10,
        Stat.INT: 10,
        Stat.WIS: 8,
        Stat.CHA: 8,
    },
    skills={
        Skill.STEALTH: 6, # Гоблины отлично прячутся
    },
    actions=[
        Action(
            name="Скимитар",
            description="Рукопашная атака оружием.",
            is_attack=True,
            hit_bonus=4,
            damage_dice="1d6 + 2",
            damage_type=DamageType.SLASHING
        ),
        Action(
            name="Короткий лук",
            description="Дальнобойная атака оружием.",
            is_attack=True,
            hit_bonus=4,
            damage_dice="1d6 + 2",
            damage_type=DamageType.PIERCING
        )
    ]
)

SKELETON = EnemyTemplate(
    name="Скелет",
    description="Оживший костяк, лишенный плоти и собственной воли.",
    challenge_rating=0.25,
    armor_class=13, # Обрывки брони
    hit_points=13,
    hit_dice="2d8 + 4",
    speed=30,
    stats={
        Stat.STR: 10,
        Stat.DEX: 14,
        Stat.CON: 15,
        Stat.INT: 6,
        Stat.WIS: 8,
        Stat.CHA: 5,
    },
    skills={}, # У простых скелетов нет особых навыков
    actions=[
        Action(
            name="Короткий меч",
            description="Рукопашная атака оружием.",
            is_attack=True,
            hit_bonus=4,
            damage_dice="1d6 + 2",
            damage_type=DamageType.PIERCING
        )
    ]
)

# Словарь для удобного поиска врагов по имени
ALL_ENEMIES = {
    "Goblin": GOBLIN,
    "Skeleton": SKELETON,
}