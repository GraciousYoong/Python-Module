from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using", end=" ")
    print("'from ... import ...' structure")
    print("Testing create_air:", end=" ")
    print(f"{create_air()}")
    print("\n")


if __name__ == "__main__":
    main()
