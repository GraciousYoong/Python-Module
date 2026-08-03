from alchemy import potions


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion:", end=" ")
    print(f"{potions.strength_potion()}")
    print("Testing healing_potion:", end=" ")
    print(f"{potions.healing_potion()}")
    print("\n")


if __name__ == "__main__":
    main()
