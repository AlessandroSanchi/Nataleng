```mermaid


classDiagram
    class Player {
       +armor_equipped: str
       +money: int
        +coins: int
        +bonus_multiplier: int
        +godpass: bool
        +sword_equipped: str
        +player_hp: int
        +player_damage: int
        +inventory: list
        +format_price(price: int): str
        +equip_sword(sword_name: str): void
        +equip_armor(armor_name: str): void
        +add_to_inventory(item: str): void
        +show_inventory(): void
    }

    class Worlds {
        +cave_unlocked: bool
        +jungle_unlocked: bool
        +desert_unlocked: bool23        +void_unlocked: bool
        +explore(world_name: str, player: Player): void
   }

     class Game {
        +player: Player
        +world: Worlds
        +running: bool
        +input_page(): void
        +save_game(filename: str): void
        +load_game(filename: str): void
       +shop(): void3       +initiate_battle(enemy_name: str, enemy_hp: int): int
        +run(): void
        +NEW_SWORDS: dict
        +POWER_UPS: dict
        +ARMOR: dict
        +ENEMY_LIST: dict
        +WORLD_ITEMS: dict
     }

    Player --> Game : uses
    Game --> Worlds : manages
    Game --> Player : contains
