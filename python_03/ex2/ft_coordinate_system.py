#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )

        parts = coords.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0].strip())
            y = float(parts[1].strip())
            z = float(parts[2].strip())
        except ValueError as error:
            invalid = ""

            for part in parts:
                try:
                    float(part.strip())
                except ValueError:
                    invalid = part.strip()
                    break

            print(
                f"Error on parameter '{invalid}': "
                f"{error}"
            )
            continue

        return (x, y, z)


print("=== Game Coordinate System ===")

print("Get a first set of coordinates")
first_pos = get_player_pos()

print(f"Got a first tuple: {first_pos}")
print(
    f"It includes: X={first_pos[0]}, "
    f"Y={first_pos[1]}, "
    f"Z={first_pos[2]}"
)

distance_to_center = math.sqrt(
    first_pos[0] ** 2
    + first_pos[1] ** 2
    + first_pos[2] ** 2
)

print(f"Distance to center: {round(distance_to_center, 4)}")

print("Get a second set of coordinates")
second_pos = get_player_pos()

distance_between = math.sqrt(
    (second_pos[0] - first_pos[0]) ** 2
    + (second_pos[1] - first_pos[1]) ** 2
    + (second_pos[2] - first_pos[2]) ** 2
)

print(
    "Distance between the 2 sets of coordinates: "
    f"{round(distance_between, 4)}"
)
