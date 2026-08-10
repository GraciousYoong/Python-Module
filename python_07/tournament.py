from ex0 import (
    FlameFactory,
    AquaFactory,
    CreatureFactory,
)

from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)

from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]

            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()

            print("\n* Battle *")
            print(creature_a.describe())
            print("vs.")
            print(creature_b.describe())
            print("now fight!")

            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except ValueError as error:
                print(f"Battle error, aborting tournament: {error}")
                return


def main() -> None:
    # Create factories
    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transforming = TransformCreatureFactory()

    # Create strategies
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    # Tournament 0
    print("Tournament 0 (basic)")
    print("[(Flame+Normal), (Healing+Defensive)]")

    opponents = [
        (flame, normal),
        (healing, defensive),
    ]

    battle(opponents)

    # Tournament 1
    print("\nTournament 1 (error)")
    print("[(Flame+Aggressive), (Healing+Defensive)]")

    opponents = [
        (flame, aggressive),
        (healing, defensive),
    ]

    battle(opponents)

    # Tournament 2
    print("\nTournament 2 (multiple)")
    print(
        "[(Aqua+Normal), "
        "(Healing+Defensive), "
        "(Transform+Aggressive)]"
    )

    opponents = [
        (aqua, normal),
        (healing, defensive),
        (transforming, aggressive),
    ]

    battle(opponents)


if __name__ == "__main__":
    main()
