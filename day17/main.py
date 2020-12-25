import numpy as np


def p1():
    lines = []
    cycles = 6
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()

    length = len(lines)

    cube_length = length + 2 + cycles * 2
    cube_length_half = int(np.floor(cube_length / 2))

    cube = np.zeros([cube_length, cube_length, cube_length])
    start_idx = int(-np.floor(length / 2))

    delta = 1 if start_idx % 2 == 1 else 0
    for x in range(start_idx, -start_idx + delta):
        for y in range(start_idx, -start_idx + delta):
            cube[cube_length_half + x, cube_length_half + y, cube_length_half + 1] = 1 if lines[x + abs(start_idx)][
                                                                                              y + abs(
                                                                                                  start_idx)] == '#' else 0

    def calc_neighbors(cube, x, y, z):  # x,y,z = 1~15
        a = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    a += cube[i, j, k]

        return a - cube[x, y, z]

    for cycle in range(cycles):
        new_status = np.zeros(cube.shape)
        for x in range(1, cube_length - 1):
            for y in range(1, cube_length - 1):
                for z in range(1, cube_length - 1):
                    status = cube[x, y, z]
                    neighbors = calc_neighbors(cube, x, y, z)
                    if status == 1:  # active
                        if neighbors == 2 or neighbors == 3:
                            new_status[x, y, z] = 1
                    else:  # inactive
                        if neighbors == 3:
                            new_status[x, y, z] = 1

        cube = new_status

    print(np.sum(cube))


def p2():
    lines = []
    cycles = 6
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()

    length = len(lines)

    cube_length = length + 2 + cycles * 2
    cube_length_half = int(np.floor(cube_length / 2))

    cube = np.zeros([cube_length, cube_length, cube_length, cube_length])
    start_idx = int(-np.floor(length / 2))

    delta = 1 if start_idx % 2 == 1 else 0
    for x in range(start_idx, -start_idx + delta):
        for y in range(start_idx, -start_idx + delta):
            cube[cube_length_half + x, cube_length_half + y, cube_length_half + 1, cube_length_half + 1] = 1 if lines[x + abs(start_idx)][
                                                                                              y + abs(
                                                                                                  start_idx)] == '#' else 0

    def calc_neighbors(cube, x, y, z, w):  # x,y,z = 1~15
        a = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    for l in range(w - 1, w + 2):
                        a += cube[i, j, k, l]

        return a - cube[x, y, z, w]

    for cycle in range(cycles):
        new_status = np.zeros(cube.shape)
        for x in range(1, cube_length - 1):
            for y in range(1, cube_length - 1):
                for z in range(1, cube_length - 1):
                    for w in range(1, cube_length - 1):
                        status = cube[x, y, z, w]
                        neighbors = calc_neighbors(cube, x, y, z, w)
                        if status == 1:  # active
                            if neighbors == 2 or neighbors == 3:
                                new_status[x, y, z, w] = 1
                        else:  # inactive
                            if neighbors == 3:
                                new_status[x, y, z, w] = 1

        cube = new_status

    print(np.sum(cube))


if __name__ == '__main__':
    # p1()
    p2()
