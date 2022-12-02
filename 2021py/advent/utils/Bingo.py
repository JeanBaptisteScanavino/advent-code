class Bingo:
    def create_bingo_grid(file):
        file.pop(0)
        file.pop(0)
        file.append("")
        grids = []
        grid = []
        for x in file:
            if x != "":
                grid.append(Bingo.make_line(x))
            else:
                grids.append(grid)
                grid = []
        return grids

    def make_line(line):
        result = []
        new_line = line.split(" ")
        for x in new_line:
            if x != " " and x != "":
                result.append(x)
        return result

    def nb_is(grids, nb):
        for grid in grids:
            for line in grid:
                for n in line:
                    n = list(map(lambda x: x.replace(nb, "X"), n))
                    print(n)
        return grids
