import time
from character import PlayerCharacter
from classes import BARBARIAN
from skills import Skill, Stat
from enemies import SKELETON, GOBLIN
from dice import roll_d20, roll_damage
from combat import run_combat

# Импортируем наши новые классы
from items import Item, Weapon, Armor, ItemType, EquipmentSlot

def make_skill_check(player: PlayerCharacter, skill: Skill, dc: int) -> bool:
    """Вспомогательная функция для проведения проверки навыка"""
    # 1. Берет бонус навыка из объекта персонажа
    modifier = player.get_skill_modifier(skill) 
    
    # 2. Вызывает функцию броска d20 (из файла dice.py)
    roll = roll_d20(modifier=modifier) 
    
    # 3. Логирует процесс в консоль (название проверки и сложность)
    print(f"\n[Проверка {skill.value[0]}] Сложность (DC): {dc}")
    time.sleep(1) # Создает паузу для драматизма
    
    # 4. Проверяет критические успехи/провалы и сравнивает результат с DC
    if roll["is_crit_success"]:
        return True
    elif roll["is_crit_fail"]:
        return False
        
    return roll["total"] >= dc

def play_crypt_level(player: PlayerCharacter):
    print("\n" + "="*50)
    print("ЛОКАЦИЯ: ЗАБРОШЕННЫЙ СКЛЕП (Версия с Инвентарем)")
    print("="*50)
    
    # Создаем предметы, которые можно найти в локации
    rusty_sword = Weapon(
        name="Ржавый двуручник",
        weight=3.5,
        damage_dice="2d6",
        damage_type="Рубящий",
        stat_bonuses={Stat.STR: 1} # Небольшой бонус к силе от баланса меча
    )
    
    bone_ring = Item(
        name="Кольцо Костяного Лорда",
        weight=0.1,
        item_type=ItemType.ACCESSORY,
        stat_bonuses={Stat.CON: 2}, # Кольцо дает +2 к Выносливости
        allowed_slots=[EquipmentSlot.RING_1, EquipmentSlot.RING_2]
    )

    chest_found = False
    ring_found = False


    
    while player.current_hp > 0:
        print("\n--- Доступные действия ---")
        print("1. Осмотреть завал камней (Скрытый сундук)")
        print("2. Обыскать кучу костей в углу")
        print("3. Идти вглубь коридора (Бой)")
        print("4. Открыть инвентарь и лист персонажа")
        print("0. Выйти из игры")
        
        choice = input("Твой выбор: ")
        
        if choice == "1":
            if chest_found:
                print("Здесь больше ничего нет, кроме разбитых камней.")
                continue
            
            print("\nТы пытаешься разобрать завал камней, надеясь найти что-то ценное...")
            # Проверка Атлетики (DC 14)
            if make_skill_check(player, Skill.ATHLETICS, dc=14):
                print(f"Удача! Под камнями спрятан сундук. Внутри лежит {rusty_sword.name}!")
                player.inventory.add_item(rusty_sword)
                
                equip_choice = input(f"Экипировать {rusty_sword.name} сейчас? (y/n): ")
                if equip_choice.lower() == 'y':
                    player.inventory.equip(rusty_sword, EquipmentSlot.MAIN_HAND)
                chest_found = True
            else:
                print("Камни слишком тяжелые. Ты только зря потратил силы.")

        elif choice == "2":
            if ring_found:
                print("В этой куче только прах и обломки.")
                continue
                
            print("\nТы аккуратно перебираешь старые кости...")
            # Проверка Внимательности (DC 12)
            if make_skill_check(player, Skill.PERCEPTION, dc=12):
                print(f"Твой взгляд упал на тусклое мерцание. Ты нашел {bone_ring.name}!")
                player.inventory.add_item(bone_ring)
                
                equip_choice = input(f"Надеть {bone_ring.name} на палец? (y/n): ")
                if equip_choice.lower() == 'y':
                    player.inventory.equip(bone_ring, EquipmentSlot.RING_1)
                ring_found = True
            else:
                print("Ничего, кроме гнилых костей. Твое воображение сыграло с тобой шутку.")

        elif choice == "3":
            print("\nТы входишь в главный зал склепа...")
            # Сначала проверяем, как изменились статы перед боем
            player.show_character_sheet()
            time.sleep(2)
            
            print("\nИз тьмы выходят Скелеты!")
            run_combat(player, SKELETON)
            
            if player.current_hp > 0:
                print("\nПобеда в первом бою! Ты чувствуешь, как тяжесть снаряжения помогает (или мешает) тебе.")
                # Здесь можно добавить логику получения опыта, которую мы обсуждали ранее
                break

        elif choice == "4":
            player.show_character_sheet()
            input("\nНажми Enter, чтобы продолжить...")

        elif choice == "0":
            break