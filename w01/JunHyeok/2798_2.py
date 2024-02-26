n, target = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
lst = []

def func(start, idx):
    global res
    global vect
    global target
    global arr
    global n

    if idx == 3:
        sum = 0
        for i in lst:
            sum += i
            # print(str(i) + " ", end = " ") 각 단계별로 어떤 조합을 사용하는지 보고싶으면 주석을 해제하세요
        # print("Sum : " + str(sum)) 각 단계별로 어떤 조합을 사용하는지 보고싶으면 주석을 해제하세요
        if sum <= target:
            res = max(res, sum)
        return

    for i in range(start, n):
        lst.append(arr[i])
        func(i + 1, idx + 1)
        lst.pop()

func(0, 0)
print(res)
