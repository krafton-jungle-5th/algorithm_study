n, k = map(int, input().split())

coins = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0

for coin in coins:
    if coin > k:
        continue
    
    cnt += k // coin
    k %= coin
    
    if k == 0:
        break

print(cnt)
    