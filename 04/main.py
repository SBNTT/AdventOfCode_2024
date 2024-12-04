def parseInput() -> list[str]:
    lines = []
    with open("input.txt") as f:
        for line_str in f:
            lines.append(line_str.strip())

    return lines


def readWordFromGrid(
        grid: list[str],
        x: int, y: int,
        dir_x: int, dir_y: int,
        length: int,
) -> str:
    word = ''
    for i in range(length):
        cx = x + dir_x * i
        cy = y + dir_y * i
        if cx < 0 or cy < 0 or cx >= len(grid[0]) or cy >= len(grid):
            break
        word += grid[cy][cx]

    return word


def part1() -> int:
    grid = parseInput()

    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] != "X":
                continue
                
            for dir_x in range(-1, 2):
                for dir_y in range(-1, 2):
                    if readWordFromGrid(grid, x, y, dir_x, dir_y, 4) == 'XMAS':
                        total += 1

    return total


def part2() -> int:
    grid = parseInput()

    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] != "A":
                continue

            word_a = readWordFromGrid(grid, x - 1, y - 1, 1, 1, 3)
            word_b = readWordFromGrid(grid, x + 1, y - 1, -1, 1, 3)

            if (word_a == 'MAS' or word_a == 'SAM') and (word_b == 'MAS' or word_b == 'SAM'):
                total += 1

    return total

if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
