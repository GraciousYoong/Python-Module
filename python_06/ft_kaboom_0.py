import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")

    print(
        "Testing light spell:",
        alchemy.grimoire.light_spell_record(
            "Fantasy",
            "Earth, wind and fire",
        ),
    )
    print("\n")


if __name__ == "__main__":
    main()
