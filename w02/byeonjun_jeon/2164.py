# 시간이 좀 길게나옴
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
cards = deque()
for i in range(1, n+1):
    cards.append(i)

while len(cards) != 1:
    cards.popleft()
    cards.rotate(-1)
print(*cards)

# 다른방법으로 푼 사람 있는지 물어보기