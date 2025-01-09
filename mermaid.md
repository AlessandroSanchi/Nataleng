classDiagram
2    class Player {
3        +armor_equipped: str
4        +money: int
5        +coins: int
6        +bonus_multiplier: int
7        +godpass: bool
8        +sword_equipped: str
9        +player_hp: int
10        +player_damage: int
11        +inventory: list
12        +format_price(price: int): str
13        +equip_sword(sword_name: str): void
14        +equip_armor(armor_name: str): void
15        +add_to_inventory(item: str): void
16        +show_inventory(): void
17    }
18
19    class Worlds {
20        +cave_unlocked: bool
21        +jungle_unlocked: bool
22        +desert_unlocked: bool
23        +void_unlocked: bool
24        +explore(world_name: str, player: Player): void
25    }
26
27    class Game {
28        +player: Player
29        +world: Worlds
30        +running: bool
31        +input_page(): void
32        +save_game(filename: str): void
33        +load_game(filename: str): void
34        +shop(): void
35        +initiate_battle(enemy_name: str, enemy_hp: int): int
36        +run(): void
37        +NEW_SWORDS: dict
38        +POWER_UPS: dict
39        +ARMOR: dict
40        +ENEMY_LIST: dict
41        +WORLD_ITEMS: dict
42    }
43
44    Player --> Game : uses
45    Game --> Worlds : manages
46    Game --> Player : contains
