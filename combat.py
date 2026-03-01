import time
from character import PlayerCharacter
from enemies import EnemyTemplate, Action
from dice import roll_d20, roll_damage
from skills import Stat

class ActiveEnemy:
    """Конкретный противник в бою, созданный на основе шаблона."""
    def __init__(self, template: EnemyTemplate):
        self.template = template
        self.name = template.name
        self.max_hp = template.hit_points
        self.current_hp = self.max_hp
        self.armor_class = template.armor_class
        self.actions = template.actions

    def take_damage(self, amount: int):
        self.current_hp = max(0, self.current_hp - amount)
        print(f"[{self.name}] получает {amount} урона! (Осталось ХП: {self.current_hp}/{self.max_hp})")

    @property
    def is_alive(self) -> bool:
        return self.current_hp > 0


def execute_attack(attacker_name: str, hit_bonus: int, damage_dice: str, target_name: str, target_ac: int) -> int:
    """Базовая механика атаки: бросок на попадание -> проверка брони -> бросок урона."""
    print(f"\n>>> {attacker_name} атакует {target_name}!")
    time.sleep(1) # Небольшая пауза для эффекта погружения
    
    attack_roll = roll_d20(modifier=hit_bonus)
    
    if attack_roll["is_crit_fail"]:
        print(f"Критический промах! {attacker_name} неуклюже спотыкается.")
        return 0
        
    if attack_roll["is_crit_success"]:
        print("КРИТИЧЕСКОЕ ПОПАДАНИЕ!")
        # При крите урон удваивается (просто кидаем формулу дважды)
        damage = roll_damage(damage_dice) + roll_damage(damage_dice)
        return damage
        
    print(f"Бросок атаки: {attack_roll['base_roll']} + {hit_bonus} = {attack_roll['total']} против AC {target_ac}")
    
    if attack_roll["total"] >= target_ac:
        print("Попадание!")
        return roll_damage(damage_dice)
    else:
        print("Промах! Броня или уклонение спасают цель.")
        return 0


def run_combat(player: PlayerCharacter, enemy_template: EnemyTemplate):
    """Основной цикл боя до смерти одного из участников."""
    enemy = ActiveEnemy(enemy_template)
    print(f"\n=== БОЙ НАЧИНАЕТСЯ: {player.name} против {enemy.name} ===")
    
    round_num = 1
    while player.current_hp > 0 and enemy.is_alive:
        print(f"\n--- Раунд {round_num} ---")
        
        # 1. Ход игрока
        # Для простоты пока считаем, что игрок бьет длинным мечом (от Силы)
        # Урон: 1d8 + модификатор силы. Бонус к попаданию: Сила + Мастерство
        str_mod = player.get_stat_modifier(Stat.STR)
        player_hit_bonus = str_mod + player.proficiency_bonus
        player_damage_formula = f"1d8+{str_mod}" if str_mod >= 0 else f"1d8{str_mod}"
        
        damage_dealt = execute_attack(
            attacker_name=player.name,
            hit_bonus=player_hit_bonus,
            damage_dice=player_damage_formula,
            target_name=enemy.name,
            target_ac=enemy.armor_class
        )
        if damage_dealt > 0:
            enemy.take_damage(damage_dealt)
            
        if not enemy.is_alive:
            print(f"\n🏆 {enemy.name} повержен! {player.name} побеждает в бою!")
            break
            
        # 2. Ход врага
        # Берем первую атаку из списка действий врага
        enemy_action = enemy.actions[0] 
        damage_taken = execute_attack(
            attacker_name=enemy.name,
            hit_bonus=enemy_action.hit_bonus,
            damage_dice=enemy_action.damage_dice,
            target_name=player.name,
            target_ac=14 # Заглушка: пока у игрока нет брони, поставим AC 14
        )
        if damage_taken > 0:
            player.take_damage(damage_taken)
            
        if player.current_hp <= 0:
            print(f"\n💀 {player.name} пал в бою... Игра окончена.")
            break
            
        round_num += 1

# # --- Блок тестирования ---
# #if __name__ == "__main__":
#     from classes import BARBARIAN
#     from enemies import GOBLIN
#     from skills import Skill
    
#     conan = PlayerCharacter(
#         name="Конан",
#         character_class=BARBARIAN,
#         stats=BARBARIAN.recommended_stats,
#         selected_skills=[Skill.ATHLETICS, Skill.SURVIVAL]
#     )
    
#     run_combat(conan, GOBLIN)