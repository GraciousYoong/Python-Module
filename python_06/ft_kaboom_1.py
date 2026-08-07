def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record

        print(
            dark_spell_record(
                "Dark Fantasy",
                "bats, frogs",
            )
        )
    except ImportError as error:
        print("\n💥 BOOM! The laboratory exploded!")
        print(error)
        print("\n")


if __name__ == "__main__":
    main()
