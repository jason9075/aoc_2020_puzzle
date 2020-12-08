import timeit

import numpy as np


def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    execute_history = np.zeros(len(lines))
    counter = 0
    accumulator = 0

    while True:
        command = lines[counter]
        if execute_history[counter] == 1:
            break
        execute_history[counter] = 1
        if command[0] == 'n':
            counter += 1
        elif command[0] == 'a':
            accumulator += int(command.split(" ")[-1])
            counter += 1
        elif command[0] == 'j':
            counter += int(command.split(" ")[-1])

    print(accumulator)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    success = False

    for change_line_index in range(0, len(lines) - 1):
        if success:
            break
        accumulator = 0
        counter = 0
        execute_history = np.zeros(len(lines))

        while counter <= len(lines):
            if len(lines) <= counter:
                success = True
                break
            command = lines[counter]
            if execute_history[counter] == 1:
                # fail
                break
            execute_history[counter] = 1
            if command[0] == 'n':
                if change_line_index == counter:
                    counter += int(command.split(" ")[-1])
                else:
                    counter += 1
            elif command[0] == 'a':
                accumulator += int(command.split(" ")[-1])
                counter += 1
            elif command[0] == 'j':
                if change_line_index == counter:
                    counter += 1
                else:
                    counter += int(command.split(" ")[-1])
        if success:
            # print(f'change at {change_line_index}')
            print(accumulator)


def p2_inverse_find_correct_path():
    lines = []
    with open('input_correct.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    lines.reverse()

    def recursive_restore(command_path, current_counter):
        # 到達第一行，此path是最佳解
        if len(lines) - 1 == current_counter:
            return True

        # 找有jmp到此行的所有指令
        for last_counter, last_command in enumerate(lines):
            if last_command[0] == 'j' and last_counter - int(
                    last_command.split(" ")[-1]) == current_counter and last_counter not in command_path:
                command_path.append(last_counter)
                if not recursive_restore(command_path, last_counter):
                    command_path.pop()
                else:
                    return True

        # 檢查是不是上一行執行下來的 (如果上一行是jmp 就檢查是不是+1 不然不會執行這行)
        if current_counter + 1 not in command_path:
            if lines[current_counter + 1][0] == 'j' and int(lines[current_counter + 1].split(" ")[-1]) != 1:
                return False

            command_path.append(current_counter + 1)
            if not recursive_restore(command_path, current_counter + 1):
                command_path.pop()
            else:
                return True

        # 死路 去除這個counter
        return False

    path = [0]
    result = recursive_restore(path, 0)
    print(path)

    comm = []

    his = []
    accumulator = 0
    for elem in path:
        his.append(627 - elem)
        comm.append(lines[elem])
        if lines[elem][0] == 'a':
            accumulator += int(lines[elem].split(" ")[-1])

    comm.reverse()
    his.reverse()
    print(his)
    print(comm)
    print(accumulator)


def p2_inverse_solve():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    lines.reverse()

    def recursive_restore(command_path, current_counter):
        # counter已到達第一行，此path是最佳解
        if len(lines) - 1 == current_counter:
            return True

        # 找有jmp到此行的所有指令
        for last_counter, last_command in enumerate(lines):
            if last_command[0] == 'j' and last_counter - int(
                    last_command.split(" ")[-1]) == current_counter and last_counter not in command_path:
                command_path.append(last_counter)
                if not recursive_restore(command_path, last_counter):
                    command_path.pop()  # 收到死路 去除path中這個counter
                else:
                    return True  # 已到達最佳解，回報上層

        # 檢查是不是上一行執行下來的
        if current_counter + 1 not in command_path:
            if lines[current_counter + 1][0] == 'j' and int(lines[current_counter + 1].split(" ")[-1]) != 1:
                return False  # (如果上一行是jmp 且數值超過1 就不會執行這行，回報死路)

            command_path.append(current_counter + 1)
            if not recursive_restore(command_path, current_counter + 1):
                command_path.pop()  # 收到死路 去除path中這個counter
            else:
                return True  # 已到達最佳解，回報上層

        return False  # 找不到其他可能方法，回報死路

    path = []
    for change_line_index in range(0, len(lines) - 1):
        if lines[change_line_index][0] == 'n':
            lines[change_line_index] = f"jmp {lines[change_line_index][4:]}"
        elif lines[change_line_index][0] == 'j':
            lines[change_line_index] = f"nop {lines[change_line_index][4:]}"

        path = [0]
        success = recursive_restore(path, 0)
        if success:
            break

        if lines[change_line_index][0] == 'n':
            lines[change_line_index] = f"jmp {lines[change_line_index][4:]}"
        elif lines[change_line_index][0] == 'j':
            lines[change_line_index] = f"nop {lines[change_line_index][4:]}"

    accumulator = 0
    for elem in path:
        if lines[elem][0] == 'a':
            accumulator += int(lines[elem].split(" ")[-1])

    print(accumulator)


if __name__ == '__main__':
    # p1()
    start = timeit.default_timer()
    p2()
    print(f"p2 cost {timeit.default_timer() - start} s")
    # p2_inverse_find_correct_path()
    start = timeit.default_timer()
    p2_inverse_solve()
    print(f"p2_inverse_solve cost {timeit.default_timer() - start} s")
