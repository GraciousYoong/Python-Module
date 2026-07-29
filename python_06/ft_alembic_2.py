import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using 'import ...' structure")
    print("Testing create_earth:", end=" ")
    print(f"{alchemy.elements.create_earth()}")
    print("\n")


if __name__ == "__main__":
    main()
