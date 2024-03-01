def square(x, y, n):
    global white, blue
    color = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                square(x, y, n//2)
                square(x, y + n//2, n//2)
                square(x + n//2, y, n//2)
                square(x + n//2, y + n//2, n//2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0

square(0, 0, N)
print(white, blue, sep='\n')