def find_sum(target, numbers):
    for i, first in enumerate(numbers[:-1]):
        for j, second in enumerate(numbers[i + 1:]):
            if target == first + second:
                return True

    return False


def p1():
    length_of_preamble = 25
    numbers = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            numbers.append(int(line))
            line = fp.readline()

    for idx, check_value in enumerate(numbers[length_of_preamble:]):

        is_valid = find_sum(check_value, numbers[idx:idx + length_of_preamble])

        if not is_valid:
            print(check_value)
            break


def p2(invalid_number):
    numbers = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            numbers.append(int(line))
            line = fp.readline()

    is_find = False
    ans_start_index = 0
    ans_end_index = 0
    for i in range(len(numbers) - 1):
        if is_find:
            break
        for j in range(i + 1, len(numbers)):
            number_sum = sum(numbers[i:j])
            if invalid_number == number_sum:
                is_find = True
                ans_start_index = i
                ans_end_index = j
                break
            elif invalid_number < number_sum:
                break

    max_vale = max(numbers[ans_start_index:ans_end_index])
    min_vale = min(numbers[ans_start_index:ans_end_index])

    print(max_vale+min_vale)

if __name__ == '__main__':
    # p1()
    # p2(127)
    p2(400480901)
