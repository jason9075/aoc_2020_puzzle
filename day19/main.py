def p1():
    is_rule = True
    rules = []
    messages = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            if line == '\n':
                is_rule = False
                line = fp.readline()
                continue

            line = line[:-1]
            if is_rule:
                rules.append(line)
            else:
                messages.append(line)

            line = fp.readline()

    # print(rules)
    max_len_of_message = 10
    print(max_len_of_message)

    rule_dict = {}
    for rule in rules:
        split_char = rule.split('"')
        if len(split_char) == 3:
            key = int(split_char[0].split(':')[0])
            rule_dict[key] = split_char[1]
        else:
            split_char = rule.split(':')
            key = int(split_char[0])

            sub_rules = split_char[1][1:].split('|')
            sub_rules = [(sr.strip().split(' ')) for sr in sub_rules]
            rule_dict[key] = sub_rules

    # print(rule_dict)

    finding_list = []
    rule_zero_msg = set()

    finding_list.extend(rule_dict[0])
    history_path = set()
    while len(finding_list) != 0:
        new_path = []
        finding_to_remove = []
        for path in finding_list:  # [1 2] [3 4] [5 6] [7]
            all_char = True
            for key in path:
                if key.isdigit():
                    all_char = False
                    break
            if all_char:
                rule_zero_msg.add(''.join(path))

                finding_to_remove.append(path)

            for idx, key in enumerate(path):  # 1 2
                if not key.isdigit():
                    continue
                next_result = rule_dict[int(key)]
                if type(next_result) is list:  # keep finding
                    for new_finding in next_result:
                        front_list = path[:idx]
                        front_list.extend(new_finding)
                        back_list = path[idx + 1:]
                        if max_len_of_message < len(back_list):
                            continue
                        front_list.extend(back_list)

                        # combine char together
                        # combine_list = []
                        # combine = ''
                        # combo = True
                        # for f in front_list:
                        #     if f.isdigit():
                        #         if 0 < len(combine):
                        #             combine_list.append(combine)
                        #         combine_list.append(f)
                        #         combo = False
                        #     elif combo:
                        #         combine += f
                        #     else:
                        #         combo = False
                        # if 0 < len(combine):
                        #     combine_list.append(combine)
                        if '-'.join(front_list) in history_path:
                            continue
                        history_path.add('-'.join(front_list))
                        new_path.append(front_list)
                    finding_to_remove.append(path)
                else:
                    path[idx] = next_result  # is char

        finding_list = [elm for elm in finding_list if elm not in finding_to_remove]
        finding_list.extend(new_path)
        print(f'remain:{len(finding_list)}, ways:{len(rule_zero_msg)}')

    total = 0
    for message in messages:
        if message in rule_zero_msg:
            total += 1

    print(total)


def p1_method2():
    is_rule = True
    rules = []
    messages = []
    with open('input-test.txt') as fp:
        line = fp.readline()
        while line:
            if line == '\n':
                is_rule = False
                line = fp.readline()
                continue

            line = line[:-1]
            if is_rule:
                rules.append(line)
            else:
                messages.append(line)

            line = fp.readline()

    # print(rules)
    # print(messages)

    rule_dict = {}
    for rule in rules:
        split_char = rule.split('"')
        if len(split_char) == 3:
            key = int(split_char[0].split(':')[0])
            rule_dict[key] = [split_char[1]]
        else:
            split_char = rule.split(':')
            key = int(split_char[0])

            sub_rules = split_char[1][1:].split('|')
            sub_rules = [(sr.strip().split(' ')) for sr in sub_rules]
            rule_dict[key] = sub_rules

    # update rule_dict
    for key, paths in rule_dict.items():
        for pi, path in enumerate(paths):  # [[1,2],[3,4]]
            for ki, next_key in enumerate(path):  # [1,2]
                next_values = rule_dict[int(next_key)]
                # if next values is all char update it
                is_all_char = 0 < sum([not e.isdigit() for e in next_values])
                if is_all_char:
                    rule_dict[key][pi][ki] = ''.join(next_values)


def p2():
    class Node:

        def __init__(self, op):

            self.left = None
            self.right = None
            self.data = op

        # Print the Tree
        def print_tree(self):
            if self.left:
                self.left.print_tree()
            print(self.data),
            if self.right:
                self.right.print_tree()

        def postorder_calc(self, r):
            if r.left is None:
                return r.data
            else:
                left = self.postorder_calc(r.left)
                right = self.postorder_calc(r.right)
                return left + right if r.data == '+' else \
                    left * right

    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()

    def calculate(text):
        op = '+'
        high_priority = False
        node = Node(0)
        idx = 0
        while idx < len(text):
            char = text[idx]
            if char == ' ':
                idx += 1
                continue
            if char == '+' or char == '*':
                op = char
                if op == '+':
                    high_priority = True
            elif char == '(':
                diff, sub_node = calculate(text[idx + 1:])
                sub_sum = sub_node.postorder_calc(sub_node)
                new_node = Node(op)
                if high_priority:
                    new_node.left = node.right
                    new_node.right = Node(sub_sum)
                    node.right = new_node
                    high_priority = False
                else:
                    new_node.left = node
                    new_node.right = Node(sub_sum)
                    node = new_node
                idx += (diff + 2)
                continue
            elif char == ')':
                return idx, node
            else:
                new_node = Node(op)
                if high_priority:
                    new_node.left = node.right
                    new_node.right = Node(int(char))
                    node.right = new_node
                    high_priority = False
                else:
                    new_node.left = node
                    new_node.right = Node(int(char))
                    node = new_node
            idx += 1

        return node

    total = 0
    for line in lines:
        root = calculate(line)
        result = root.postorder_calc(root)
        total += result
        # print(result)

    print(total)


if __name__ == '__main__':
    p1()
    # p1_method2()
