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
    oak = Plant("Oak", 200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)
    plants_list = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plants_list:
        print("Created:", end=" ")
        plant.show()


if __name__ == "__main__":
    main()
