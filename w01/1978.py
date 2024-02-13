import math


n = int(input())
count = 0

data = list(map(int, input().split()))

for i in range(n):
    if data[i] == 1:
        continue
    elif data[i] == 2:
        count += 1
    elif data[i] % 2 == 0:
        continue
    else:
        is_prime = True
        for j in range(3, int(math.sqrt(data[i])) + 1):
            if data[i] % j == 0:
                is_prime = False
                continue
        if is_prime:
            count += 1


print(count)

