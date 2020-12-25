import numpy as np


def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    def calc(first, second):
        data = np.zeros(36, dtype=int)
        for idx, (f, s) in enumerate(zip(first, second)):
            if f == 'X':
                data[idx] = int(s)
            else:
                data[idx] = int(f)

        data = [str(elm) for elm in data]
        return int(''.join(data), 2)

    current_mask = ""
    mem_dict = {}
    for line in lines:
        line = line[:-1]
        if line[:4] == 'mask':
            current_mask = line[-36:]
            continue
        else:
            mem_index = int(line.split(' ')[0][4:-1])
            operation_value = int(line.split(' ')[-1])
            result = calc(current_mask, f'{operation_value:036b}')
            mem_dict[mem_index] = result

    print(mem_dict)
    total = 0
    for k, v in mem_dict.items():
        total += v

    print(total)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    def calc(first, second):
        data = np.zeros(36, dtype=int)
        fi = []
        for idx, (f, s) in enumerate(zip(first, second)):
            if f == '0':
                data[idx] = int(s)
            elif f == '1':
                data[idx] = 1
            else:  # == x
                data[idx] = 0
                fi.append(idx)

        return [str(elm) for elm in data], fi

    def recursive_set_value(m_dict, binary_address, fi, set_index, assign_value):
        if set_index == len(fi)-1:
            binary_address[fi[set_index]] = '0'
            m_dict[int(''.join(binary_address), 2)] = assign_value
            binary_address[fi[set_index]] = '1'
            m_dict[int(''.join(binary_address), 2)] = assign_value
            return

        binary_address[fi[set_index]] = '0'
        m_dict[int(''.join(binary_address), 2)] = assign_value
        recursive_set_value(m_dict, binary_address, fi, set_index + 1, assign_value)
        binary_address[fi[set_index]] = '1'
        m_dict[int(''.join(binary_address), 2)] = assign_value
        recursive_set_value(m_dict, binary_address, fi, set_index + 1, assign_value)

    current_mask = ""
    mem_dict = {}
    total = 0
    for line in lines:
        line = line[:-1]
        if line[:4] == 'mask':
            current_mask = line[-36:]
            continue
        else:
            mem_index = int(line.split(' ')[0][4:-1])
            operation_value = int(line.split(' ')[-1])
            result, float_indexes = calc(current_mask, f'{mem_index:036b}')
            recursive_set_value(mem_dict, result, float_indexes, 0, operation_value)

    for k, v in mem_dict.items():
        total += v
    print(total)


if __name__ == '__main__':
    # p1()
    p2()
