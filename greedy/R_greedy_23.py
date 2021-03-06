'''
분류 : 그리디 알고리즘
문제 : 카드 정렬하기 (백준 1715번)
작성일자 : 2021.03.04
'''

# 목적 : 카드를 합치는 횟수의 연산을 최소화
# 접근 : 카드의 수가 적은 것부터 합쳐나가기

## 힙으로 우선순위 큐를 사용하여 풀이한다
import heapq
import sys

N = int(input())
cards = []
for _ in range(N) : 
    cards.append(int(sys.stdin.readline().rstrip()))

# cards 리스트를 최소 힙 구조로 변경
card_deck = []
for card in cards : 
    heapq.heappush(card_deck, card)

# 카드가 딱 한종류 뿐이면 비교할 필요 없으므로 0 
if len(card_deck) == 1 : 
    print(0)
else : 
    # 제일 작은 두 수의 합이 계속 힙에 추가 되도록 구현
    result = 0
    while len(card_deck) > 1 : 
        temp_x = heapq.heappop(card_deck)
        temp_y = heapq.heappop(card_deck)
        result += temp_x + temp_y
        heapq.heappush(card_deck, temp_x+temp_y)
    print(result)



'''
# 직접 풀은 풀이가 왜 틀렸는지는 아직 모르겠음
import sys
N = int(input())
cards = []
for _ in range(N) : 
    cards.append(int(sys.stdin.readline().rstrip()))
cards.sort()
i = len(cards)
total = 0
for card in cards : 
    total = total + card*i
    i -= 1
if len(cards) == 1: 
    print(0)
else : 
    print(total-cards[0])
'''
