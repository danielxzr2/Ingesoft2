# ------------------------------------------------
# BASE ENEMY
# ------------------------------------------------
class Enemy:
    def __init__(self, name, hp):
        self.name = name
        self.hp   = hp

    def describe(self):
        print(f"{self.name} — HP: {self.hp}")


# ------------------------------------------------
# CREATIONAL: Factory
# ------------------------------------------------
def spawn_enemy(kind):
    enemies = {
        "goblin": lambda: Enemy("Goblin", 30),
        "orc":    lambda: Enemy("Orc",    80),
        "dragon": lambda: Enemy("Dragon", 200),
    }
    creator = enemies.get(kind.lower())
    if creator is None:
        raise ValueError(f"Unknown enemy: '{kind}'")
    return creator()


# ------------------------------------------------
# STRUCTURAL: Decorator
# Wraps an enemy and adds a power-up on top
# ------------------------------------------------
class EnemyDecorator:
    def __init__(self, enemy):
        self._enemy = enemy

    def describe(self):
        self._enemy.describe()


class Shielded(EnemyDecorator):
    def describe(self):
        self._enemy.describe()
        print("  + Shield: takes half damage 🛡️")


class Enraged(EnemyDecorator):
    def describe(self):
        self._enemy.describe()
        print("  + Enraged: deals double damage 😡")


class Poisoned(EnemyDecorator):
    def describe(self):
        self._enemy.describe()
        print("  + Poisoned: loses HP each turn ☠️")


# ------------------------------------------------
# Demo
# ------------------------------------------------
goblin = spawn_enemy("goblin")
goblin.describe()
print()

# Wrap the orc with a power-up
orc = Shielded(spawn_enemy("orc"))
orc.describe()
print()

# Stack multiple decorators on the dragon
dragon = Poisoned(Enraged(spawn_enemy("dragon")))
dragon.describe()
