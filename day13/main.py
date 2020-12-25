import numpy as np


def p1():
    with open('input.txt') as fp:
        my_depart = int(fp.readline())
        bus_info = fp.readline()

    earliest_bus_depart = my_depart
    wait_time = 0
    bus_id = 0
    find_bus = False
    while not find_bus:

        for bus_depart in bus_info.split(","):
            if bus_depart == 'x':
                continue

            if earliest_bus_depart % int(bus_depart) != 0:
                continue

            bus_id = int(bus_depart)
            wait_time = earliest_bus_depart - my_depart
            find_bus = True
            break

        if not find_bus:
            earliest_bus_depart += 1

    print(bus_id)
    print(earliest_bus_depart)
    print(wait_time)
    print((earliest_bus_depart - my_depart) * bus_id)


def p2():
    with open('input_test.txt') as fp:
        my_depart = int(fp.readline())
        bus_info = fp.readline()

    info_dict = {}
    for idx, bus_depart in enumerate(bus_info.split(",")):
        if bus_depart == 'x':
            continue
        info_dict[int(bus_depart)] = idx

    print(info_dict)
    counter = 0
    capacity = 5000
    data = np.zeros([capacity, len(info_dict)])
    for idx, (k, v) in enumerate(info_dict.items()):
        start = 0
        while True:
            if capacity - 1 < start + v:
                break
            data[start + v, idx] = 1
            start += k
    print(data[:50, :])


if __name__ == '__main__':
    # p1()
    p2()
