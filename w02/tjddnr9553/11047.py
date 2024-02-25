import sys
input = sys.stdin.readline


def solution():
    coins = []
    count = 0

    N, K = map(int, input().split())

    # N개만큼 동전의 가치 입력
    for i in range(N):
        coins.append(int(input()))

    coins.sort(reverse=True)  # 내림차순 정렬

    for j in coins:
        count = count + (K//j)  # 필요한 코인수 count
        K = K % j  # 쓰고 남은 돈
        if (K <= 0):
            break

    print(count)


solution()
