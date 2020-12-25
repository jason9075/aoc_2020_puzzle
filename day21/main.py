from collections import defaultdict


def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()

    def zero():
        return 0

    ingredient_dict = defaultdict(zero)
    allergens_set = set()
    for line in lines:
        ingredients = line.split('(')[0]
        ingredients = ingredients.strip().split(' ')
        for i in ingredients:
            ingredient_dict[i] += 1
        allergens = line.split('(')[1]
        allergens = allergens[9:-1]
        allergens = allergens.strip().split(',')
        for a in allergens:
            allergens_set.add(a.strip())

    count_list = []
    for (k, v) in ingredient_dict.items():
        count_list.append(v)

    count_list.sort()

    total = 0
    for i in range(len(count_list) - len(allergens_set)):
        total += count_list[i]

    print(total)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()

    # count
    def zero():
        return 0

    ingredient_dict = defaultdict(zero)
    for line in lines:
        ingredients = line.split('(')[0]
        ingredients = ingredients.strip().split(' ')
        for i in ingredients:
            ingredient_dict[i] += 1
    single_set = set()
    for (k, v) in ingredient_dict.items():
        if v <= 18:  # by p1
            single_set.add(k)

    ingredients = []
    allergens = []
    for line in lines:
        ingredient = line.split('(')[0]
        ingredient = ingredient.strip().split(' ')
        ingredient = [i for i in ingredient if i not in single_set]
        ingredients.append(ingredient)
        allergen = line.split('(')[1]
        allergen = allergen[9:-1]
        allergen = allergen.strip().split(',')
        allergen = [a.strip() for a in allergen]
        allergens.append(allergen)

    possible_dict = {}
    a_set = set()
    for a in allergens:
        for elm in a:
            a_set.add(elm)

    i_set = set()
    for i in ingredients:
        for elm in i:
            i_set.add(elm)

    for suppose_a in a_set:
        possible_dict[suppose_a] = []
        for suppose_i in i_set:
            match_correct = True
            for idx, (i, a) in enumerate(zip(ingredients, allergens)):
                if suppose_a in a:
                    if suppose_i not in i:
                        match_correct = False
                        break

            if match_correct:
                possible_dict[suppose_a].append(suppose_i)

    print(possible_dict)
    answer_dict = {}

    while len(answer_dict) != len(possible_dict):
        remove_name = ''
        for k, v in possible_dict.items():
            if len(v) == 1:
                remove_name = v[0]
                answer_dict[remove_name] = k
                break

        for k, v in possible_dict.items():
            if remove_name in v:
                v.remove(remove_name)

    answer_dict = {k: v for k, v in sorted(answer_dict.items(), key=lambda item: item[1])}
    allergen_ingredients = []
    for key in answer_dict.keys():
        allergen_ingredients.append(key)

    print(allergen_ingredients)
    print(','.join(allergen_ingredients))


if __name__ == '__main__':
    # p1()
    p2()
