from collections import deque
import sys
input = sys.stdin.readline


def solution():
    num_list = deque()
    # N장의 카드 받기
    N = int(input())
    # N장의 카드 배열 만들기
    for i in range(1, N+1):
        num_list.append(i)

    # index[1]의 값을 배열에 추가하고, [0:2] 0~1번방 요소를 삭제
    for j in range(0, N-1):
        num_list.append(num_list[1])
        num_list.popleft()
        num_list.popleft()

    print(num_list[0])


solution()