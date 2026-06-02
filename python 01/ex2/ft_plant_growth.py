#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str,
                 height: float,
                 plant_age: int) -> None:
        self.name = name
        self.height = height
        self.plant_age = plant_age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, {self.plant_age} days old")

    def grow(self, growth_rate: float) -> None:
        self.height = round(self.height + growth_rate, 1)

    def age(self) -> None:
        self.plant_age += 1


def main() -> None:
    rose = Plant("Rose", 25.0, 30)
    initial_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age()
        rose.show()
        day += 1
    growth_height = round((rose.height - initial_height), 1)
    print(f"Growth this week: {growth_height}cm")


if __name__ == "__main__":
    main()
