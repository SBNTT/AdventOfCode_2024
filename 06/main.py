def parseInput():
    lines = []
    starting_pos = (0, 0)
    with open("input.txt") as f:
        for y, line_str in enumerate(f):
            line = line_str.strip()
            lines.append(line := list(line_str.strip()))
            if '^' in line:
                starting_pos = (line.index('^'), y)

    return lines, starting_pos


def followPath(grid, position):
    #          up     right   down     left
    dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
    dir_i = 0

    positions = dict()
    while 0 <= position[0] < len(grid[0]) and 0 <= position[1] < len(grid):
        if grid[position[1]][position[0]] == '#':
            position = (position[0] - dirs[dir_i][0], position[1] - dirs[dir_i][1])  # go backward
            dir_i = (dir_i + 1) % len(dirs)  # turn

        if position not in positions:
            positions[position] = dir_i
        elif dir_i == positions[position]:
            return -1  # loop detected

        position = (position[0] + dirs[dir_i][0], position[1] + dirs[dir_i][1])  # go forward

    return len(positions)


def part1() -> int:
    grid, start_position = parseInput()

    return followPath(grid, start_position)


def part2() -> int:
    grid, start_position = parseInput()

    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] != '.':
                continue

            grid[y][x] = '#'
            if followPath(grid, start_position) == -1:
                total += 1
            grid[y][x] = '.'

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
