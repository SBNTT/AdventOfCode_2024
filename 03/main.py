import re


def parseInput() -> str:
    lines = []
    with open("input.txt") as f:
        for line_str in f:
            lines.append(line_str.strip())

    return ''.join(lines)


def part1() -> int:
    code = parseInput()
    matches = re.finditer(r"mul\((\d+),(\d+)\)", code)
    return sum([int(match.groups()[0]) * int(match.groups()[1]) for match in matches])


def part2() -> int:
    code = parseInput()
    matches = re.finditer(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", code)

    total = 0
    do = True
    for match in matches:
        if match.groups()[2] is not None:
            do = True
        elif match.groups()[3] is not None:
            do = False
        elif do:
            total += int(match.groups()[0]) * int(match.groups()[1])

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
