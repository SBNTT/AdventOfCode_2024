def parseInput() -> list[list[int]]:
    grid = []
    with open("input.txt") as f:
        for line in f:
            grid.append([int(nb) for nb in line.strip()])

    return grid


def getPossiblePaths(grid: list[list[int]], pos: tuple[int, int]):
    x, y = pos
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbors = []

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == grid[y][x] + 1:
            neighbors.append((nx, ny))

    return neighbors


def countTrails(grid: list[list[int]], start_position: tuple[int, int]):
    stack = [(start_position, getPossiblePaths(grid, start_position))]
    tops = set()
    count = 0
    while len(stack) > 0:
        [pos, possible_paths] = stack.pop()
        if grid[pos[1]][pos[0]] == 9:
            tops.add(pos)
            count += 1
            continue

        if len(possible_paths) == 0:
            continue

        next_pos = possible_paths.pop()
        stack.append((pos, possible_paths))
        stack.append((next_pos, getPossiblePaths(grid, next_pos)))

    return len(tops), count


def part1() -> int:
    grid = parseInput()

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                total += countTrails(grid, (x, y))[0]

    return total


def part2() -> int:
    grid = parseInput()

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                total += countTrails(grid, (x, y))[1]

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
