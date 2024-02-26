n = int(input())
arr = list(map(int, input().split(" ")))

result = 0
for i in arr:
    count = 0
    if i == 1 or i == 0:
        continue
    for j in range(2, int(i/2+1)):
        if i%j == 0:
            count = 1
            break
    if count == 0:
        result += 1

print(result)