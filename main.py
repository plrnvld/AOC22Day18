from __future__ import annotations
from datetime import datetime
import sys


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.key = f"{x},{y},{z}"

    def __str__(self):
        return f"Cube ({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        if isinstance(other, Cube):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def add_x(self, delta) -> Cube:
        return self.add(delta, 0, 0)

    def add_y(self, delta) -> Cube:
        return self.add(0, delta, 0)

    def add_z(self, delta) -> Cube:
        return self.add(0, 0, delta)

    def add(self, delta_x, delta_y, delta_z) -> Cube:
        return Cube(self.x + delta_x, self.y + delta_y, self.z + delta_z)

    def neighbors(self):
        return [
            self.add_x(1),
            self.add_x(-1),
            self.add_y(1),
            self.add_y(-1),
            self.add_z(1),
            self.add_z(-1)
        ]


def read_cube(line) -> Cube:
    splitted_ints = [int(text) for text in line.split(",")]
    return Cube(
        splitted_ints[0],
        splitted_ints[1],
        splitted_ints[2],
    )


def calc_cubes_surface() -> int:
    surface = 0
    i = 1
    for c in cubes_dict.values():
        num_neighbors = sum(map(lambda n: n.key in cubes_dict, c.neighbors()))
        surface += 6 - num_neighbors
        i += 1

    return surface


cubes_dict = dict()

with open('Input.txt') as f:
    for line in f:
        cube = read_cube(line)
        cubes_dict[cube.key] = cube

min_x = sys.maxsize
max_x = -sys.maxsize
min_y = sys.maxsize
max_y = -sys.maxsize
min_z = sys.maxsize
max_z = -sys.maxsize

for cube in cubes_dict.values():
    min_x = min(min_x, cube.x)
    max_x = max(max_x, cube.x)
    min_y = min(min_y, cube.y)
    max_y = max(max_y, cube.y)
    min_z = min(min_z, cube.z)
    max_z = max(max_z, cube.z)

print(f"Min x:{min_x}, max x:{max_x}, min y:{min_y}, max y:{max_y}, min z:{min_z}, max z:{max_z}")

start = datetime.now()
print(f"Surface: {calc_cubes_surface()}")
finish = datetime.now()

delta = finish - start
print(f"Calculation time: {delta}")
