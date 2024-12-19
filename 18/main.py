DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)
DIR_UP = (0, -1)
DIR_DOWN = (0, 1)

DIRECTIONS = [DIR_LEFT, DIR_RIGHT, DIR_DOWN, DIR_UP]


def parseInput():
    with open("input.txt") as f:
        return [(int(nbs[0]), int(nbs[1])) for line in f for nbs in [line.strip().split(',')]]


def find_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])

    stack = [(0, start)]
    path_history = {}
    weights = {start: 0}

    while stack:
        stack.sort()
        current_weight, current = stack.pop(0)

        if current == end:
            path = []
            while current in path_history:
                path.append(current)
                current = path_history[current]
            path.append(start)
            return path[::-1]

        for dx, dy in DIRECTIONS:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] != 1:
                next_weight = weights[current] + 1

                if neighbor not in weights or next_weight < weights[neighbor]:
                    weights[neighbor] = next_weight
                    path_history[neighbor] = current
                    stack.append((next_weight, neighbor))

    return None


def part1() -> int:
    walls = parseInput()[:1024]

    size = 71
    start_pos = (0, 0)
    end_pos = (size - 1, size - 1)

    grid = [[0 for _ in range(size)] for _ in range(size)]
    for wx, wy in walls:
        grid[wy][wx] = 1

    path = find_path(grid, start_pos, end_pos)
    return len(path) - 1


def part2() -> tuple[int, int]:
    walls = parseInput()

    size = 71
    start_pos = (0, 0)
    end_pos = (size - 1, size - 1)

    grid = [[0 for _ in range(size)] for _ in range(size)]
    for i, (wx, wy) in enumerate(walls):
        grid[wy][wx] = 1
        print(f'{i} / {len(walls)}')
        if find_path(grid, start_pos, end_pos) is None:
            return wx, wy

    return 0, 0


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
