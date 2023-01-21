class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Cube ({self.x},{self.y},{self.z})"

    def __eq__(self, other):
        if isinstance(other, Cube):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def add_x(self, delta):
        return self.add(delta, 0, 0)

    def add_y(self, delta):
        return self.add(0, delta, 0)
        
    def add_z(self, delta):
        return self.add(0, 0, delta)

    def add(self, delta_x, delta_y, delta_z):
        return Cube(self.x + delta_x, self.y + delta_y, self.z + delta_z)

    def neighbors(self):
        return [self.add_x(1), 
                self.add_x(-1), 
                self.add_y(1), 
                self.add_y(-1), 
                self.add_z(1), 
                self.add_z(-1)]

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
    for c in cubes:
        neighbors = c.neighbors()
        intersection = [value for value in neighbors if value in cubes]
        surface += 6 - len(intersection)
        print(i)
        i += 1
        
    return surface

cubes = []

with open('Input.txt') as f:
    for line in f:
        cube = read_cube(line)
        cubes.append(cube)

print(f"Surface: {calc_cubes_surface()}")



        
