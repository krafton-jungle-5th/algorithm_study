n, m = map(int, input().split())

card_list = list(map(int, input().split()))
card_list.sort()

min_diff = float('inf')     # 무한대로 초기화
result = 0

for a in range (n):
    for b in range (a + 1, n):
        for c in range (b + 1, n):
            sum = card_list[a] + card_list[b] + card_list[c]
            diff = m - sum
            if 0 <= diff < min_diff:
                min_diff = diff
                result = m - min_diff

print(result)