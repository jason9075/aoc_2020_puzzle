def p1(right=3, down=1):
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    tree_count = 0
    x_pos = 0

    for idx, line in enumerate(lines):
        if idx % down != 0:
            continue
        line = line[:-1]  # remove \n

        if len(line) <= x_pos:
            x_pos -= len(line)

        if line[x_pos] == '#':
            tree_count += 1

        x_pos += right

    print(tree_count)
    return tree_count


def p2():
    a1 = p1(right=1, down=1)
    a2 = p1(right=3, down=1)
    a3 = p1(right=5, down=1)
    a4 = p1(right=7, down=1)
    a5 = p1(right=1, down=2)

    print(a1*a2*a3*a4*a5)


if __name__ == '__main__':
    # _ = p1()
    p2()
