class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, amount):
        """Уменьшает очки здоровья героя на принимаемую величину"""
        real_damage = max(0, amount - self.defense)
        self.health -= real_damage
        if self.health > 0:
            print(f"💥 {self.name} нанёс {amount} урона. Текущее здоровье: {self.health}")
            self.is_alive()

    def is_alive(self):
        """Проверят жив ли враг"""
        if self.health > 0:
            return True
        else:
            return False