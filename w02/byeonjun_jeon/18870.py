import sys
input = sys.stdin.readline

n = int(input())
arr_input = list(map(int, input().split()))
sort_list = sorted(set(arr_input))

dic = {sort_list[i] : i for i in range(len(sort_list))}

# .index는 선형 탐색을 함으로 O(n^2)가 되버려 시간초과가 뜬다
# 이를 해결하기 위해 dict 자료형에 index를 저장해놓고 사용하면 해결
for i in arr_input:
    print(dic[i], end=" ")

    



