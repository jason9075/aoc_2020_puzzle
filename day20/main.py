from collections import defaultdict


class Tile:
    def __init__(self, id_num, left, top, right, bottom):
        self.id_num = id_num
        self.front_edges = [left, top, right, bottom]
        self.back_edges = [right[::-1], top[::-1], left[::-1], bottom[::-1]]
        self.front_match_id =set()
        self.back_match_id =set()
        self.match_count = 0


def p1():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()

    tiles = []
    for idx in range(0, len(lines), 12):
        id_num = int(lines[idx].split(' ')[1][:-1])
        left, right = '', ''
        for j in range(0, 10):
            left += lines[idx + 10 - j][0]
            right += lines[idx + 1 + j][9]
        top = lines[idx + 1]
        bottom = lines[idx + 10][::-1]
        tile = Tile(id_num, left, top, right, bottom)
        tiles.append(tile)

    for tile_a in tiles[:-1]:
        for tile_b in tiles[1:]:
            match_other = False

            # af vs bf
            for edge_a in tile_a.front_edges:
                if match_other:
                    break
                for edge_b in tile_b.front_edges:
                    edge_b = edge_b[::-1]
                    if edge_a == edge_b:
                        tile_a.match_count += 1
                        tile_b.match_count += 1
                        tile_a.front_match_id.add(f'{tile_b.id_num}.f')
                        tile_b.front_match_id.add(f'{tile_a.id_num}.f')
                        match_other = True
                        break
            # af vs bb
            for edge_a in tile_a.front_edges:
                if match_other:
                    break
                for edge_b in tile_b.back_edges:
                    edge_b = edge_b[::-1]
                    if edge_a == edge_b:
                        tile_a.match_count += 1
                        tile_b.match_count += 1
                        tile_a.front_match_id.add(f'{tile_b.id_num}.b')
                        tile_b.back_match_id.add(f'{tile_a.id_num}.f')
                        match_other = True
                        break

            # ab vs bf
            for edge_a in tile_a.back_edges:
                if match_other:
                    break
                for edge_b in tile_b.front_edges:
                    edge_b = edge_b[::-1]
                    if edge_a == edge_b:
                        tile_a.match_count += 1
                        tile_b.match_count += 1
                        tile_a.back_match_id.add(f'{tile_b.id_num}.f')
                        tile_b.front_match_id.add(f'{tile_a.id_num}.b')
                        match_other = True
                        break

            # ab vs bb
            for edge_a in tile_a.back_edges:
                if match_other:
                    break
                for edge_b in tile_b.back_edges:
                    edge_b = edge_b[::-1]
                    if edge_a == edge_b:
                        tile_a.match_count += 1
                        tile_b.match_count += 1
                        tile_a.back_match_id.add(f'{tile_b.id_num}.b')
                        tile_b.back_match_id.add(f'{tile_a.id_num}.b')
                        match_other = True
                        break

    match_counts = [t.match_count for t in tiles]
    print(1)


def p2():
    lines = []
    with open('input.txt') as fp:
        line = fp.readline()
        while line:
            line = line[:-1]
            lines.append(line)
            line = fp.readline()


if __name__ == '__main__':
    p1()
    # p2()
