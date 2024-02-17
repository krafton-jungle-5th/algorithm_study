# Sol 1
n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())), reverse=True)

max_sum = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            current_sum = numbers[i] + numbers[j] + numbers[k]
            
            if current_sum <= m:
                max_sum = max(max_sum, current_sum)
                if max_sum == m:
                    break

print(max_sum)

# Sol 2 (Chat GPT)
from itertools import combinations

def find_nearest_blackjack_sum(cards, target_sum):
    max_sum = 0

    # 카드 중 3장을 선택하는 모든 조합을 확인
    for combination in combinations(cards, 3):
        current_sum = sum(combination)

        # 현재 합이 기존 최대 합보다 크고, 타겟 합 이하인 경우 갱신
        if current_sum > max_sum and current_sum <= target_sum:
            max_sum = current_sum

    return max_sum

# 입력 받기
n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 결과 출력
result = find_nearest_blackjack_sum(cards, m)
print(result)
