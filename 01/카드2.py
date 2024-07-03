from collections import deque

N = int(input())
# deque 는 양끝에서 추가삭제 O(1)
cards = deque()

for i in range(1, N+1):
    cards.append(i)
# 1장보다 많을때 까지 반복
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
        
print(cards.pop())
