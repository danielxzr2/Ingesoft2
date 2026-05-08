class Warrior:
    def attack(self):
        print("Warrior swings a sword! ⚔️")

class Mage:
    def attack(self):
        print("Mage casts a fireball! 🔥")

class Archer:
    def attack(self):
        print("Archer shoots an arrow! 🏹")


# --- The Factory ---

def create_character(character_type):
    characters = {
        "warrior": Warrior,
        "mage":    Mage,
        "archer":  Archer,
    }
    cls = characters.get(character_type.lower())
    if cls is None:
        raise ValueError(f"Unknown character type: '{character_type}'")
    return cls()


# --- Demo ---

for kind in ["warrior", "mage", "archer"]:
    hero = create_character(kind)
    hero.attack()
