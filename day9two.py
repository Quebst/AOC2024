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
    fblock = comptwo(fblock)
    #print(f"fblock is {fblock}")

    checksum = 0
    index = 0
    while index < len(fblock) - 1:
        if fblock[index] != '.':
            checksum += index * fblock[index]
            index += 1
        else:
            index += 1
        

    print(f"Total checksum is {checksum}")

def comptwo(fblock):
    top = len(fblock) - 1

    # Find empty blocks [start, size]
    empties = []
    last = 9

    for i in range(len(fblock)):
        if fblock[i] == '.' and last != '.':
            size = 1
            start = i
        elif fblock[i] == '.':
            size += 1
        elif last == '.':
            empties.append([start, size])
        else:
            pass
        last = fblock[i]
    
    #print(f"Empies is {empties}")
    #print(f"fblock start is {fblock}")


    # top > 0
    while top > 0:

        if fblock[top] == '.':
            top -= 1
        else:
            # find chunk of top file [start, size]
            num = fblock[top]
            size = 0
            while fblock[top] == num:
                size += 1
                top -= 1
            # top + 1 is start, size is size
            for k in range(len(empties)):
                if empties[k][1] >= size and empties[k][0] < top + 1:
                    for j in range(size):
                        fblock[empties[k][0] + j] = fblock[top + 1 + j]
                        fblock[top + 1 + j] = '.'
                    empties[k] = [empties[k][0] + size, empties[k][1] - size]
                    break

            
    return fblock



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