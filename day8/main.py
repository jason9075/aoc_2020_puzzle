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

    for change_line_index in range(0, len(lines)):
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
            print(accumulator)


if __name__ == '__main__':
    # p1()
    p2()
