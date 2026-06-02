#!/usr/bin/env python3

class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, "
                  f"{self._age} age, {self._show} show")

    def __init__(self, name: str,
                 height: float,
                 plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age
        self.stats = Plant.Stats()

    @staticmethod
    def is_more_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls: type["Plant"]) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self.stats._show += 1
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, {self.plant_age} days old")

    def grow(self, growth_rate: float) -> None:
        self.height = round(self.height + growth_rate, 1)
        self.stats._grow += 1

    def age(self) -> None:
        self.plant_age += 1
        self.stats._age += 1


class Flower(Plant):
    def __init__(self, name: str,
                 height: float,
                 plant_age: int,
                 color: str) -> None:
        super().__init__(name, height, plant_age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if not self._bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    class Stats(Plant.Stats):
        _shade_count: int

        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(self, name: str,
                 height: float,
                 plant_age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, plant_age)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.Stats = Tree.Stats()

    def produce_shade(self) -> None:
        self.stats._shade_count += 1
        print(f"Tree {self.name.capitalize()} now produces a shade of "
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str,
                 height: float,
                 plant_age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, growth_rate: float) -> None:
        super().grow(growth_rate)
        self.nutritional_value += 1

    def age(self) -> None:
        super().age()
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str,
                 height: float,
                 plant_age: int,
                 color: str) -> None:
        super().__init__(name, height, plant_age, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old ===")
    print("Is 30 days more than a year? ->", Plant.is_more_than_a_year(30))
    print("Is 400 days more than a year? ->", Plant.is_more_than_a_year(400))

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_statistics(rose)

    print("\n[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)

    print("\n[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()
    display_statistics(oak)

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()

    print("\n[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(2.1)
        tomato.age()

    tomato.show()
    display_statistics(tomato)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()

    print("\n[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age()
    sunflower.bloom()

    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
