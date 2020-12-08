def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    max_id = 0
    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        row_binary, col_binary = line[:7], line[7:]
        row_binary = row_binary.replace('F', '0')
        row_binary = row_binary.replace('B', '1')
        col_binary = col_binary.replace('L', '0')
        col_binary = col_binary.replace('R', '1')
        row, col = int(row_binary, 2), int(col_binary, 2)
        seat_id = row * 8 + col
        if max_id < seat_id:
            max_id = seat_id

    print(max_id)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    total_row = 64008  # (1+2+3+...126)*8=64008
    total_col = 28  # 1+2+3+...7=28
    l = []
    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        row_binary, col_binary = line[:7], line[7:]
        row_binary = row_binary.replace('F', '0')
        row_binary = row_binary.replace('B', '1')
        col_binary = col_binary.replace('L', '0')
        col_binary = col_binary.replace('R', '1')
        row, col = int(row_binary, 2), int(col_binary, 2)

        seat_id = row * 8 + col
        l.append(seat_id)

    total_id_sum = (min(l) + max(l)) * (len(l)+1) / 2

    for seat_id in l:
        total_id_sum -= seat_id
    print(total_id_sum)


if __name__ == '__main__':
    # p1()
    p2()
