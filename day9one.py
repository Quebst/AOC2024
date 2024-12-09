raw_data = """2333133121414131402"""

# data empty alternate, bits as id 
# 00...111...2...333.44.5555.6666.777.888899

def main():
    print("Starting Main")
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    #lines = read_data.splitlines()
    line = []
    for c in read_data:
        line.append(int(c))

    fblock = transform(line)
    #print(f"fblock is {fblock}")
    fblock = comp(fblock)
    #print(f"fblock is {fblock}")

    checksum = 0
    index = 0
    while True:
        checksum += index * fblock[index]
        index += 1
        if fblock[index] == '.':
            break

    print(f"Total checksum is {checksum}")


def comp(fblock):
    bottom = 0
    top = len(fblock) - 1

    while bottom < top:
        while fblock[bottom] != '.':
            bottom += 1
        while fblock[top] == '.':
            top -= 1
        
        if bottom < top:
            temp = fblock[bottom]
            fblock[bottom] = fblock[top]
            fblock[top] = temp
        else:
            break

    return fblock


def transform(line):
    fblock = []

    index = 0
    files = True

    while line:
        if files:
            quantity = line.pop(0)
            for i in range(quantity):
                fblock.append(index)
            index += 1
            files = False
        else:
            quantity = line.pop(0)
            for i in range(quantity):
                fblock.append('.')
            files = True

    return fblock
    

if __name__ == "__main__":
    main()