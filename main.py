import numpy as np

class   Cube():
    def __init__(self):
        sides_names = ["F", "R", "U", "B", "L", "D"]
        sides_colors = ["B", "R", "Y", "G", "O", "W"]
        self.sides = {}
        for i, name in enumerate(sides_names):
            c = sides_colors[i]
            self.sides[name] = np.random.rand(3, 3)
            #self.sides[name] = np.ndarray((3, 3), dtype=list)
            #self.sides[name].fill(c)
            print(name)
            print(self.sides[name])
            print("----------------------------")
            #self.sides[name] = np.moveaxis(self.sides[name], -1, 0)
            #self.sides[name] = np.flip(self.sides[name], 0)

            self.sides[name] = np.moveaxis(self.sides[name], -1, 0)
            self.sides[name] = np.flip(self.sides[name], 1)
            print(name)
            print(self.sides[name])
            print("----------------------------")


def main():
    cube = Cube()


if __name__ == "__main__":
    main()
