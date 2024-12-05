def parseInput() -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules = []
    updates = []
    parsing_part_1 = True
    with open("input.txt") as f:
        for line_str in f:
            if line_str.strip() == '':
                parsing_part_1 = False
            elif parsing_part_1:
                str_list = line_str.strip().split('|')
                rules.append((int(str_list[0]), int(str_list[1])))
            else:
                updates.append(list(map(int, line_str.strip().split(','))))

    return rules, updates


def is_update_valid(update, rules) -> tuple[bool, int, int]:
    for page_index, page in enumerate(update):
        for rule in rules:
            if page == rule[0] and rule[1] in update and page_index > (index := update.index(rule[1])):
                return False, page_index, index
            if page == rule[1] and rule[0] in update and page_index < (index := update.index(rule[0])):
                return False, page_index, index

    return True, -1, -1


def part1() -> int:
    rules, updates = parseInput()

    total = 0
    for update in updates:
        if is_update_valid(update, rules)[0]:
            total += update[int(len(update) / 2)]

    return total


def part2() -> int:
    rules, updates = parseInput()

    total = 0
    for update in updates:
        is_valid, i, j = is_update_valid(update, rules)
        if is_valid:
            continue

        while not is_valid:
            update[j], update[i] = update[i], update[j]
            is_valid, i, j = is_update_valid(update, rules)

        total += update[int(len(update) / 2)]

    return total


if __name__ == '__main__':
    print(f"part1: {part1()}")
    print(f"part2: {part2()}")
