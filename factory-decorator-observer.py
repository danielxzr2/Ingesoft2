# ------------------------------------------------
# BEHAVIORAL: Observer
# Objects that want to react to enemy death
# ------------------------------------------------
class ScoreSystem:
    def on_enemy_died(self, enemy):
        print(f"  [Score]  +{enemy.hp} points!")

class QuestSystem:
    def on_enemy_died(self, enemy):
        print(f"  [Quest]  '{enemy.name}' kill registered.")

class LootSystem:
    def on_enemy_died(self, enemy):
        print(f"  [Loot]   Dropped some gold! 💰")


# ------------------------------------------------
# BASE ENEMY — notifies observers when it dies
# ------------------------------------------------
class Enemy:
    def __init__(self, name, hp):
        self.name      = name
        self.hp        = hp
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage! (HP: {self.hp})")
        if self.hp <= 0:
            print(f"{self.name} has died! 💀")
            for obs in self._observers:
                obs.on_enemy_died(self)

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
# ------------------------------------------------
class EnemyDecorator:
    def __init__(self, enemy):
        self._enemy = enemy

    # Forward everything to the wrapped enemy
    def __getattr__(self, name):
        return getattr(self._enemy, name)

    def describe(self):
        self._enemy.describe()


class Shielded(EnemyDecorator):
    def take_damage(self, amount):
        self._enemy.take_damage(amount // 2)  # half damage

    def describe(self):
        self._enemy.describe()
        print("  + Shield: takes half damage 🛡️")


class Enraged(EnemyDecorator):
    def take_damage(self, amount):
        self._enemy.take_damage(amount * 2)   # double damage

    def describe(self):
        self._enemy.describe()
        print("  + Enraged: takes double damage 😡")


# ------------------------------------------------
# Demo
# ------------------------------------------------
score  = ScoreSystem()
quests = QuestSystem()
loot   = LootSystem()

# -- Plain goblin --
goblin = spawn_enemy("goblin")
goblin.add_observer(score)
goblin.add_observer(quests)

print("=== Goblin ===")
goblin.describe()
goblin.take_damage(35)

print()

# -- Shielded orc --
orc = Shielded(spawn_enemy("orc"))
orc.add_observer(score)
orc.add_observer(loot)

print("=== Shielded Orc ===")
orc.describe()
orc.take_damage(50)  # only 25 gets through
orc.take_damage(120) # only 60 gets through → dies
