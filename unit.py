import random

class Unit:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health # Здоровье
        self.attack = attack # Сила атаки
        self.defense = defense # Защита

    def take_damage(self, damage):
        damage = random.randint(self.attack - 3, self.attack + 3) # Варьируем урон для реалистичности
        real_damage = max(0, damage - self.defense) # Урон не может быть меньше 0
        self.health -= real_damage # Вычитаем реальный урон из здоровья
        print(f"{self.name} получает {damage} урона! (Осталось здоровья: {self.health})") 

    def is_alive(self):
        return self.health > 0

    def attack_target(self, target): # Метод для атаки цели
        print(f"{self.name} атакует {target.name}!")
        target.take_damage(self.attack)



