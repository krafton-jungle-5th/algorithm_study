from collections import deque

n = int(input())
cards = deque(range(1, n+1))

while len(cards) > 1:
    cards.popleft()  
    top_card = cards.popleft() 
    cards.append(top_card)

print(*cards)
