n = int(input())

result = 0

for i in range(n):
    strArr = list(input())
    resultArr = []
    flagArr = []
    for i in range(len(strArr)):
        # 배열에 없으면 추가
        if strArr[i] not in resultArr:
            resultArr.append(strArr[i])
        # 배열에 있으면 
        else:
            # 바로 전 문자열과 비교
            flagArr.append(strArr[i] == strArr[i-1])
    
    # 만약 조건과 다른 case가 있다면 continue
    if flagArr.count(False) > 0:
        continue

    result += 1

print(result)

# 신박하다고 생각된 다른사람의 코드
N = int(input())

count = N

for i in range(N) :
    word = input() 
    for j in range(0,len(word)-1) :
        if word[j] == word[j+1] :
            pass
        elif word[j] in word[j+1:] :
            count -=1
            break
        
print(count) 


