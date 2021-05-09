import numpy as np


class   Cube():
    """ Abstraction of a Rubik's cube """
    def __init__(self):
        # Sides and colors identifiers
        self.sides_names = ["F", "R", "U", "B", "L", "D"]
        self.sides_colors = ["B", "R", "Y", "G", "O", "W"]

        # Creation of a faces matrix for each side of the cube
        self.sides = {}
        for i, name in enumerate(self.sides_names):
            c = self.sides_colors[i]
            self.sides[name] = {
                                'matrix': np.ndarray((3, 3), dtype=list),
                                'links': []
                               }
            # Fills a faces matrix with an unit color (assuming that we generate a solved cube)
            self.sides[name]["matrix"].fill(c)

        # Linking matrices parts together to replicate the mecanical operations of a Rubik's Cube
        self.sides["F"]["links"] = [("U", "D"), ("R", "L"), ("D", "U"), ("L", "R")]
        self.sides["R"]["links"] = [("U", "R"), ("B", "R"), ("D", "R"), ("F", "R"),]
        self.sides["U"]["links"] = [("L", "U"), ("B", "U"), ("R", "U"), ("F", "U")]
        self.sides["B"]["links"] = [("U", "U"), ("R", "R"), ("D", "D"), ("L", "L")]
        self.sides["L"]["links"] = [("U", "L"), ("B", "L"), ("D", "L"), ("F", "L")]
        self.sides["D"]["links"] = [("F", "D"), ("L", "D"), ("B", "D"), ("R", "D")]

    def show(self):
        for i, side in enumerate(self.sides.keys()):
            print(self.sides_names[i])
            print(self.sides[side]["matrix"])
        print("----------------------------")

    def swap_lines(self, link_a, link_b):
        tmp = self.get_line_content(link_a).copy()
        self.write_line(link_a, self.get_line_content(link_b))
        self.write_line(link_b, tmp)

    def get_line_content(self, link):
        if link[1] == 'U':
            return self.sides[link[0]]['matrix'][0]
        elif link[1] == 'D':
            return self.sides[link[0]]['matrix'][2]
        elif link[1] == 'L':
            return [i[0] for i in self.sides[link[0]]['matrix']]
        elif link[1] == 'R':
            return [i[2] for i in self.sides[link[0]]['matrix']]

    def write_line(self, link, line):
        if link[1] == 'U':
            print('upper line ({})'.format(line))
            self.sides[link[0]]['matrix'][0] = line
        elif link[1] == 'D':
            print('bottom line')
            self.sides[link[0]]['matrix'][2] = line
        elif link[1] == 'L':
            print('left line')
            for i, dest_line in enumerate(self.sides[link[0]]['matrix']):
                dest_line[0] = line[i]
        elif link[1] == 'R':
            print('right line')
            for i, dest_line in enumerate(self.sides[link[0]]['matrix']):
                dest_line[2] = line[i]

    def move(self, side):
        # Clockwise "classic" move
        self.sides[side]["matrix"] = np.moveaxis(self.sides[side]["matrix"], -1, 0)
        self.sides[side]["matrix"] = np.flip(self.sides[side]["matrix"], 1)
        # Swap lines to step in the clockwise direction
        self.swap_lines(self.sides[side]["links"][0], self.sides[side]["links"][3])
        self.swap_lines(self.sides[side]["links"][1], self.sides[side]["links"][3])
        self.swap_lines(self.sides[side]["links"][2], self.sides[side]["links"][3])

    def prim_move(self, side):
        # Anti-clockwise move
        self.sides[side]["matrix"] = np.moveaxis(self.sides[side]["matrix"], -1, 0)
        self.sides[side]["matrix"] = np.flip(self.sides[side]["matrix"], 0)
        # Swap lines to step in the anti-clockwise direction
        self.swap_lines(self.sides[side]["links"][0], self.sides[side]["links"][3])
        self.swap_lines(self.sides[side]["links"][1], self.sides[side]["links"][3])
        self.swap_lines(self.sides[side]["links"][2], self.sides[side]["links"][3])


def main():
    cube = Cube()
    cube.move('L')
    cube.show()


if __name__ == "__main__":
    main()
