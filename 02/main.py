def parseInput() -> list[list[int]]:
    lines = []
    with open("input.txt") as f:
        for line_str in f:
            lines.append(list(map(int, line_str.split())))

    return lines


def isReportSafe(report: list[int]) -> bool:
    direction = None
    for pos in range(len(report) - 1):
        if abs(report[pos] - report[pos + 1]) not in (1, 2, 3):
            break
        if direction is None:
            direction = report[pos] - report[pos + 1] > 0
        elif direction != (report[pos] - report[pos + 1] > 0):
            break
    else:
        return True

    return False


def part1() -> int:
    reports = parseInput()
    return sum(1 for report in reports if isReportSafe(report))


def part2() -> int:
    reports = parseInput()

    total = 0
    for report in reports:
        for pos in range(len(report)):
            if isReportSafe([x for i, x in enumerate(report) if i != pos]):
                total += 1
                break

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
