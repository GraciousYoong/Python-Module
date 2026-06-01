class Plant:
    def __init__(self, name, height, plant_age):
        self._name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = height

        if plant_age < 0:
            print(f"{name}: Error, age can't be negative")
            self._plant_age = 0
        else:
            self._plant_age = plant_age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._plant_age

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(new_height, 1)
            print(f"Height updated: {self._height}cm")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._plant_age = new_age
            print(f"Age updated: {self._plant_age} days")

    def show(self):
        print(f"{self._name}: {self._height}cm, {self._plant_age} days old")


def main():
    print("=== ft_garden_security.py ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()
    print("\n")
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-10)
    rose.set_age(-5)
    print("\n")
    print("Current state:", end=" ")
    rose.show()
 

if __name__ == "__main__":
    main()