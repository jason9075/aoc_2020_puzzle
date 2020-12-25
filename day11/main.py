import numpy as np


def p1():
    rows = 98
    columns = 98

    seats = np.zeros([rows + 2, columns + 2], dtype=bool)
    status = np.zeros([rows + 2, columns + 2], dtype=bool)

    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    for r, line in enumerate(lines):
        for c, pos in enumerate(line):
            seats[r + 1, c + 1] = True if pos == 'L' else False  # floor = 0, is seat=1
            status[r + 1, c + 1] = False if pos == 'L' else True  # empty = 0, occupied=1

    # print(seats)
    # print(status)

    # update once
    times = 0
    while True:
        new_status = np.zeros([rows + 2, columns + 2], dtype=bool)
        for r in range(1, seats.shape[0] - 1):
            for c in range(1, seats.shape[1] - 1):
                if not seats[r, c]:
                    continue  # not seat, just ignore it.
                check_indexes = [[r - 1, c - 1], [r - 1, c], [r - 1, c + 1],
                                 [r, c - 1], [r, c + 1],
                                 [r + 1, c - 1], [r + 1, c], [r + 1, c + 1]]
                occupied_adjacent = 0
                occupied_map = np.logical_and(seats, status)
                for check_index in check_indexes:
                    if occupied_map[check_index[0], check_index[1]]:
                        occupied_adjacent += 1
                if status[r, c]:  # is occupied
                    new_status[
                        r, c] = False if 4 <= occupied_adjacent else True  # four or more seats adjacent to it are also occupied, the seat becomes empty.
                else:  # is empty
                    new_status[
                        r, c] = True if 0 == occupied_adjacent else False  # no occupied seats adjacent to it, the seat becomes occupied.
        times += 1
        if np.array_equal(status, new_status):
            break
        else:
            status = new_status

    print(new_status)
    occupied_map = np.logical_and(seats, status)
    print(np.sum(occupied_map))


def p2():
    rows = 98
    columns = 98

    seats = np.zeros([rows + 2, columns + 2], dtype=bool)
    status = np.zeros([rows + 2, columns + 2], dtype=bool)

    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    for r, line in enumerate(lines):
        for c, pos in enumerate(line):
            seats[r + 1, c + 1] = True if pos == 'L' else False  # floor = 0, is seat=1
            status[r + 1, c + 1] = False if pos == 'L' else True  # empty = 0, occupied=1

    # print(seats)
    # print(status)

    def calc_occupied(r, c, occ_map, seat_map):
        occupied_adjacent = 0

        # top left
        for d in range(1, min(r, c)):
            if occ_map[r - d, c - d]:
                occupied_adjacent += 1
                break
            if seat_map[r - d, c - d]:
                break  # empty seat
        # top
        for d in range(1, r):
            if occ_map[r - d, c]:
                occupied_adjacent += 1
                break
            if seat_map[r - d, c]:
                break  # empty seat
        # top right
        for d in range(1, min(r, columns-c+1)):
            if occ_map[r - d, c+d]:
                occupied_adjacent += 1
                break
            if seat_map[r - d, c+d]:
                break  # empty seat
        # left
        for d in range(1, c):
            if occ_map[r, c-d]:
                occupied_adjacent += 1
                break
            if seat_map[r, c-d]:
                break  # empty seat
        # right
        for d in range(1, columns-c+1):
            if occ_map[r, c+d]:
                occupied_adjacent += 1
                break
            if seat_map[r, c+d]:
                break  # empty seat
        # bottom left
        for d in range(1, min(rows-r+1, c)):
            if occ_map[r+d, c-d]:
                occupied_adjacent += 1
                break
            if seat_map[r+d, c-d]:
                break  # empty seat
        # bottom
        for d in range(1, rows-r+1):
            if occ_map[r+d, c]:
                occupied_adjacent += 1
                break
            if seat_map[r+d, c]:
                break  # empty seat
        # bottom right
        for d in range(1, min(rows-r+1, columns-c+1)):
            if occ_map[r+d, c+d]:
                occupied_adjacent += 1
                break
            if seat_map[r+d, c+d]:
                break  # empty seat

        return occupied_adjacent

    # update once
    times = 0
    while True:
        new_status = np.zeros([rows + 2, columns + 2], dtype=bool)
        for r in range(1, seats.shape[0] - 1):
            for c in range(1, seats.shape[1] - 1):
                if not seats[r, c]:
                    continue  # not seat, just ignore it.
                occupied_map = np.logical_and(seats, status)
                occupied_adjacent = calc_occupied(r,c,occupied_map, seats)

                if status[r, c]:  # is occupied
                    new_status[
                        r, c] = False if 5 <= occupied_adjacent else True  # four or more seats adjacent to it are also occupied, the seat becomes empty.
                else:  # is empty
                    new_status[
                        r, c] = True if 0 == occupied_adjacent else False  # no occupied seats adjacent to it, the seat becomes occupied.
        times += 1

        if np.array_equal(status, new_status):
            break
        else:
            status = new_status

    print(new_status)
    occupied_map = np.logical_and(seats, status)
    print(np.sum(occupied_map))


if __name__ == '__main__':
    # p1()
    p2()
