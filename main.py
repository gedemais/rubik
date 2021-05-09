import numpy as np


class   Cube():
    """ Abstraction of a Rubik's cube """
    def __init__(self):
        # Sides and colors identifiers
        sides_names = ["F", "R", "U", "B", "L", "D"]
        sides_colors = ["B", "R", "Y", "G", "O", "W"]

        # Creation of a faces matrix for each side of the cube
        self.sides = {}
        for i, name in enumerate(sides_names):
            c = sides_colors[i]
            self.sides[name] = {
                                'matrix': np.ndarray((3, 3), dtype=list),
                                'links': []
                               }
            # Fills a faces matrix with an unit color (assuming that we generate a solved cube)
            self.sides[name].fill(c)

        # Linking matrices parts together to replicate the mecanical operations of a Rubik's Cube
        self.sides["F"]["links"] = [("U", "D"), ("L", "R"), ("R", "L"), ("D", "U")]
        self.sides["R"]["links"] = [("U", "R"), ("F", "R"), ("B", "R"), ("D", "R")]
        self.sides["U"]["links"] = [("L", "U"), ("R", "U"), ("F", "U"), ("B", "U")]
        self.sides["B"]["links"] = [("U", "U"), ("R", "R"), ("L", "L"), ("D", "D")]
        self.sides["L"]["links"] = [("U", "L"), ("F", "L"), ("D", "L"), ("B", "L")]
        self.sides["D"]["links"] = [("F", "D"), ("L", "D"), ("R", "D"), ("B", "D")]

    def move(self, side):
        # Clockwise "classic" move
        self.sides[side]["matrix"] = np.moveaxis(self.sides[side], -1, 0)
        self.sides[side]["matrix"] = np.flip(self.sides[side], 1)

        first_side = self.sides[side]["links"][0][0]
        first_line = self.sides[side]["links"][0][1]
        # Swap shit

    def prim_move(self, side):
        # Anti-clockwise move
        self.sides[side]["matrix"] = np.moveaxis(self.sides[side], -1, 0)
        self.sides[side]["matrix"] = np.flip(self.sides[side], 0)


def main():
    cube = Cube()
    print(cube.sides)


if __name__ == "__main__":
    main()
