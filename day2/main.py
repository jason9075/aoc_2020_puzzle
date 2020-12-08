def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    available_count = 0
    for line in lines:
        num_range, char, passwd = line.split(" ")
        low_bound, high_bound = num_range.split("-")
        char = char[0]

        count = 0
        for alpha in passwd:
            if alpha == char:
                count += 1

        if int(low_bound) <= count <= int(high_bound):
            available_count += 1

    print(available_count)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    available_count = 0
    for line in lines:
        num_range, char, passwd = line.split(" ")
        pos1, pos2 = num_range.split("-")
        char = char[0]

        is_pos1_valid = passwd[int(pos1)-1] == char
        is_pos2_valid = passwd[int(pos2)-1] == char

        if is_pos1_valid != is_pos2_valid:
            available_count += 1

    print(available_count)


if __name__ == '__main__':
    # p1()
    p2()
