import numpy as np

class   Cube():
    def __init__(self):
        sides_names = ["F", "R", "U", "B", "L", "D"]
        sides_colors = ["B", "R", "Y", "G", "O", "W"]
        self.sides = {}
        for i, name in enumerate(sides_names):
            c = sides_colors[i]
            self.sides[name] = (np.ndarray((3, 3), dtype=list), [])
            self.sides[name].fill(c)

        self.sides["F"][1] = [("U", "D"), ("L", "R"), ("R", "L"), ("D", "U")]
        self.sides["R"][1] = [("U", "R"), ("F", "R"), ("B", "R"), ("D", "R")]
        self.sides["U"][1] = [("L", "U"), ("R", "U"), ("F", "U"), ("B", "U")]
        self.sides["B"][1] = [("", ""), ("", ""), ("", ""), ("", "")]
        self.sides["L"][1] = [("", ""), ("", ""), ("", ""), ("", "")]
        self.sides["D"][1] = [("", ""), ("", ""), ("", ""), ("", "")]

    def move(self, side):
        self.sides[side] = np.moveaxis(self.sides[side], -1, 0)
        self.sides[side] = np.flip(self.sides[side], 1)
    def prim_move(self, side):
        self.sides[side] = np.moveaxis(self.sides[side], -1, 0)
        self.sides[side] = np.flip(self.sides[side], 0)


def main():
    cube = Cube()
    print(cube.sides)


if __name__ == "__main__":
    main()
