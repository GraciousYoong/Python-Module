from collections.abc import Callable


# Callable syntax: Callable[[argument_types], return_type]
Spell = Callable[[str, int], str]
Condition = Callable[[str, int], bool]


def spell_combiner(
    spell1: Spell,
    spell2: Spell,
) -> Callable[[str, int], tuple[str, str]]:
    def combined(
        target: str,
        power: int,
    ) -> tuple[str, str]:
        return (
            spell1(target, power),
            spell2(target, power),
        )

    return combined


def power_amplifier(
    base_spell: Spell,
    multiplier: int,
) -> Spell:
    def amplified(
        target: str,
        power: int,
    ) -> str:
        return base_spell(
            target,
            power * multiplier,
        )

    return amplified


def conditional_caster(
    condition: Condition,
    spell: Spell,
) -> Spell:
    def conditional(
        target: str,
        power: int,
    ) -> str:
        if condition(target, power):
            return spell(target, power)

        return "Spell fizzled"

    return conditional


def spell_sequence(
    spells: list[Spell],
) -> Callable[[str, int], list[str]]:
    def sequence(
        target: str,
        power: int,
    ) -> list[str]:
        return [
            spell(target, power)
            for spell in spells
        ]

    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heals {target} for {power} HP"


def shield(target: str, power: int) -> str:
    return f"Shields {target} for {power}"


def strong_enough(target: str, power: int) -> bool:
    return power >= 20 and target != "giant"


def main() -> None:
    print("Testing spell combiner...")

    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 10)

    print(f"Combined spell result: {result}")

    print("\nTesting power amplifier...")

    mega_fireball = power_amplifier(
        fireball,
        3,
    )

    print("Original: 10, Amplified: 30")
    print(mega_fireball("Dragon", 10))

    print("\nTesting conditional caster...")

    strong_fireball = conditional_caster(
        strong_enough,
        fireball,
    )

    print(strong_fireball("Dragon", 30))
    print(strong_fireball("Dragon", 10))

    print("\nTesting spell sequence...")

    sequence = spell_sequence(
        [fireball, heal, shield]
    )

    print(sequence("Dragon", 10))


if __name__ == "__main__":
    main()
