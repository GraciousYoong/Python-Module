#!/usr/bin/env python3

from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
)


def test_healing_factory() -> None:
    print("Testing Creature with healing capability")

    factory = HealingCreatureFactory()

    print("base:")
    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())

    print("evolved:")
    creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(creature.heal())


def test_transform_factory() -> None:
    print("Testing Creature with transform capability")

    factory = TransformCreatureFactory()

    print("base:")
    creature = factory.create_base()
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())

    print("evolved:")
    creature = factory.create_evolved()
    print(creature.describe())
    print(creature.attack())
    print(creature.transform())
    print(creature.attack())
    print(creature.revert())


def main() -> None:
    test_healing_factory()
    print("\n")
    test_transform_factory()
    print("\n")


if __name__ == "__main__":
    main()