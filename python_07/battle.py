from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")

    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(
    flame_factory: FlameFactory,
    aqua_factory: AquaFactory,
) -> None:
    print("Testing battle")

    flame = flame_factory.create_base()
    aqua = aqua_factory.create_base()

    print(flame.describe())
    print("vs.")
    print(aqua.describe())
    print("fight!")
    print(flame.attack())
    print(aqua.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    print("\n")
    test_factory(aqua_factory)
    print("\n")
    test_battle(flame_factory, aqua_factory)
    print("\n")


if __name__ == "__main__":
    main()
