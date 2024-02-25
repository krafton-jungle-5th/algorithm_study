n = int(input())
arr = list(map(int, input().split()))

l = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i] and l[i] < l[j] + 1:
            l[i] = l[j] + 1

print(max(l))




