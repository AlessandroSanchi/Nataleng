import random
import time
import art
from termcolor import colored

# ASCII Art for the game title
Art = art.text2art("Welcome to Untitled Farming Game")
Art_c = colored(Art, "magenta")
print(Art_c)

# Player class
class Player:
    def __init__(self):
        self.armor_equipped = ""
        self.money = 15000000
        self.coins = 10000000
        self.bonus_multiplier = 1
        self.godpass = False
        self.sword_equipped = ""
        self.player_hp = 100
        self.player_damage = 0
        self.new_swords = NEW_SWORDS
        self.power_ups = POWER_UPS
        self.armor = ARMOR

    def format_price(self, price) -> str:
        if price >= 1_000_000:
            return colored(f"${price/1_000_000:.1f}M", "yellow")
        elif price >= 1_000:
            return colored(f"${price/1_000:.1f}K", "yellow")
        else:
            return colored(f"${price}", "yellow")

    def equip_sword(self, sword_name):
        if sword_name in self.new_swords:
            if self.new_swords[sword_name]["stock"] > 0:
                if self.new_swords[sword_name]["damage"] < self.player_damage:
                    self.money -= self.new_swords[sword_name]["price"]
                    self.new_swords[sword_name]["stock"] -= 1
                    print(colored(f"You bought {sword_name} but did not equip it as it's weaker.", "red"))
                else:
                    self.sword_equipped = sword_name
                    self.player_damage = self.new_swords[sword_name]["damage"]
                    self.new_swords[sword_name]["stock"] -= 1
                    print(colored(f"Equipped {sword_name}. Player Damage increased to {self.player_damage}!", "green"))
            else:
                print(colored(f"{sword_name} is out of stock.", "red"))
        else:
            print(colored("Failed to equip sword. Sword not found.", "red"))

    def equip_armor(self, armor_name):
        if armor_name in self.armor:
            if self.armor[armor_name]["stock"] > 0:
                self.armor_equipped = armor_name
                self.player_hp += self.armor[armor_name]["hp"]
                self.armor[armor_name]["stock"] -= 1
                print(colored(f"Equipped {armor_name}. Player HP increased to {self.player_hp}!", "green"))
            else:
                print(colored(f"{armor_name} is out of stock.", "red"))
        else:
            print(colored("Failed to equip armor. Armor not found.", "red"))

# Worlds class
class Worlds:
    def __init__(self):
        self.cave_unlocked = False
        self.jungle_unlocked = False
        self.desert_unlocked = False
        self.void_unlocked = False

    def explore(self, world_name, player):
        if world_name in WORLD_ITEMS:
            print(colored(f"Farming in the {world_name}...", "green"))
            items = WORLD_ITEMS[world_name]["items"]
            weights = WORLD_ITEMS[world_name]["weights"]

            while True:
                random_item = random.choices(list(items.keys()), weights=weights, k=1)[0]
                money_added = items.get(random_item, 0) * player.bonus_multiplier
                player.money += money_added
                print(colored(f"You found {random_item}! Added ${money_added} Total money: ${player.money}", "yellow"))
                time.sleep(1.5)
                menu = input(colored("Write whatever to stop exploring or type 'c' to continue: ", "cyan"))
                if menu != "c":
                    break

# Game class
class Game:
    def __init__(self):
        self.player = Player()
        self.world = Worlds()
        self.running = True

    def input_page(self):
        print(colored("-1 Farm", "green"))
        print(colored("-2 Shop", "cyan"))
        print(colored("-3 Fight", "light_blue"))
        print(colored("- 4 Quit", "light_magenta"))
        money_c = colored(f"Money: ${self.player.money}", "light_yellow")
        coins_c = colored(f"Coins: £{self.player.coins}", "yellow")
        print(money_c)
        print(coins_c)

    def shop(self):
        print(colored("------------", "cyan"))
        print(colored("Welcome to the Shop!", "cyan"))
        print(colored("------------", "cyan"))
        print(colored("Available Swords:", "light_cyan"))
        for sword, details in self.player.new_swords.items():
            print(f"{sword}: {self.player.format_price(details['price'])} (Stock: {details['stock']})")
        print(colored("------------", "cyan"))
        print(colored("Available Armor:", "light_cyan"))
        for armor, details in self.player.armor.items():
            print(f"{armor}: {self.player.format_price(details['price'])} (Stock: {details['stock']})")
        print(colored("------------", "cyan"))
        print(colored("Available Power-Ups:", "light_cyan"))
        for power_up, details in self.player.power_ups.items():
            print(f"{power_up}: {self.player.format_price(details['price'])} (Stock: {details['stock']})")

        choice = input(colored("What would you like to buy? (Enter the item name or Enter to leave): ", "cyan")).strip().lower()
       
        # Handle sword purchase
        for sword in self.player.new_swords:
            if sword.lower() == choice:
                sword_price = self.player.new_swords[sword]["price"]
                if self.player.money >= sword_price and self.player.new_swords[sword]["stock"] > 0:
                    self.player.money -= sword_price
                    self.player.equip_sword(sword)
                    print(colored(f"You bought {sword}!", "green"))
                    print(colored(f"Current Sword Equipped: {self.player.sword_equipped}", "yellow"))  
                else:
                    print(colored("You don't have enough money or the item is out of stock.", "red"))
                return

        # Handle armor purchase
        for armor in self.player.armor:
            if armor.lower() == choice:
                armor_price = self.player.armor[armor]["price"]
                if self.player.money >= armor_price and self.player.armor[armor]["stock"] > 0:
                    self.player.money -= armor_price
                    self.player.equip_armor(armor)
                    print(colored(f"You bought {armor}!", "green"))
                else:
                    print(colored("You don't have enough money or the item is out of stock.", "red"))
                return

        # Handle power-up purchase
        for power_up in self.player.power_ups:
            if power_up.lower() == choice:
                power_up_price = self.player.power_ups[power_up]["price"]
                if self.player.money >= power_up_price and self.player.power_ups[power_up]["stock"] > 0:
                    self.player.money -= power_up_price
                    self.player.power_ups[power_up]["stock"] -= 1
                   
                    if power_up == "X2Pass":
                        self.player.bonus_multiplier *= 2
                        print(colored("You bought the X2Pass successfully! Now you will get 2x for all your earnings!", "green"))
                        self.player.power_ups[power_up]["price"] *= 2
                   
                    print(colored(f"You bought {power_up}!", "green"))
                else:
                    print(colored("You don't have enough money or the item is out of stock.", "red"))
                return
           
        if choice == 'exit':
            print(colored("Exiting the shop.", "yellow"))
        else:
            print(colored("Invalid choice. Please try again.", "red"))

    def initiate_battle(self, enemy_name, enemy_hp):
        player_hp = self.player.player_hp
        if self.player.armor_equipped:
            player_hp += self.player.armor[self.player.armor_equipped]["hp"]

        print(colored(f"You've encountered a {enemy_name} with {enemy_hp} HP!", "light_red"))
        time.sleep(1)

        while player_hp > 0 and enemy_hp > 0:
            # Attack
            enemy_hp -= self.player.player_damage
            print(colored(f"You attacked {enemy_name} and dealt {self.player.player_damage} damage!", "green"))
            time.sleep(1)

            if enemy_hp <= 0:
                print(colored(f"The {enemy_name} died!", "green"))
                loot = self.calculate_loot(enemy_name)
                self.player.coins += loot
                print(colored(f"Gained £{loot} Coins!", "yellow"))
                return loot

            enemy_damage = random.randint(ENEMY_LIST[enemy_name]["min_damage"], ENEMY_LIST[enemy_name]["max_damage"])
            player_hp -= enemy_damage
            print(colored(f"The {enemy_name} attacked and dealt {enemy_damage} damage!", "red"))
            time.sleep(0.5)

            if player_hp <= 0:
                print(colored("You Died.", "red"))
                return 0  
        return 0  

    def calculate_loot(self, enemy_name):
        loot = 0
        if enemy_name == "Goblin":
            loot = random.randint(50, 200)
        elif enemy_name == "Romagna":
            loot = random.randint(100, 300)
        elif enemy_name == "Bat":
            loot = random.randint(500, 1000)
        elif enemy_name == "Snake":
            loot = random.randint(4000, 4500)
        elif enemy_name == "Scorpion":
            loot = random.randint(42000, 65000)
        elif enemy_name == "Void Beast":
            loot = random.randint(115000, 150000)
        elif enemy_name == "Golem":
            loot = random.randint(1000, 1200)
        elif enemy_name == "Tiger":
            loot = random.randint(5000, 7000)
        elif enemy_name == "Mummy":
            loot = random.randint(35000, 50000)
        elif enemy_name == "Shadow Entity":
            loot = random.randint(100000, 150000)
        return loot

    def run(self):
        while self.running:
            print(colored("---------------------", "cyan"))
            self.input_page()
            choice = input(colored("What would you like to do? ", "light_blue"))

            if choice == "1":
                print(colored("Select World:", "blue"))
                print(colored("1. Forest", "green"))
                if self.world.cave_unlocked:
                    print(colored("2. Cave", "light_cyan"))
                else:
                    print(colored("2. Cave (Unlock for $15K)", "light_cyan"))
                if self.world.jungle_unlocked:
                    print(colored("3. Jungle", "light_green"))
                else:
                    print(colored("3. Jungle (Unlock for $50K)", "light_green"))
                if self.world.desert_unlocked:
                    print(colored("4. Desert", "yellow"))
                else:
                    print(colored("4. Desert (Unlock for $250K)", "yellow"))
                if self.world.void_unlocked:
                    print(colored("5. Void", "magenta"))
                else:
                    print(colored("5. Void (Unlock for $1M)", "magenta"))
               
                world_choice = input(colored("Enter your choice: ", "cyan"))

                if world_choice == "1":
                    self.world.explore("Forest", self.player)
                elif world_choice == "2":
                    if not self.world.cave_unlocked and self.player.money >= 15000:
                        self.player.money -= 15000
                        self.world.cave_unlocked = True
                        print(colored("You bought a ticket to the Cave and unlocked it!", "green"))
                    elif self.world.cave_unlocked:
                        self.world.explore("Cave", self.player)
                    else:
                        print(colored("Sorry, you don't have enough money to unlock the Cave.", "red"))
                elif world_choice == "3":
                    if not self.world.jungle_unlocked and self.player.money >= 50000:
                        self.player.money -= 50000
                        self.world.jungle_unlocked = True
                        print(colored("You bought a ticket to the Jungle and unlocked it!", "green"))
                    elif self.world.jungle_unlocked:
                        self.world.explore("Jungle", self.player)
                    else:
                        print(colored("Sorry, you don't have enough money to unlock the Jungle.", "red"))
                elif world_choice == "4":
                    if not self.world.desert_unlocked and self.player.money >= 250000:
                        self.player.money -= 250000
                        self.world.desert_unlocked = True
                        print(colored("You bought a ticket to the Desert and unlocked it!", "green"))
                    elif self.world.desert_unlocked:
                        self.world.explore("Desert", self.player)
                    else:
                        print(colored("Sorry, you don't have enough money to unlock the Desert.", "red"))
                elif world_choice == "5":
                    if not self.world.void_unlocked and self.player.money >= 1000000:
                        self.player.money -= 1000000
                        self.world.void_unlocked = True
                        print(colored("You bought a ticket to the Void and unlocked it!", "green"))
                    elif self.world.void_unlocked:
                        self.world.explore("Void", self.player)
                    else:
                        print(colored("Sorry, you don't have enough money to unlock the Void.", "red"))

            elif choice == "2":
                self.shop()

            elif choice == "3":
                if self.player.sword_equipped != "":
                    print(colored("Select World:", "blue"))
                    print(colored("1. Forest", "green"))
                    if self.world.cave_unlocked:
                        print(colored("2. Cave", "light_cyan"))
                    else:
                        print(colored("2. Cave (Unlock for £15K)", "light_cyan"))
                    if self.world.jungle_unlocked:
                        print(colored("3. Jungle", "light_green"))
                    else:
                        print(colored("3. Jungle (Unlock for £50K)", "light_green"))
                    if self.world.desert_unlocked:
                        print(colored("4. Desert", "yellow"))
                    else:
                        print(colored("4. Desert (Unlock for £250K)", "yellow"))
                    if self.world.void_unlocked:
                        print(colored("5. Void", "magenta"))
                    else:
                        print(colored("5. Void (Unlock for £1M)", "magenta"))
                   
                    world_choice = input(colored("Enter your choice: ", "cyan"))

                    if world_choice == "1":
                        print(colored("Entering the forest...", "green"))
                        while True:
                            enemy_list = ["Goblin", "Romagna"]
                            random_enemy = random.choice(enemy_list)
                            coins_gained = self.initiate_battle(random_enemy, random.randint(100, 300))
                            self.player.coins += coins_gained
                            user_input = input(colored("Write 'E' to stop fighting: ", "cyan"))
                            if user_input.lower() == "e":
                                break

                    elif world_choice == "2":
                        if not self.world.cave_unlocked and self.player.coins >= 15000:
                            self.player.coins -= 15000
                            self.world.cave_unlocked = True
                            print(colored("You bought a ticket to the Cave and unlocked it!", "green"))
                        elif not self.world.cave_unlocked:
                            print(colored("You need to unlock the Cave first!", "red"))
                            return
                        print(colored("Entering the cave...", "green"))
                        while self.world.cave_unlocked:
                            enemy_list = ["Bat", "Golem"]
                            random_enemy = random.choice(enemy_list)
                            coins_gained = self.initiate_battle(random_enemy, random.randint(300, 500))
                            self.player.coins += coins_gained
                            user_input = input(colored("Write 'E' to stop fighting: ", "cyan"))
                            if user_input.lower() == "e":
                                break

                    elif world_choice == "3":
                        if not self.world.jungle_unlocked and self.player.coins >= 50000:
                            self.player.coins -= 50000
                            self.world.jungle_unlocked = True
                            print(colored("You bought a ticket to the Jungle and unlocked it!", "green"))
                        elif not self.world.jungle_unlocked:
                            print(colored("You need to unlock the Jungle first!", "red"))
                            return
                        print(colored("Entering the jungle...", "green"))
                        while self.world.jungle_unlocked:
                            enemy_list = ["Snake", "Tiger"]
                            random_enemy = random.choice(enemy_list)
                            coins_gained = self.initiate_battle(random_enemy, random.randint(500, 1000))
                            self.player.coins += coins_gained
                            user_input = input(colored("Write 'E' to stop fighting: ", "cyan"))
                            if user_input.lower() == "e":
                                break

                    elif world_choice == "4":
                        if not self.world.desert_unlocked and self.player.coins >= 250000:
                            self.player.coins -= 250000
                            self.world.desert_unlocked = True
                            print(colored("You bought a ticket to the Desert and unlocked it!", "green"))
                        elif not self.world.desert_unlocked:
                            print(colored("You need to unlock the Desert first!", "red"))
                            return
                        print(colored("Entering the desert...", "green"))
                        while self.world.desert_unlocked:
                            enemy_list = ["Scorpion", "Mummy"]
                            random_enemy = random.choice(enemy_list)
                            coins_gained = self.initiate_battle(random_enemy, random.randint(1200, 1600))
                            self.player.coins += coins_gained
                            user_input = input(colored("Write 'E' to stop fighting: ", "cyan"))
                            if user_input.lower() == "e":
                                break

                    elif world_choice == "5":
                        if not self.world.void_unlocked and self.player.coins >= 1000000:
                            self.player.coins -= 1000000
                            self.world.void_unlocked = True
                            print(colored("You bought a ticket to the Void and unlocked it!", "green"))
                        elif not self.world.void_unlocked:
                            print(colored("You need to unlock the Void first!", "red"))
                            return
                        print(colored("Entering the void...", "green"))
                        while self.world.void_unlocked:
                            enemy_list = ["Void Beast", "Shadow Entity"]
                            random_enemy = random.choice(enemy_list)
                            coins_gained = self.initiate_battle(random_enemy, random.randint(2000, 5000))
                            self.player.coins += coins_gained
                            user_input = input(colored("Write 'E' to stop fighting: ", "cyan"))
                            if user_input.lower() == "e":
                                break              
                else:
                    print(colored("You can't fight without a sword, buy one at the shop.", "red"))

            elif choice == "4":
                print(colored("Leaving...", "cyan"))
                time.sleep(0.5)
                self.running = False

        print(colored("Goodbye! Thanks for playing Untitled Farming Game.", "blue"))

# Data Definitions
NEW_SWORDS = {
    "Wooden Sword": {"price": 15000, "stock": 1, "damage": 75},
    "Legendary Sword": {"price": 100000, "stock": 1, "damage": 350},
    "Excalibur": {"price": 500000, "stock": 1, "damage": 1000}
}

POWER_UPS = {
    "Gold Chain": {"price": 500000, "stock": 1, "multiplier": 5},
    "Golden Statue": {"price": 10000000, "stock": 1, "activate_godpass": True},
    "X2Pass": {"price": 150, "stock": 10}  
}

ARMOR = {
    "Leather Armor": {"price": 20000, "stock": 1, "hp": 2000},
    "Iron Armor": {"price": 100000, "stock": 1, "hp": 5000},
    "Dragon Scale Armor": {"price": 500000, "stock": 1, "hp": 15000}
}

ENEMY_LIST = {
    "Goblin": {"min_damage": 5, "max_damage": 16},
    "Bat": {"min_damage": 150, "max_damage": 250},
    "Snake": {"min_damage": 200, "max_damage": 350},
    "Scorpion": {"min_damage": 250, "max_damage": 450},
    "Void Beast": {"min_damage": 300, "max_damage": 600},
    "Romagna": {"min_damage": 15, "max_damage": 25},
    "Golem": {"min_damage": 200, "max_damage": 350},
    "Tiger": {"min_damage": 200, "max_damage": 400},
    "Mummy": {"min_damage": 400, "max_damage": 600},
    "Shadow Entity": {"min_damage": 450, "max_damage": 900}
}

WORLD_ITEMS = {
    "Forest": {
        "items": {
            "Rock": 1,
            "Gem": 5,
            "Silver coins": 6,
            "Gold coins": 8,
            "Pearl": 10,
            "Diamond": 20,
            "Ancient relic": 50
        },
        "weights": (40, 15, 10, 8, 5, 3, 2)
    },
    "Cave": {
        "items": {
            "Crystal": 7,
            "Glowing mushroom": 3,
            "Artifact": 15,
            "Rare mineral": 30,
            "Fossil": 50
        },
        "weights": (30, 15, 10, 8, 6)
    },
    "Jungle": {
        "items": {
            "Rare Orchid": 5,
            "Dragon Fruit": 9,
            "Jaguar Leaf": 12,
            "Elephant Ivory": 15,
            "Ara Plumage": 23,
            "Ancient Tribal Mask": 35,
            "Jungle Emerald": 50
        },
        "weights": (40, 15, 10, 8, 5, 3, 2)
    },
 "Desert": {
        "items": {
            "Cactus Flower": 8,
            "Sandstone Carving": 14,
            "Mirage Crystal": 19,
            "Scarab Beetle": 24,
            "Sunset Agate": 38,
            "Nomad Turban": 57,
            "Sands of Time": 83
        },
        "weights": (40, 15, 10, 8, 5, 3, 2)
    },
    "Void": {
        "items": {
            "Cosmic Dust": 75,
            "Nebula Shard": 90,
            "Black Hole Orb": 110,
            "Celestial Echo": 125,
            "Galactic Nova": 135,
            "Astral Beacon": 150,
            "Stellar Mirage": 300
        },
        "weights": (40, 20, 15, 10, 6, 5, 1)
    }
}

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
