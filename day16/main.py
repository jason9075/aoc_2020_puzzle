def p1():
    available_range = []
    near_by_ticket = []

    is_collect_range = True
    is_my_ticket = False
    is_near_by_ticket = False
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            if line == '\n':
                line = fp.readline()
                continue
            line = line[:-1]

            if line == 'your ticket:':
                is_collect_range = False
                is_my_ticket = True
                line = fp.readline()
                continue

            if line == 'nearby tickets:':
                is_my_ticket = False
                is_near_by_ticket = True
                line = fp.readline()
                continue

            if is_collect_range:
                line = line.split(': ')[-1]
                r1 = line.split(' ')[0]
                r2 = line.split(' ')[2]
                available_range.append((int(r1.split('-')[0]), int(r1.split('-')[1])))
                available_range.append((int(r2.split('-')[0]), int(r2.split('-')[1])))
            elif is_my_ticket:
                pass
            elif is_near_by_ticket:
                near_by_ticket.append(line.split(','))

            line = fp.readline()

    error = 0
    for nums in near_by_ticket:
        for num in nums:
            num = int(num)

            is_error = True
            for r in available_range:
                if int(r[0]) <= num <= int(r[1]):
                    is_error = False
                    break

            if is_error:
                error += num

    print(error)


def p2():
    my_ticket = None
    available_range = []
    near_by_ticket = []

    is_collect_range = True
    is_my_ticket = False
    is_near_by_ticket = False
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            if line == '\n':
                line = fp.readline()
                continue
            line = line[:-1]

            if line == 'your ticket:':
                is_collect_range = False
                is_my_ticket = True
                line = fp.readline()
                continue

            if line == 'nearby tickets:':
                is_my_ticket = False
                is_near_by_ticket = True
                line = fp.readline()
                continue

            if is_collect_range:
                line = line.split(': ')[-1]
                r1 = line.split(' ')[0]
                r2 = line.split(' ')[2]
                available_range.append(
                    (int(r1.split('-')[0]), int(r1.split('-')[1]), int(r2.split('-')[0]), int(r2.split('-')[1])))
            elif is_my_ticket:
                my_ticket = line.split(',')
                my_ticket = [int(n) for n in my_ticket]
            elif is_near_by_ticket:
                near_by_ticket.append(line.split(','))

            line = fp.readline()

    valid_tickets = []
    for nums in near_by_ticket:
        is_error = False

        for num in nums:
            is_in_range = False
            num = int(num)

            for r in available_range:
                if int(r[0]) <= num <= int(r[1]) or int(r[2]) <= num <= int(r[3]):
                    is_in_range = True  # at least in range
                    break

            if not is_in_range:  # this num not fit any range:
                is_error = True
                break

        if not is_error:
            nums = [int(n) for n in nums]
            valid_tickets.append(nums)

    print(len(valid_tickets))
    column_index = {}

    for range_idx, ar in enumerate(available_range):
        compat_index = []
        for ticket_index in range(0, len(available_range)):
            not_this_index = False

            for valid_ticket in valid_tickets:
                num = valid_ticket[ticket_index]
                if num < int(ar[0]) or int(ar[1]) < num < int(ar[2]) or int(ar[3]) < num:
                    not_this_index = True
                    break
            if not_this_index:
                continue
            else:
                compat_index.append(ticket_index)
        column_index[range_idx] = compat_index

    print(column_index)

    answer_dict = {}
    chosen_set = set([])

    while True:
        for idx, (key, column) in enumerate(column_index.items()):
            if len(column) == len(answer_dict) + 1:
                accept_set = set(column)
                accept_set = accept_set - chosen_set
                answer_dict[key] = accept_set.pop()
                chosen_set.add(answer_dict[key])

        if len(answer_dict) == len(column_index):
            break

    print(answer_dict)

    total = 1
    for idx in range(6):
        total *= my_ticket[answer_dict[idx]]

    print(total)


if __name__ == '__main__':
    # p1()
    p2()
