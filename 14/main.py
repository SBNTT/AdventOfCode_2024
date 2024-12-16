import re
from functools import reduce
from operator import mul


def parseInput() -> list[tuple[tuple[int, int], tuple[int, int]]]:
    robots = []
    with open("input.txt") as f:
        for line in f:
            split_line = re.split(r'[\s=,]', line)
            robots.append(([int(split_line[1]), int(split_line[2])], (int(split_line[4]), int(split_line[5]))))

    return robots


def part1() -> int:
    w = 101
    h = 103
    time = 100

    robots = parseInput()
    quadrants_counts = [0, 0, 0, 0]
    for (posx, posy), (velx, vely) in robots:
        final_posx, final_posy = (
            (posx + velx * time) % w,
            (posy + vely * time) % h,
        )

        if 0 <= final_posx < w // 2:
            if 0 <= final_posy < h // 2:
                quadrants_counts[0] += 1
            elif h // 2 + 1 <= final_posy < h:
                quadrants_counts[1] += 1
        elif w // 2 + 1 <= final_posx < w:
            if 0 <= final_posy < h // 2:
                quadrants_counts[2] += 1
            elif h // 2 + 1 <= final_posy < h:
                quadrants_counts[3] += 1

    return reduce(mul, quadrants_counts)


def part2():
    w = 101
    h = 103
    robots = parseInput()

    i = 0
    while True:
        i += 1
        print('-' * w)
        print(f'frame {i}')
        input()

        poss = set()
        for robot in robots:
            robot[0][0] = (robot[0][0] + robot[1][0]) % w
            robot[0][1] = (robot[0][1] + robot[1][1]) % h
            poss.add(tuple(robot[0]))

        for y in range(h):
            for x in range(w):
                print('■' if (x, y) in poss else ' ', end='')
            print()


if __name__ == '__main__':
    print(f"part1: {part1()}")
    part2()
