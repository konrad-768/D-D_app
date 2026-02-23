import random
from character import Character
from skills import Stat, Skill

# Создаем персонажей
warrior = Character(
    name="Варвар Грог",
    stats={Stat.STR: 16, Stat.DEX: 12, Stat.CON: 15, Stat.INT: 8, Stat.WIS: 10, Stat.CHA: 10},
    proficiencies=[Skill.ATHLETICS],
    hp=12,
    ac=14, # Средний доспех
    weapon_die=12 # Двуручный топор (d12)
)

goblin = Character(
    name="Гоблин Сник",
    stats={Stat.STR: 8, Stat.DEX: 16, Stat.CON: 10, Stat.INT: 10, Stat.WIS: 8, Stat.CHA: 8},
    proficiencies=[Skill.STEALTH],
    hp=7,
    ac=15, # Высокая ловкость делает его трудным мишенью
    weapon_die=6 # Короткий меч (d6)
)

# Цикл боя
print(f"--- БИТВА НАЧИНАЕТСЯ: {warrior.name} vs {goblin.name} ---")
round_num = 1

while warrior.current_hp > 0 and goblin.current_hp > 0:
    print(f"\nРаунд {round_num}")
    warrior.attack(goblin)
    if goblin.current_hp <= 0:
        print(f"\n{goblin.name} повержен!")
        break
    
    goblin.attack(warrior)
    if warrior.current_hp <= 0:
        print(f"\n{warrior.name} пал в бою...")
        break
    round_num += 1