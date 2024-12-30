import time

raw_data = """Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""


def main():
    start_time = time.time()
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    # lines = read_data.splitlines()
    rega = 729
    regb = 0
    regc = 0
    program = [0, 1, 5, 4, 3, 0]

    output = []

    instruct = 0
    while instruct < len(program):
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
                output.extend(str(combo(operand, rega, regb, regc) % 8) + ",")
            case 6:
                regb = rega // (2 ** combo(operand, rega, regb, regc))
            case 7:
                regc = rega // (2 ** combo(operand, rega, regb, regc))
        instruct += 2

    output = "".join(output)
    print(output)
    print(f"Time is {time.time() - start_time}")


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
