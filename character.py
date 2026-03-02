from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math

# Cущности для персонажа, его характеристик, навыков и инвентаря
from skills import Stat, Skill
from classes import ClassTemplate
# Система инвентаря и предметов
from items import Item, Weapon, Armor, ItemType, EquipmentSlot, InventoryManager

@dataclass
class PlayerCharacter:
    name: str
    character_class: ClassTemplate
    stats: Dict[Stat, int]
    selected_skills: List[Skill]
    level: int = 1
    
    # Поля, вычисляемые автоматически
    max_hp: int = field(init=False)
    current_hp: int = field(init=False)
    inventory: InventoryManager = field(init=False)

    def __post_init__(self):
        """Инициализация после создания объекта"""
        
        # 1. Валидация навыков (твой оригинальный код)
        if not self.character_class.validate_skill_selection(self.selected_skills):
            raise ValueError(f"Ошибка навыков у {self.name}!")

        # 2. Инициализация инвентаря
        self.inventory = InventoryManager()

        # 3. Рассчитываем HP (1 уровень: max_hit_die + mod)
        con_mod = self.get_stat_modifier(Stat.CON)
        self.max_hp = self.character_class.hit_die + con_mod 
        self.current_hp = self.max_hp

    # --- ЛОГИКА ХАРАКТЕРИСТИК С УЧЕТОМ ЭКИПИРОВКИ ---

    def get_full_stat_value(self, stat: Stat) -> int:
        """Базовое значение + бонусы от всех надетых колец, брони и т.д."""
        base_value = self.stats.get(stat, 10)
        bonuses = self.inventory.get_all_stat_bonuses()
        return base_value + bonuses.get(stat, 0)

    def get_stat_modifier(self, stat: Stat) -> int:
        """Итоговый модификатор (например, +3), учитывающий вещи"""
        full_value = self.get_full_stat_value(stat)
        return math.floor((full_value - 10) / 2)

    @property
    def armor_class(self) -> int:
        """Автоматический расчет КД (AC)"""
        # База 10 + Ловкость
        ac = 10 + self.get_stat_modifier(Stat.DEX)
        
        # Добавляем бонус от надетой брони (слот BODY)
        equipped_armor = self.inventory.equipped[EquipmentSlot.BODY]
        if isinstance(equipped_armor, Armor):
            ac += equipped_armor.ac_bonus
            
        return ac

    @property
    def proficiency_bonus(self) -> int:
        return 2 + (self.level - 1) // 4

    # --- БОЕВАЯ ЛОГИКА ---

    def get_attack_data(self) -> dict:
        """Возвращает данные для совершения атаки"""
        main_weapon = self.inventory.equipped[EquipmentSlot.MAIN_HAND]
        
        # Для варвара используем Силу
        str_mod = self.get_stat_modifier(Stat.STR)
        
        if isinstance(main_weapon, Weapon):
            return {
                "name": main_weapon.name,
                "bonus": str_mod + self.proficiency_bonus,
                "damage": f"{main_weapon.damage_dice} + {str_mod}",
                "type": main_weapon.damage_type
            }
        
        return {
            "name": "Кулаки",
            "bonus": str_mod + self.proficiency_bonus,
            "damage": f"1 + {str_mod}",
            "type": "Дробящий"
        }

    # --- МЕТОДЫ СОСТОЯНИЯ ---

    def take_damage(self, amount: int):
        self.current_hp = max(0, self.current_hp - amount)
        print(f"-> {self.name} ранен на {amount}. HP: {self.current_hp}/{self.max_hp}")

    def show_character_sheet(self):
        attack = self.get_attack_data()
        print(f"\n" + "="*30)
        print(f"ГЕРОЙ: {self.name} | Уровень: {self.level}")
        print(f"КЛАСС: {self.character_class.name.value}")
        print(f"HP: {self.current_hp}/{self.max_hp} | AC: {self.armor_class}")
        print(f"ОРУЖИЕ: {attack['name']} (Бросок: +{attack['bonus']}, Урон: {attack['damage']})")
        print("-" * 30)
        print("ХАРАКТЕРИСТИКИ (с учетом бонусов):")
        for stat in Stat:
            val = self.get_full_stat_value(stat)
            mod = self.get_stat_modifier(stat)
            print(f"  {stat.value:15}: {val} ({'+' if mod >= 0 else ''}{mod})")
        
        self.inventory.show_inventory()
        print("="*30 + "\n")