n =int(input())

body_list = []
volume_count_list = []

for i in range(n):
    w, h = map(int, input().split())
    body_list.append((w, h))
    
def volume(num):
    volume_count = 0
    for j in range(n):
        if body_list[num][0] < body_list[j][0] and body_list[num][1] < body_list[j][1]:
            volume_count += 1
    return volume_count + 1

for k in range(n):
    result = volume(k)
    volume_count_list.append(result)
    
print(*volume_count_list)