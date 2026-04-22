#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str,
                 height: int,
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
    pass