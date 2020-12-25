import numpy as np


def p1(file):
    jol_num = []
    with open(file) as fp:
        line = fp.readline()
        while line:
            jol_num.append(int(line))
            line = fp.readline()

    # jol_num.append(0)
    jol_num.sort()
    jol_num.reverse()

    num_of_thr = 0
    num_of_one = 0
    for idx, jol in enumerate(jol_num[:-1]):
        diff = jol - jol_num[idx + 1]
        if diff == 3:
            num_of_thr += 1
        elif diff == 1:
            num_of_one += 1
        else:
            print(f"strange diff: {diff}")

    num_of_thr += 1  # final +3

    return num_of_thr, num_of_one, jol_num


def p2_wrong():
    num_of_thr, num_of_one, jol_num = p1('input_test.txt')
    print(jol_num)
    print(num_of_thr)
    print(num_of_one)
    print(jol_num[0] + 3)

    high = jol_num[0] + 3

    jol_set = set(jol_num)

    remain = high
    sol_set = set()  # 警告：把完整path存進set裡會超級佔用空間，此set僅供debug使用
    sol_list = []

    def find_path(path, s, r, usage_thr, usage_one):

        if 1 <= usage_thr or 3 <= usage_one:
            next_value = r - 3
            if next_value in jol_set:
                if next_value == 0:
                    # s.add(f'{path}-0')
                    sol_list.append(1)
                if 1 <= usage_thr:
                    find_path(f'{path}-{next_value}', s, next_value, usage_thr - 1, usage_one)
                else:
                    find_path(f'{path}-{next_value}', s, next_value, usage_thr, usage_one - 3)

        if 2 <= usage_one:
            next_value = r - 2
            if next_value in jol_set:
                if next_value == 0:
                    # s.add(f'{path}-0')
                    sol_list.append(1)
                find_path(f'{path}-{next_value}', s, next_value, usage_thr, usage_one - 2)

        if 1 <= usage_one:
            next_value = r - 1
            if next_value in jol_set:
                if next_value == 0:
                    # s.add(f'{path}-0')
                    sol_list.append(1)
                find_path(f'{path}-{next_value}', s, next_value, usage_thr, usage_one - 1)

    find_path(f"{remain}", sol_set, remain, num_of_thr, num_of_one)

    # print(f'sol_set: {sol_set}')
    print(f'sol_count: {len(sol_list)}')


def p2():
    _, _, jol_num = p1('input.txt')
    jol_num.append(0)
    print(jol_num)
    jol_num.reverse()

    # recursive
    # def decompose(num):
    #     if num not in jol_num:
    #         return 0
    #     if num == 0:
    #         return 1
    #     if num == 1:
    #         return 1
    #     if num == 2:
    #         return 2
    #     return decompose(num - 3) + decompose(num - 2) + decompose(num - 1)
    #
    # print(decompose(jol_num[-1]))


    # dp
    data = np.zeros(jol_num[-1] + 1, dtype=int)

    for i, jol in enumerate(jol_num):
        if jol == 0:
            data[jol] = 1
        elif jol == 1:
            data[jol] = 1
        elif jol == 2:
            data[jol] = 2
        elif jol == 3:
            data[jol] = 4
        else:
            data[jol] = data[jol - 1] + data[jol - 2] + data[jol - 3]

    print(f'data : {data}')
    print(f'answer : {data[-1]}')


if __name__ == '__main__':
    # num_of_thr, num_of_one, _ = p1("input.txt")
    # print(num_of_thr)
    # print(num_of_one)
    # print((num_of_thr) * num_of_one)

    # p2_wrong()
    p2()
