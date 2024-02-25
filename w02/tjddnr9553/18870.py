import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    num_list = list(map(int, input().split()))
    set_list = sorted(list(set(num_list)))
    dic = {}

    # 오름차순으로 정렬 및 중복제거가 됐기 때문에 i는 자신보다 작은 수의 개수랑 같다.
    for i in range(0, len(set_list)):
        dic[set_list[i]] = i

    # nun_list에서 한개씩 key값으로 검색 후 출력
    for j in num_list:
        print(dic[j])


solution()

import sys
input = sys.stdin.readline


def solution():
    N = int(input())
    num_list = list(map(int, input().split()))
    set_list = list(set(num_list))
    count_list = [0]*N

    for i in range(0, N):
        for j in range(0, len(set_list)):
            if num_list[i] > set_list[j]:
                count_list[i] += 1

    # 리스트 원소나 문자열 각각의 문자를 한 칸 씩 띄운 후(공백) 출력
    print(*count_list)


solution()
