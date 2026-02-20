from enemy import Enemy
from character import Character 

warior = Character("Воин", 100, 20, 10)
goblin = Enemy("Гоблин", 50, 15, 5)

# Пример боя
print(f"{warior.name} вступает в бой с {goblin.name}!")
while warior.is_alive() and goblin.is_alive():
    # Воин атакует Гоблина
    warior.attack_target(goblin)

    if not goblin.is_alive():
        print(f"{goblin.name} повержен!")
        break

    # Гоблин атакует Воина
    goblin.attack_target(warior)

    if not warior.is_alive():
        print(f"{warior.name} повержен!")
        break