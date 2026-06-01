#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str,
                 height: float,
                 age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, growth_rate):
        self.height = round(self.height + growth_rate, 1)

    def age_up(self):
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    starting_height = rose.height
    rose.show()
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow(0.8)
        rose.age_up()
        rose.show()
    total_growth = round(rose.height - starting_height, 1)
    print(f"Growth this week: {total_growth}cm")
