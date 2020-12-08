def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    contain_map = {}

    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        descriptions = line.split(",")

        key = ""
        values = []

        for i, description in enumerate(descriptions):
            words = description.split(" ")

            if i == 0:
                key = f'{words[0]} {words[1]}'
                values.append(f'{words[-3]} {words[-2]}')
                continue
            values.append(f'{words[-3]} {words[-2]}')

        contain_map[key] = values

    # print(contain_map)

    def recursive(k, vs):
        if k == 'no other':
            return False
        elif k == 'shiny gold':
            return True
        for v in vs:
            if v == 'no other':
                continue
            if recursive(v, contain_map[v]):
                return True
        return False

    shiny_gold_count = 0
    for (contain_key, contain_values) in contain_map.items():
        if contain_key == 'shiny gold':
            continue  # shiny gold 本身不算
        if recursive(contain_key, contain_values):
            shiny_gold_count += 1

    print(shiny_gold_count)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    contain_map = {}

    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        descriptions = line.split(",")

        key = ""
        values = {}

        for i, description in enumerate(descriptions):
            words = description.split(" ")

            if i == 0:
                if f'{words[-3]} {words[-2]}' == 'no other':
                    continue
                key = f'{words[0]} {words[1]}'
                values[f'{words[-3]} {words[-2]}'] = int(words[-4])
                continue
            values[f'{words[-3]} {words[-2]}'] = int(words[-4])

        contain_map[key] = values

    # print(contain_map)

    def recursive_count(v_dict):
        count = 0
        for v_k, v_count in v_dict.items():
            count += v_count
            if v_k not in contain_map.keys():
                continue
            count += v_count * recursive_count(contain_map[v_k])
        return count

    shiny_gold_count = recursive_count(contain_map['shiny gold'])
    print(shiny_gold_count)


if __name__ == '__main__':
    # p1()
    p2()
