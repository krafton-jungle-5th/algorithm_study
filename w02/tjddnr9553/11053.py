import sys
input = sys.stdin.readline


def solution():
    # 수열 개수 입력
    n = int(input())
    arr = list(map(int, input().strip().split()))
    
    # dp 테이블 1로 초기화
    dp = [1] * len(arr)

    # 문제를 잘못이해함(꼭 배수로 증가할 필요는 없음/ 그냥 증가하는 수열이기만 하면 됨)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


solution()
