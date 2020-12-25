import numpy as np


def p1():
    with open('input.txt') as fp:
        line = fp.readline()

    mem_map = {}
    latest_value = 0
    for idx, value in enumerate(line.split(',')):
        value = int(value)
        mem_map[value] = [idx + 1, None]
        latest_value = value

    target_round = 2020

    def update_mem(m_map, index, t):
        if index not in list(m_map.keys()):
            m_map[index] = [t, None]
            return
        m_map[index][1] = m_map[index][0]
        m_map[index][0] = t

    for turn in range(len(mem_map) + 1, target_round + 1):
        if latest_value not in list(mem_map.keys()):
            update_mem(mem_map, latest_value, turn)
            latest_value = 0
            update_mem(mem_map, 0, turn)
        elif mem_map[latest_value][1] is not None:  # (turn, turn)
            latest_value = mem_map[latest_value][0] - mem_map[latest_value][1]
            update_mem(mem_map, latest_value, turn)
        elif mem_map[latest_value][1] is None:  # (turn, none)
            latest_value = 0
            update_mem(mem_map, 0, turn)

        print(f'turn:{turn} value:{latest_value}')


def p2():
    with open('input.txt') as fp:
        line = fp.readline()

    mem_map = {}
    latest_value = 0
    for idx, value in enumerate(line.split(',')):
        value = int(value)
        mem_map[value] = [idx + 1, None]
        latest_value = value

    target_round = 30000000

    def update_mem(m_map, index, t):
        if index not in list(m_map.keys()):
            m_map[index] = [t, None]
            return
        m_map[index][1] = m_map[index][0]
        m_map[index][0] = t

    for turn in range(len(mem_map) + 1, target_round + 1):
        if latest_value not in list(mem_map.keys()):
            update_mem(mem_map, latest_value, turn)
            latest_value = 0
            update_mem(mem_map, 0, turn)
        elif mem_map[latest_value][1] is not None:  # (turn, turn)
            latest_value = mem_map[latest_value][0] - mem_map[latest_value][1]
            update_mem(mem_map, latest_value, turn)
        elif mem_map[latest_value][1] is None:  # (turn, none)
            latest_value = 0
            update_mem(mem_map, 0, turn)

        # if latest_value == 0:

    print(f'turn:{1} value:{latest_value}')


if __name__ == '__main__':
    # p1()
    p2()
