def parseInput() -> tuple[list[int], list[int]]:
    list_a, list_b = [], []
    with open("input.txt") as f:
        for line_str in f:
            line = line_str.split()
            list_a.append(int(line[0]))
            list_b.append(int(line[1]))

    return list_a, list_b


def part1() -> int:
    list_a, list_b = parseInput()
    list_a.sort()
    list_b.sort()

    total = 0
    for (a, b) in zip(list_a, list_b):
        total += abs(a - b)

    return total


def part2() -> int:
    list_a, list_b = parseInput()

    total = 0
    for a in list_a:
        total += a * list_b.count(a)

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
