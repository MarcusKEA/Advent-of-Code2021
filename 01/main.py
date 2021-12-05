import io
cnt = 0

with io.open('01\input.txt', encoding='utf-8') as o:
    input = o.read()
    input = input.split("\n")

for i in range(len(input)):
    if input[i-1] < input[i]:
        cnt += 1
print(cnt)