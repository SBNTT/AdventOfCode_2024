from itertools import permutations


def parseInput():
    with open("input.txt") as f:
        antennas = {}
        lines = [line.strip() for line in f]
        width, height = len(lines[0]), len(lines)
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c != '.':
                    antennas.setdefault(c, []).append((x, y))
    return width, height, antennas


def computeAntiNodes(max_steps: int | None, self_anti_node: bool):
    width, height, antennas = parseInput()

    anti_nodes = set()
    for positions in antennas.values():
        if self_anti_node and len(positions) > 1:
            anti_nodes.update(positions)

        for pos_a, pos_b in permutations(positions, 2):
            step_x, step_y = pos_b[0] - pos_a[0], pos_b[1] - pos_a[1]

            steps, x, y = 0, pos_b[0] + step_x, pos_b[1] + step_y
            while 0 <= x < width and 0 <= y < height and (max_steps is None or steps < max_steps):
                anti_nodes.add((x, y))
                steps, x, y = steps + 1, x + step_x, y + step_y

    return len(anti_nodes)


if __name__ == '__main__':
    print(f"part1: {computeAntiNodes(max_steps=1, self_anti_node=False)}")
    print(f"part2: {computeAntiNodes(max_steps=None, self_anti_node=True)}")
