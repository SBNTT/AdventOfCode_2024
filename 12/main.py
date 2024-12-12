DIR_LEFT = (-1, 0)
DIR_RIGHT = (1, 0)
DIR_UP = (0, -1)
DIR_DOWN = (0, 1)


def parseInput() -> tuple[list[list[str]], list[set[tuple[int, int]]], int, int]:
    with open("input.txt") as f:
        grid = [list(line.strip()) for line in f]

    width, height = len(grid[0]), len(grid)
    positions_to_visit = [(x, y) for x in range(width) for y in range(height)]
    regions = []

    def discover(x: int, y: int):
        for (dir_x, dir_y) in [DIR_LEFT, DIR_RIGHT, DIR_UP, DIR_DOWN]:
            nx, ny = x + dir_x, y + dir_y
            if 0 <= nx < width and 0 <= ny < height \
                    and grid[y][x] == grid[ny][nx] \
                    and (nx, ny) in positions_to_visit:
                positions_to_visit.remove((nx, ny))
                regions[-1].add((nx, ny))
                discover(*(nx, ny))

    while len(positions_to_visit) > 0:
        pos = positions_to_visit.pop()
        regions.append(set())
        regions[-1].add(pos)
        discover(*pos)

    return grid, regions, width, height


def part1() -> int:
    grid, regions, w, h = parseInput()

    total = 0
    for region in regions:
        perimeter = 0
        for (x, y) in region:
            for (dir_x, dir_y) in [DIR_LEFT, DIR_RIGHT, DIR_UP, DIR_DOWN]:
                nx, ny = x + dir_x, y + dir_y
                if not (0 <= nx < w and 0 <= ny < h) or grid[y][x] != grid[ny][nx]:
                    perimeter += 1

        total += len(region) * perimeter

    return total


def part2() -> int:
    grid, regions, w, h = parseInput()

    total = 0
    for region in regions:
        corners = 0
        for (x, y) in region:
            for ((dir_xa, dir_ya), (dir_xb, dir_yb)) in [
                (DIR_LEFT, DIR_UP),
                (DIR_UP, DIR_RIGHT),
                (DIR_RIGHT, DIR_DOWN),
                (DIR_DOWN, DIR_LEFT),
            ]:
                nxa, nya, nxb, nyb = x + dir_xa, y + dir_ya, x + dir_xb, y + dir_yb
                nxc, nyc = x + dir_xa + dir_xb, y + dir_ya + dir_yb

                # outer corner
                if (not (0 <= nxa < w and 0 <= nya < h) or grid[y][x] != grid[nya][nxa]) \
                        and (not (0 <= nxb < w and 0 <= nyb < h) or grid[y][x] != grid[nyb][nxb]):
                    corners += 1

                # inner corner
                if (0 <= nxa < w and 0 <= nya < h and grid[y][x] == grid[nya][nxa]) \
                        and (0 <= nxb < w and 0 <= nyb < h and grid[y][x] == grid[nyb][nxb]) \
                        and (0 <= nxc < w and 0 <= nyc < h and grid[y][x] != grid[nyc][nxc]):
                    corners += 1

        total += len(region) * corners

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
