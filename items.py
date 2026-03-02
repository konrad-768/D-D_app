from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional


from skills import Stat

class EquipmentSlot(Enum):
    """Определяет все возможные позиции для экипировки на 'кукле' персонажа"""
    MAIN_HAND = auto()   # Правая рука (Оружие)
    OFF_HAND = auto()    # Левая рука (Щит, кинжал, факел)
    BODY = auto()        # Доспех / Одежда
    HEAD = auto()        # Шлем / Капюшон
    RING_1 = auto()      # Первое кольцо
    RING_2 = auto()      # Второе кольцо
    AMULET = auto()      # Шея
    FEET = auto()        # Сапоги (на будущее)

class ItemType(Enum):
    """Категории предметов для фильтрации в инвентаре"""
    WEAPON = "Оружие"
    ARMOR = "Броня"
    ACCESSORY = "Аксессуар"
    CONSUMABLE = "Расходник"
    MISC = "Разное"

@dataclass
class Item:
    """Базовый класс для любого предмета в игре"""
    name: str
    weight: float
    item_type: ItemType = ItemType.MISC
    description: str = ""
    # Бонусы к статам: {Stat.STR: 2, Stat.CON: 1}
    stat_bonuses: Dict[Stat, int] = field(default_factory=dict)
    
    # Список слотов, в которые можно надеть этот предмет
    # Если список пустой — предмет нельзя экипировать (например, хлам или зелье)
    allowed_slots: List[EquipmentSlot] = field(default_factory=list)

@dataclass
class Weapon(Item):
    """Класс для мечей, топоров и прочего вооружения"""
    damage_dice: str = "1d6"
    damage_type: str = "Физический"
    
    def __post_init__(self):
        self.item_type = ItemType.WEAPON
        # Оружие по умолчанию идет в правую руку, но может и в левую (если одноручное)
        if not self.allowed_slots:
            self.allowed_slots = [EquipmentSlot.MAIN_HAND, EquipmentSlot.OFF_HAND]

@dataclass
class Armor(Item):
    """Класс для доспехов"""
    ac_bonus: int = 0
    stealth_disadvantage: bool = False
    
    def __post_init__(self):
        self.item_type = ItemType.ARMOR
        if not self.allowed_slots:
            self.allowed_slots = [EquipmentSlot.BODY]

class InventoryManager:
    """Менеджер, отвечающий за хранение и ношение вещей"""
    def __init__(self, owner_strength: int = 10):
        self.items: List[Item] = []
        # Инициализируем пустую куклу персонажа через Enum
        self.equipped: Dict[EquipmentSlot, Optional[Item]] = {slot: None for slot in EquipmentSlot}
        self.capacity_multiplier = 5  # Коэффициент грузоподъемности (D&D стайл)

    def add_item(self, item: Item) -> bool:
        """Добавить предмет в общую сумку"""
        self.items.append(item)
        print(f"Предмет '{item.name}' добавлен в инвентарь.")
        return True

    def equip(self, item: Item, slot: EquipmentSlot) -> bool:
        """Попытка надеть предмет в указанный слот"""
        if item not in self.items:
            print(f"Ошибка: {item.name} нет в инвентаре.")
            return False
        
        if slot not in item.allowed_slots:
            print(f"Ошибка: {item.name} нельзя надеть в слот {slot.name}.")
            return False
        
        # Если слот занят — "снимаем" старую вещь (логику снятия можно дописать)
        self.equipped[slot] = item
        print(f"Успех: {item.name} теперь в слоте {slot.name}.")
        return True

    def get_total_weight(self) -> float:
        """Суммарный вес всех вещей в сумке и на теле"""
        return sum(item.weight for item in self.items)

    def get_all_stat_bonuses(self) -> Dict[Stat, int]:
        """Собирает сумму всех бонусов со всех надетых предметов"""
        total_bonuses = {}
        for item in self.equipped.values():
            if item:
                for stat, value in item.stat_bonuses.items():
                    total_bonuses[stat] = total_bonuses.get(stat, 0) + value
        return total_bonuses

    def show_inventory(self):
        """Консольная визуализация инвентаря"""
        print("\n=== ЭКИПИРОВКА ===")
        for slot, item in self.equipped.items():
            item_name = item.name if item else "Пусто"
            print(f"{slot.name:10}: {item_name}")
        print(f"Общий вес: {self.get_total_weight()} кг")