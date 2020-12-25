import numpy as np


def p1():
    order = '389125467'  # test input
    order = '167248359'  # real input

    pos_count = len(order)
    circle = np.zeros([pos_count])

    for idx, num in enumerate(order):
        circle[idx] = int(num)

    move_at_idx = 0

    def next_num_cup(current, delta, is_value=False):
        if current + delta < 0:
            return current + delta + pos_count
        elif current + delta == 0:
            return pos_count if is_value else 0
        return int((current + delta) % pos_count)

    for _ in range(100):
        pick_cup = circle[move_at_idx]
        other_three_list = [circle[next_num_cup(move_at_idx, 1)],
                            circle[next_num_cup(move_at_idx, 2)],
                            circle[next_num_cup(move_at_idx, 3)]]

        # find dest
        dest_value = next_num_cup(pick_cup, -1, is_value=True)
        while True:
            if dest_value in other_three_list:
                dest_value = next_num_cup(dest_value, -1, is_value=True)
            else:
                break

        # shift until dest
        shift_at_idx = next_num_cup(move_at_idx, 1)
        be_shifted_at_idx = next_num_cup(move_at_idx, 4)
        while True:
            if circle[be_shifted_at_idx] != dest_value:
                circle[shift_at_idx] = circle[be_shifted_at_idx]

                shift_at_idx = next_num_cup(shift_at_idx, 1)
                be_shifted_at_idx = next_num_cup(be_shifted_at_idx, 1)
            else:
                circle[shift_at_idx] = circle[be_shifted_at_idx]
                circle[be_shifted_at_idx] = other_three_list[-1]
                circle[next_num_cup(be_shifted_at_idx, -1)] = other_three_list[-2]
                circle[next_num_cup(be_shifted_at_idx, -2)] = other_three_list[-3]
                break

        move_at_idx = next_num_cup(move_at_idx, 1)

    one_index = 0
    for idx, num in enumerate(circle):
        if num == 1:
            one_index = idx
            break

    circle = [str(int(e)) for e in circle]
    pre = ''.join(circle[one_index + 1:])
    post = ''.join(circle[:one_index])
    print(f'{pre}{post}')


def p2():
    pass


if __name__ == '__main__':
    p1()
    # p2()
