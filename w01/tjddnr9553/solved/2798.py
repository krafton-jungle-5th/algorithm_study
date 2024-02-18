def solution():
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    answer = 0

    # 3중 for문
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                total = numbers[i]+numbers[j]+numbers[k]
                if total <= M:
                    # 결과중 최대값 찾아내기
                    answer = max(answer, total)

    print(answer)


solution()