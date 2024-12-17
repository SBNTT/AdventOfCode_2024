DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)
DIR_UP = (0, -1)
DIR_DOWN = (0, 1)


def parseInput():
    start_pos = (0, 0)
    end_pos = (0, 0)
    grid = []
    with open("input.txt") as f:
        for y, line in enumerate(f):
            grid.append(list(line.strip()))
            if 'S' in grid[-1]:
                start_pos = (grid[-1].index('S'), y)
            if 'E' in grid[-1]:
                end_pos = (grid[-1].index('E'), y)

    return grid, start_pos, end_pos


def part1() -> int:
    grid, start_pos, end_pos = parseInput()

    weights = {
        start_pos: 1
    }

    stack = [(start_pos, DIR_RIGHT)]

    while len(stack) > 0:
        current_pos, current_dir = stack[-1]
        current_weight = weights[current_pos]
        next_pos = (
            current_pos[0] + current_dir[0],
            current_pos[1] + current_dir[1]
        )

        if grid[next_pos[1]][next_pos[0]] in '.E' \
                and (next_pos not in weights or weights[next_pos] > current_weight + 1):
            weights[next_pos] = current_weight + 1
            stack.append((next_pos, current_dir))
            continue

        for next_dir in [DIR_LEFT, DIR_RIGHT, DIR_DOWN, DIR_UP]:
            next_pos = (
                current_pos[0] + next_dir[0],
                current_pos[1] + next_dir[1]
            )

            if grid[next_pos[1]][next_pos[0]] in '.E' \
                    and (next_pos not in weights or weights[next_pos] > current_weight + 1001):
                weights[next_pos] = current_weight + 1001
                stack.append((next_pos, next_dir))
                break
        else:
            stack.pop()

    return weights[end_pos] - 1


def part2() -> int:
    return 0


if __name__ == '__main__':
    print(f"part1: {(shortest_path := part1())}")
    print(f"part2: {part2()}")
