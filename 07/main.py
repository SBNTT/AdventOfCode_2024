from functools import reduce


def parseInput() -> list[tuple[int, list[int]]]:
    equations = []
    with open("input.txt") as f:
        for line_str in f:
            line = line_str.split(': ')
            equations.append((int(line[0]), [int(nb) for nb in line[1].split(' ')]))

    return equations


def computeResult(base: int) -> int:
    def baseN(num, b, numerals="012"):
        return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

    equations = parseInput()

    total = 0
    for expected_result, numbers in equations:
        for i in range(base ** (positions := len(numbers) - 1)):
            operators = baseN(i, base).zfill(positions)
            if reduce(
                    lambda result, p: (
                            result + numbers[p + 1] if operators[p] == '0' else
                            result * numbers[p + 1] if operators[p] == '1' else
                            int(str(result) + str(numbers[p + 1]))
                    ),
                    range(positions),
                    numbers[0]
            ) == expected_result:
                total += expected_result
                break

    return total


if __name__ == '__main__':
    print(f"part1: {computeResult(base=2)}")
    print(f"part2: {computeResult(base=3)}")
