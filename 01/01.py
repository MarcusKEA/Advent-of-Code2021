import io

def problem1(l):
    return [l[i] > l[i-1] for i in range(1, len(l))].count(True)

def problem2(l):
    lst = [sum(l[i-2:i+1]) for i in range(2, len(l))]
    return problem1(lst)

if __name__ == "__main__":
    with io.open('01\input.txt', encoding='utf-8') as o:
        input = o.read().splitlines()
        input = [int(i) for i in input]
    print(problem1(input))
    print(problem2(input))