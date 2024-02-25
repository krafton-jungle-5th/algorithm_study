n, k = map(int, input().split())

coin_list = [int(input()) for _ in range(n)]
coin_list.sort(reverse=True)

coin_count = 0
for coin in coin_list:
    coin_count += k // coin
    k = k % coin
    
print(coin_count)