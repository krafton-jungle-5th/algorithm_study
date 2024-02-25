n = int(input())
cnt = 0

for _ in range(n):  
    data = input()
    chars = []

    for idx, char in enumerate(data):
        if idx == 0 or char != data[idx-1]:
            if char not in chars:
                chars.append(char)
            else:
                break
    else:
        cnt += 1

print(cnt)