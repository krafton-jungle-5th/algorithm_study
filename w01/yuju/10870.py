num = int(input())
f_list = [0, 1]

for i in range(2, num+1):
    new = f_list[i-1] + f_list[i-2]
    f_list.append(new)

print(f_list[num])