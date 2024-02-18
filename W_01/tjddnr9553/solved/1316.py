# 풀지 못해서 python 슬라이싱 참고했습니다.
def solution():
    n = int(input())
    count = n

    for i in range(0, n):
        word = input()
        for j in range(0, len(word)-1):
            if word[j] == word[j+1]:
                pass
            elif word[j] in word[j+1:]:
                count -= 1
                break

    print(count)


solution()
