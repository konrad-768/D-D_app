import random
import re
from typing import Dict, Any

def roll(sides: int) -> int:
    """Бросает один кубик с указанным количеством граней (например, d6, d8)."""
    return random.randint(1, sides)

def roll_d20(modifier: int = 0, advantage: bool = False, disadvantage: bool = False) -> Dict[str, Any]:
    """
    Бросок d20 с модификатором. 
    Возвращает словарь с подробностями броска (чтобы знать, выпал ли Крит!).
    """
    roll1 = roll(20)
    roll2 = roll(20)
    
    # Механика преимущества (кидаем 2 раза, берем большее) и помехи (берем меньшее)
    if advantage and not disadvantage:
        base_roll = max(roll1, roll2)
    elif disadvantage and not advantage:
        base_roll = min(roll1, roll2)
    else:
        base_roll = roll1 # Обычный бросок
        
    total = base_roll + modifier
    
    # Обработка критических успехов и провалов
    is_crit_success = (base_roll == 20)
    is_crit_fail = (base_roll == 1)
    
    return {
        "base_roll": base_roll,
        "modifier": modifier,
        "total": total,
        "is_crit_success": is_crit_success,
        "is_crit_fail": is_crit_fail
    }

def roll_damage(formula: str) -> int:
    """
    Парсит и бросает формулу урона, например '1d6 + 2' или '2d8-1'.
    """
    # Убираем все пробелы для удобства парсинга
    formula = formula.replace(" ", "") 
    
    # Регулярное выражение, которое ищет: (число)d(число)(+ или - число)
    match = re.match(r"(\d+)d(\d+)([\+\-]\d+)?", formula)
    
    if not match:
        # Если это просто статичное число (например, "5")
        if formula.isdigit():
            return int(formula)
        raise ValueError(f"Неверный формат формулы кубиков: {formula}")
        
    count = int(match.group(1))      # Сколько кубиков (например, 1)
    sides = int(match.group(2))      # Грани кубика (например, 6)
    modifier_str = match.group(3)    # Модификатор (например, "+2")
    
    total_damage = sum(roll(sides) for _ in range(count))
        
    if modifier_str:
        total_damage += int(modifier_str)
        
    # Урон не может быть отрицательным (если выбросили 1 и модификатор -2)
    return max(0, total_damage) 
