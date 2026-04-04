import alchemy.potions

if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength potions: {alchemy.potions.strength_potion()}")
    print(f"Testing healing potions: {alchemy.potions.healing_potion()}")