import random 
from enum import Enum
from skills import Stat, Skill

class Character:
    def __init__(self, name, stats, proficiencies, hp, ac, weapon_die=6):
        self.name = name
        self.stats = stats  # Dict {Stat.STR: 16, ...}
        self.proficiencies = proficiencies  # List of Skill Enums
        self.max_hp = hp
        self.current_hp = hp
        self.ac = ac # Armor Class (Класс Доспеха)
        self.weapon_die = weapon_die # Кубик урона оружия (d6, d8, d12)
        self.level = 1

    def get_mod(self, stat_enum):
        return (self.stats[stat_enum] - 10) // 2

    @property
    def prof_bonus(self):
        return (self.level - 1) // 4 + 2

    def attack(self, target):
        # 1. Бросок на попадание: d20 + Сила + Бонус мастерства
        roll = random.randint(1, 20)
        attack_total = roll + self.get_mod(Stat.STR) + self.prof_bonus
        
        print(f"[{self.name}] атакует [{target.name}]: Выпало {roll} (Итого {attack_total})")

        # 2. Проверка: попал ли?
        if roll == 20:
            print("КРИТИЧЕСКИЙ УДАР!")
            damage = random.randint(1, self.weapon_die) + random.randint(1, self.weapon_die) + self.get_mod(Stat.STR)
        elif attack_total >= target.ac:
            damage = random.randint(1, self.weapon_die) + self.get_mod(Stat.STR)
        else:
            print(f"Промах! (Нужно было побить КД {target.ac})")
            return

        # 3. Нанесение урона
        target.current_hp -= max(1, damage) # Минимум 1 урона
        print(f"Попадание! Нанесено {damage} урона. У {target.name} осталось {max(0, target.current_hp)} HP.")
        


        

        