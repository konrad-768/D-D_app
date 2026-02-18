from character import Character
from enemy import Enemy

warior = Character("Воин", 100, 20, 10)
goblin = Enemy("Гоблин", 50, 15, 5)

# Пример боя
print(f"{warior.name} вступает в бой с {goblin.name}!")
while warior.is_alive() and goblin.is_alive():
    # Воин атакует Гоблина
    print(f"{warior.name} атакует {goblin.name}!")
    goblin.take_damage(warior.attack)

    if not goblin.is_alive():
        print(f"{goblin.name} повержен!")
        break

    # Гоблин атакует Воина
    print(f"{goblin.name} атакует {warior.name}!")
    warior.take_damage(goblin.attack)

    if not warior.is_alive():
        print(f"{warior.name} повержен!")
        break