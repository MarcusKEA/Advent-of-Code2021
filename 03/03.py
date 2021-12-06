import io

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def problem1(l:list):
    item = dict()
    gammaRate = []
    epsilonRate = []

    for i in range(12):
        thing = {i : []}
        item.update(thing)
    for i in l:
        for j in range(len(i)):
            item[j].append(i[j])
    
    for i in range(len(item)):
        item[i] = [int(i) for i in item[i]]
        ones = item[i].count(True)
        zeroes = item[i].count(False)
        
        if ones > zeroes:
            gammaRate.append(1)
            epsilonRate.append(0)
        else:
            gammaRate.append(0)
            epsilonRate.append(1)
    
    gammaRate = binatodeci(gammaRate)
    epsilonRate = binatodeci(epsilonRate)

    return gammaRate * epsilonRate

def problem2(l):
    return



if __name__ == "__main__":
    with io.open('03\input', encoding='utf-8') as o:
        input = o.read().splitlines()
    print(problem1(input))
    print(problem2(input))