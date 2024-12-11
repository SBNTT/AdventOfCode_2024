def parseInput() -> list[int]:
    with open("input.txt") as f:
        return [int(i) for i in f.readline().split(' ')]


def transform_nb(nb: int) -> list[int]:
    if nb == 0:
        return [1]
    elif len(str_nb := str(nb)) % 2 == 0:
        return [
            int(str_nb[:len(str_nb) // 2]),
            int(str_nb[len(str_nb) // 2:])
        ]
    else:
        return [nb * 2024]


def countStones(iterations: int) -> int:
    mapping = {nb: 1 for nb in parseInput()}

    for i in range(iterations):
        next_mapping = {}
        for number, count in mapping.items():
            for next_nb in transform_nb(number):
                if next_nb in next_mapping:
                    next_mapping[next_nb] += count
                else:
                    next_mapping[next_nb] = count

        mapping = next_mapping

    return sum(mapping.values())


if __name__ == '__main__':
    print(f"part1: {countStones(iterations=25)}")
    print(f"part2: {countStones(iterations=75)}")
