from functools import lru_cache


def parseInput() -> tuple[list[str], list[str]]:
    with open("input.txt") as f:
        patterns = f.readline().strip().split(', ')
        f.readline()
        designs = [line.strip() for line in f.readlines()]

    return patterns, designs


def part1() -> int:
    patterns, designs = parseInput()

    @lru_cache()
    def check_design(design: str) -> int:
        if design == '':
            return 1

        for pattern in patterns:
            if design.startswith(pattern):
                if check_design(design[len(pattern):]):
                    return 1

        return 0

    return sum([check_design(design) for design in designs])


def part2() -> int:
    patterns, designs = parseInput()

    @lru_cache()
    def check_design(design: str) -> int:
        if design == '':
            return 1

        total = 0
        for pattern in patterns:
            if design.startswith(pattern):
                total += check_design(design[len(pattern):])

        return total

    return sum([check_design(design) for design in designs])


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
