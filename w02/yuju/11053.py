n = int(input())
a = list(map(int, input().split()))

num = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            num[i] = max(num[i], num[j]+1)
            
print(max(num))