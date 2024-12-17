from dataclasses import dataclass


@dataclass
class ProgramState:
    A: int
    B: int
    C: int
    PC: int
    output: list[int]


def parseInput():
    A, program = 0, []
    with open("input.txt") as f:
        for line in f:
            split_line = line.strip().split(': ')
            if split_line[0] == 'Register A':
                A = int(split_line[1])
            elif split_line[0] == 'Program':
                program = [int(it) for it in split_line[1].split(',')]

    return A, program


def run_program(A: int, program: list[int]) -> list[int]:
    state = ProgramState(A, 0, 0, 0, [])

    def lookup_combo_operand(operand: int) -> int:
        return [
            lambda: 0,
            lambda: 1,
            lambda: 2,
            lambda: 3,
            lambda: state.A,
            lambda: state.B,
            lambda: state.C,
        ][operand]()

    def adv(operand: int):
        state.A = state.A // (2 ** lookup_combo_operand(operand))
        state.PC += 2

    def bxl(operand: int):
        state.B = state.B ^ operand
        state.PC += 2

    def bst(operand: int):
        state.B = (lookup_combo_operand(operand) % 8) & 0b111
        state.PC += 2

    def jnz(operand: int):
        if state.A == 0:
            state.PC += 2
            return

        state.PC = operand

    def bxc(_):
        state.B = state.B ^ state.C
        state.PC += 2

    def out(operand: int):
        state.output.append(lookup_combo_operand(operand) % 8)
        state.PC += 2

    def bdv(operand: int):
        state.B = state.A // (2 ** lookup_combo_operand(operand))
        state.PC += 2

    def cdv(operand: int):
        state.C = state.A // (2 ** lookup_combo_operand(operand))
        state.PC += 2

    opcodes = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]

    while state.PC < len(program) - 1:
        opcodes[program[state.PC]](program[state.PC + 1])

    return state.output


def compute_step(A: int) -> int:
    """
    Specific to my input. I deduced it by reverse-engineering the program from my input.
    TODO: Refactor to execute a part of the program, making this algorithm functional for any input.
    """
    B = (A % 8) & 0b111
    B ^= 2
    C = A // (2 ** B)
    B ^= 3
    B ^= C

    return B % 8


def find_original_a(a: int, cursor: int, program: list[int]) -> int | None:
    if cursor >= len(program):
        return a >> 3 if run_program(a >> 3, program) == program else None

    possibilities = [potential_a for potential_a in range(8) if compute_step(a | potential_a) == program[-(cursor+1)]]
    for possibility in possibilities:
        if (r := find_original_a(((a | possibility) << 3), cursor + 1, program)) is not None:
            return r

    return None


if __name__ == '__main__':
    p1_A, p = parseInput()

    print(f"part1: ", end='')
    print(*run_program(p1_A, p), sep=',')

    print(f"part2: {find_original_a(0, 0, p)}")
