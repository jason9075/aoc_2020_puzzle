import math

import numpy as np


def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    loc_x, loc_y = 0, 0
    face = 'E'
    dir_set = {'N', 'S', 'E', 'W'}

    def forward(x, y, direction, steps):
        if direction == 'N':
            y -= steps
        elif direction == 'S':
            y += steps
        elif direction == 'E':
            x += steps
        elif direction == 'W':
            x -= steps

        return x, y

    def turn(ship_direction, turn_direction, degree):
        # N:0, E:1, S:2, W:3
        degree /= 90
        if turn_direction == 'L':
            degree = -degree

        if ship_direction == 'N':
            ship_direction = 0
        elif ship_direction == 'E':
            ship_direction = 1
        elif ship_direction == 'S':
            ship_direction = 2
        elif ship_direction == 'W':
            ship_direction = 3
        else:
            print('wrong input')
            exit(1)

        ship_direction += degree
        ship_direction %= 4

        if ship_direction == 0:
            ship_direction = 'N'
        elif ship_direction == 1:
            ship_direction = 'E'
        elif ship_direction == 2:
            ship_direction = 'S'
        elif ship_direction == 3:
            ship_direction = 'W'
        else:
            print('wrong input')
            exit(1)

        return ship_direction

    for line in lines:
        line = line[:-1]

        command, value = line[0], int(line[1:])
        if command in dir_set:
            loc_x, loc_y = forward(loc_x, loc_y, command, value)
        elif command == 'F':
            loc_x, loc_y = forward(loc_x, loc_y, face, value)
        else:
            face = turn(face, command, value)

    print(loc_x, loc_y)
    print(abs(loc_x) + abs(loc_y))


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1
    dir_set = {'N', 'S', 'E', 'W'}

    def mv_waypoint(w_x, w_y, direction, steps):
        if direction == 'N':
            w_y += steps
        elif direction == 'S':
            w_y -= steps
        elif direction == 'E':
            w_x += steps
        elif direction == 'W':
            w_x -= steps

        return w_x, w_y

    def forward(s_x, s_y, w_x, w_y, steps):
        dist_x = w_x * steps
        dist_y = w_y * steps

        s_x += dist_x
        s_y += dist_y

        return s_x, s_y

    def turn(w_x, w_y, turn_direction, degree):
        # N:0, E:1, S:2, W:3
        if turn_direction == 'L':
            degree = -degree

        sin = math.sin(degree / 180 * math.pi)
        cos = math.cos(degree / 180 * math.pi)

        new_w_x = round(w_x * cos + w_y * sin)
        new_w_y = round(w_y * cos - w_x * sin)

        return new_w_x, new_w_y

    for line in lines:
        line = line[:-1]

        command, value = line[0], int(line[1:])
        if command in dir_set:
            waypoint_x, waypoint_y = mv_waypoint(waypoint_x, waypoint_y, command, value)
        elif command == 'F':
            ship_x, ship_y = forward(ship_x, ship_y, waypoint_x, waypoint_y, value)
        else:
            waypoint_x, waypoint_y = turn(waypoint_x, waypoint_y, command, value)

        # print(line)
        # print("ship:", ship_x, ship_y)
        # print("wp:", waypoint_x, waypoint_y)
    print(abs(ship_x) + abs(ship_y))


if __name__ == '__main__':
    # p1()
    p2()
