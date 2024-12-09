def parseInput() -> str:
    with open("input.txt") as f:
        return f.readlines()[0]


def part1() -> int:
    disk = []
    for i in range(len(raw_map := parseInput())):
        disk += [i // 2 if i % 2 == 0 else None for _ in range(int(raw_map[i]))]

    end_pos = 0
    for i in range(len(disk) - 1, 0, -1):
        if disk[i] is not None:
            new_pos = disk.index(None)
            if new_pos >= i:
                end_pos = i
                break

            disk[new_pos] = disk[i]
            disk[i] = None

    total = 0
    for i, bloc_id in enumerate(disk[:end_pos + 1]):
        total += i * bloc_id

    return total


def part2() -> int:
    disk = []
    for i in range(len(raw_map := parseInput())):
        disk.append((i // 2 if i % 2 == 0 else None, int(raw_map[i])))

    i = len(disk)
    while i >= 0:
        i -= 1

        bloc_id, bloc_size = disk[i]
        if bloc_id is None:
            continue

        for j in range(i):
            target_bloc_id, target_bloc_size = disk[j]
            if target_bloc_id is not None:
                continue

            if target_bloc_size >= bloc_size:
                disk[j] = disk[i]
                disk[i] = (None, bloc_size)

                if target_bloc_size > bloc_size:
                    disk.insert(j + 1, (None, target_bloc_size - bloc_size))
                    i += 1

                break

    total = 0
    index = 0
    for bloc in disk:
        for i in range(bloc[1]):
            if bloc[0] is not None:
                total += index * bloc[0]
            index += 1

    return total


if __name__ == '__main__':
    # 6311837662089
    # 6311837662089
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
