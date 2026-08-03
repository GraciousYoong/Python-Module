import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potion")
    print("Testing strength_potion:", end=" ")
    print(f"{alchemy.strength_potion()}")
    print("Testing heal alias:", end=" ")
    print(f"{alchemy.heal()}")
    print("\n")


if __name__ == "__main__":
    main()
