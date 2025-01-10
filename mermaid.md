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
        +format_price(price: int)
        +equip_sword(sword_name: str)
        +equip_armor(armor_name: str)
        +add_to_inventory(item: str)

    }

    class Worlds {
        +cave_unlocked: bool
        +jungle_unlocked: bool
        +desert_unlocked: bool        
        +void_unlocked: bool
        +explore(world_name: str, player: Player)
   }

     class Game {
        +player: Player
        +world: Worlds
        +running: bool
        +input_page()
        +save_game(filename: str)
        +load_game(filename: str)
        +shop()       
        +initiate_battle(enemy_name: str, enemy_hp: int)
        +run()
        +ENEMY_LIST: dict
     }

    Player --> Game : 
    Game --> Worlds : manages
    Game --> Player : contains
