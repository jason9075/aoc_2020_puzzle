def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()

    def do_op(first, op, second):
        if op == '+':
            return first + second
        if op == '*':
            return first * second

    def calculate(text):
        value = 0
        op = '+'
        idx = 0
        while idx < len(text):
            char = text[idx]
            if char == ' ':
                idx += 1
                continue
            if char == '+' or char == '*':
                op = char
            elif char == '(':
                diff, result_of_next = calculate(text[idx + 1:])
                value = do_op(value, op, result_of_next)
                idx += (diff + 2)
                continue
            elif char == ')':
                return idx, value
            else:
                if value == 0:
                    value = int(char)
                else:
                    value = do_op(value, op, int(char))
            idx += 1

        return value

    total = 0
    for line in lines:
        answer = calculate(line)
        total += answer
    print(total)


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
    # p1()
    p2()
