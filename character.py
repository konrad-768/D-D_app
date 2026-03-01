from dataclasses import dataclass, field
from typing import Dict, List
import math

# Импортируем наши заготовки
from skills import Stat, Skill
from classes import ClassTemplate

@dataclass
class PlayerCharacter:
    name: str
    character_class: ClassTemplate
    stats: Dict[Stat, int]
    selected_skills: List[Skill]
    level: int = 1
    
    # Поля, которые вычисляются автоматически при создании
    max_hp: int = field(init=False)
    current_hp: int = field(init=False)

    def __post_init__(self):
        """Этот метод автоматически запускается после создания объекта"""
        
        # 1. Проверяем, правильно ли игрок выбрал навыки
        if not self.character_class.validate_skill_selection(self.selected_skills):
            raise ValueError(
                f"Ошибка создания персонажа {self.name}! "
                f"Класс {self.character_class.name.value} должен выбрать "
                f"{self.character_class.skills_count} навыка из своего списка."
            )

        # 2. Рассчитываем стартовое здоровье (Макс. значение кубика + мод. Телосложения)
        con_mod = self.get_stat_modifier(Stat.CON)
        # На 1 уровне всегда дается максимум ХП
        self.max_hp = self.character_class.hit_die + con_mod 
        self.current_hp = self.max_hp

    @property
    def proficiency_bonus(self) -> int:
        """Бонус мастерства зависит от уровня (+2 на 1-4 ур., +3 на 5-8 ур. и т.д.)"""
        return 2 + (self.level - 1) // 4

    def get_stat_modifier(self, stat: Stat) -> int:
        """
        Стандартная формула перевода характеристики в модификатор:
        (Значение - 10) / 2, с округлением вниз.
        Например: 15 -> +2, 8 -> -1, 10 -> 0.
        """
        return math.floor((self.stats[stat] - 10) / 2)

    def get_skill_modifier(self, skill: Skill) -> int:
        """
        Считает итоговый бонус для броска навыка.
        """
        # В твоем skills.py значение навыка — это кортеж ("Имя", Базовый Стат).
        # Достаем базовый стат под индексом 1.
        base_stat = skill.value[1]
        
        # Берем модификатор от характеристики (например, от Ловкости для Скрытности)
        total_bonus = self.get_stat_modifier(base_stat)
        
        # Если персонаж владеет этим навыком, добавляем бонус мастерства
        if skill in self.selected_skills:
            total_bonus += self.proficiency_bonus
            
        return total_bonus

    def take_damage(self, amount: int):
        """Получение урона"""
        self.current_hp = max(0, self.current_hp - amount)
        print(f"{self.name} получает {amount} урона. Осталось ХП: {self.current_hp}/{self.max_hp}")

    def heal(self, amount: int):
        """Лечение"""
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        print(f"{self.name} лечится на {amount}. Текущее ХП: {self.current_hp}/{self.max_hp}")
        
    def show_character_sheet(self):
        """Красивый вывод информации о персонаже"""
        print(f"--- Лист Персонажа: {self.name} ---")
        print(f"Класс: {self.character_class.name.value} | Уровень: {self.level}")
        print(f"HP: {self.current_hp}/{self.max_hp} | Бонус мастерства: +{self.proficiency_bonus}")
        print("\nХарактеристики:")
        for stat, value in self.stats.items():
            mod = self.get_stat_modifier(stat)
            mod_str = f"+{mod}" if mod >= 0 else str(mod)
            print(f"  {stat.value}: {value} ({mod_str})")
