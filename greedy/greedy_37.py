'''
분류 : 그리디 알고리즘
문제 : 카드 합체 놀이 (백준 15903)
작성일자 : 2021.03.14
'''

# 여러 장의 카드 중 두장씩 카드를 합쳐서 총합 만들기
## 목적 : 최소의 총합 만들기
## 접근 : 제일 작은것 두개만 뽑아서 합하고 다시 넣기 
##       우선순위 큐로도 구현 가능
##       정렬로 풀면 232ms, 최소힙으로 풀면 84ms로 속도차이가 많이 남
import sys
import heapq

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
# 최소힙으로 변경
heapq.heapify(num)
index = 0
while index < M : 
    # 최소힙의 루트노드를 연달아 두개 pop
    a = heapq.heappop(num)
    b = heapq.heappop(num)
    c = a + b
    d = a + b
    # 계산 후 다시 push
    heapq.heappush(num,c)
    heapq.heappush(num,d)
    index += 1
print(sum(num))
'''
import sys 

N, M = map(int, input().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
index = 0
while index < M : 
    num.sort()
    x = num[0]
    y = num[1]
    num[0] = x+y
    num[1] = x+y
    index+=1
print(sum(num))
'''