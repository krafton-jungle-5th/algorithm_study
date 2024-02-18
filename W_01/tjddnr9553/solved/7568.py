def solution():
    N = int(input())
    info_list = []
    rank_list = [0] * N
    
    for i in range(N):
        x, y = map(int, input().split())
        info_list.append((x, y))
    
    for i in range(N):
        rank = 1
        for j in range(N):
            if info_list[i][0] < info_list[j][0] and info_list[i][1] < info_list[j][1]:
                rank += 1
        rank_list[i] = rank
    
    for rank in rank_list:
        print(rank)


solution()