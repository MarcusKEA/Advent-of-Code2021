import io

def problem1(l):
    depth = 0
    horizontal = 0
    for i in l:
        if i[0] == "f":
            horizontal += int(i[-1])
        if i[0] == "u":
            depth -= int(i[-1])
        if i[0] == "d":
            depth += int(i[-1])

    return depth * horizontal

def problem2(l):
    depth = 0
    horizontal = 0
    aim = 0
    for i in l:
        if i[0] == "f":
            horizontal += int(i[-1])
            depth = depth + aim * int(i[-1])
        if i[0] == "u":
            aim -= int(i[-1])
        if i[0] == "d":
            aim += int(i[-1])

    return depth * horizontal

if __name__ == "__main__":
    with io.open('02\input', encoding='utf-8') as o:
        input = o.read().splitlines()
    print(problem1(input))
    print(problem2(input))