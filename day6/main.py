def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    groups = []
    questions = set()

    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        if line == "":
            groups.append(questions.copy())
            questions.clear()
            continue

        for char in line:
            questions.add(char)

    groups.append(questions.copy())  # last record

    q_count = 0
    for group in groups:
        q_count += len(group)

    print(q_count)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            lines.append(line)
            line = fp.readline()

    groups = []
    first_questions = set()
    q_count = 0
    first_user = True

    for idx, line in enumerate(lines):
        line = line[:-1]  # remove \n

        if line == "":
            q_count += len(first_questions)
            first_questions.clear()
            first_user = True
            continue

        user_questions = set()
        if first_user:
            for char in line:
                first_questions.add(char)
            first_user = False
        else:
            for char in line:
                user_questions.add(char)
            first_questions = first_questions.intersection(user_questions)

    q_count += len(first_questions)
    print(q_count)


if __name__ == '__main__':
    # p1()
    p2()
