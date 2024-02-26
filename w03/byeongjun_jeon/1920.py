import sys
input = sys.stdin.readline

# 시간 초과
# O(n2)
# n = int(input())

# arr = list(map(int, input().split()))

# m = int(input())

# arr2 = list(map(int, input().split()))

# for i in arr2:
#     if i in arr:
#         print(1)
#     else:
#         print(0)

# 이분탐색을 사용해야 할듯
n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())

arr2 = list(map(int, input().split()))

def binary_search(start, end, target):
    
    # 모든 요소 탐색을 마쳤는데도 일치하는 값이 없으면
    if start > end:
        print(0)
        return

    mid = (start+end)//2

    #배열의 절반에 위치한 값이 result와 같으면
    if arr[mid] == target:
        print(1)
        return
    # 만약 result가 더 크면
    elif arr[mid] < target:
        binary_search(mid + 1, end, target)
    # 만약 result가 더 작으면
    elif arr[mid] > target:
        binary_search(start, mid - 1, target)

for i in arr2:
    binary_search(0, len(arr)-1, i)


