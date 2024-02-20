def solution():
    N = int(input())

    num_list = [0, 1]
    num = 0
    for i in range(0, N-1):
        num = num_list[i]+num_list[i+1]
        num_list.append(num)

    answer = num_list[N]

    print(answer)


solution()
