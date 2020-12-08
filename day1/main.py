def p1():
    numbers = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            numbers.append(int(line))
            line = fp.readline()

    print(numbers)

    for i, front in enumerate(numbers[:-1]):
        for j, back in enumerate(numbers[i + 1:]):
            if front + back == 2020:
                print(front)
                print(back)
                print(front * back)


def p2():
    numbers = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            numbers.append(int(line))
            line = fp.readline()

    print(numbers)

    for i, first in enumerate(numbers[:-2]):
        for j, second in enumerate(numbers[i + 1:-1]):
            for k, third in enumerate(numbers[i + j + 2:]):
                if first + second + third == 2020:
                    print(first)
                    print(second)
                    print(third)
                    print(first * second * third)


if __name__ == '__main__':
    # p1()
    p2()
