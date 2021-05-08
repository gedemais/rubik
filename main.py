import numpy as np

class   Cube():
    def __init__(self):
        sides_names = ["Front", "Right", "Up", "Back", "Left", "Down"]
        sides_colors = ["B", "R", "Y", "G", "O", "W"]
        self.sides = {}
        for i, name in enumerate(sides_names):
            c = sides_colors[i]
            self.sides[name] = np.ndarray((3, 3), dtype=list)
            self.sides[name].fill(c)
            print(name)
            print(self.sides[name])


def main():
    cube = Cube()


if __name__ == "__main__":
    main()
