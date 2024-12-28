import time
from sys import exit

# 216584205979245

AMOUNTS = [
    1,
    8,
    64,
    512,
    4096,
    32768,
    262144,
    2097152,
    16777216,
    134217728,
    1073741824,
    8589934592,
    68719476736,
    549755813888,
    4398046511104,
    35184372088832,
    281474976710656,
]

program = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 2, 5, 5, 3, 0, 0, 0]


def main():
    start_time = time.time()
    print("Starting Main")

    k = 15
    result = 0
    guess = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 2, 5, 1, 1, 1, 0]

    next_level(k, result, guess)
    print(f"Time is {time.time() - start_time}")


def next_level(k, result, guess):

    while program[k + 1] == guess[k + 1]:

        if guess[k] == program[k]:
            if k == 0:
                print(f"{guess} is guess \n{program} is program")
                print(f"Result is {result}")
                exit()
            else:
                next_level(k - 1, result, guess)

        result = result + AMOUNTS[k]
        guess = test_a(result, program)


def test_a(original_a, program):
    rega = original_a
    regb = 0
    regc = 0

    output = []

    instruct = 0
    while instruct < len(program) - 2:
        opcode = program[instruct]
        operand = program[instruct + 1]

        match opcode:
            case 0:
                rega = rega // (2 ** combo(operand, rega, regb, regc))
            case 1:
                regb = regb ^ operand
            case 2:
                regb = (combo(operand, rega, regb, regc)) % 8
            case 3:
                if rega != 0:
                    instruct = operand - 2
            case 4:
                regb = regb ^ regc
            case 5:
                output.append(combo(operand, rega, regb, regc) % 8)
            case 6:
                regb = rega // (2 ** combo(operand, rega, regb, regc))
            case 7:
                regc = rega // (2 ** combo(operand, rega, regb, regc))

        instruct += 2

    output.append(0)
    output.append(0)
    return output


def combo(operand, rega, regb, regc):
    match operand:
        case 0:
            return 0
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 3
        case 4:
            return rega
        case 5:
            return regb
        case 6:
            return regc
        case _:
            return "Not a valid combo opcode"


if __name__ == "__main__":
    main()
