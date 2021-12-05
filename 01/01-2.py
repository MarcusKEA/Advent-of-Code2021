import io

with io.open('01\input.txt', encoding='utf-8') as o:
    input = o.read()
    input = input.split("\n")

try:
    input = [int(i) for i in input]

except:
    print("error")
input.pop()
cnt = 0




for i in range(len(input)):
    a = input[i:i+3]
    a = [int(i) for i in a]
    a = sum(a)
    b = input[i+1:i+4]
    b = [int(i) for i in b]
    b = sum(b)
    if a < b:
        cnt += 1


print("Cnt: ",cnt)
