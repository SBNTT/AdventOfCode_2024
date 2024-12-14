import re


def parseInput() -> list[list[int]]:
    machines = [[]]
    with open("input.txt") as f:
        for line in f:
            if (line := line.strip()) == '':
                machines.append([])
            else:
                split_line = re.split(r': |, |[XY]\+?=?', line)
                machines[-1].append((int(split_line[2]), int(split_line[4])))

    return machines


def solve(a_dirx, a_diry, b_dirx, b_diry, target_x, target_y):
    det = 3 * a_dirx * b_diry - 3 * a_diry * b_dirx
    det_A = target_x * b_diry - target_y * b_dirx
    det_B = 3 * a_dirx * target_y - 3 * a_diry * target_x

    A = det_A / det
    B = det_B / det

    return A * 3, B


def part1() -> int:
    machines = parseInput()

    total = 0
    for (a_dirx, a_diry), (b_dirx, b_diry), (target_x, target_y) in machines:
        (a, b) = solve(a_dirx, a_diry, b_dirx, b_diry, target_x, target_y)
        if int(a) == a and int(b) == b and a < 100 and b < 100:
            total += (int(a) * 3 + int(b))

    return total


def part2() -> int:
    machines = parseInput()

    total = 0
    for (a_dirx, a_diry), (b_dirx, b_diry), (target_x, target_y) in machines:
        (a, b) = solve(a_dirx, a_diry, b_dirx, b_diry, target_x + 10000000000000, target_y + 10000000000000)
        if int(a) == a and int(b) == b:
            total += (int(a) * 3 + int(b))

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
