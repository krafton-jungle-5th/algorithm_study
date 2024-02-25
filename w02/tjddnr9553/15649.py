from itertools import permutations
import sys
input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    # 1 ~ N+1까지의 수에서 M개씩 순열로 생성
    num_list = list(permutations(range(1, N+1), M))

    for answer in num_list:
        print(*answer)


solution()
