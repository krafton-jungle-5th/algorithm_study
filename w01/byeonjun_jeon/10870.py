n = int(input())

if n == 0:
    print(0)
    quit()
if n == 1:
    print(1)
    quit()

arr = [0,1]

# 피보나치 수 
for i in range(n-1):
    num = arr[-1] + arr[-2]
    arr.append(num)

print(arr[-1])

