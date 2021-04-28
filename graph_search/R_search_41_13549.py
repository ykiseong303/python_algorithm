'''
분류 : DFS & BFS
문제 : 숨바꼭질 (백준 13549)
작성일자 : 2021.04.28
'''

# 목적 : A>B가 되는 최소 연산횟수
# 접근 : 현재위치에서 3가지 연산에 대해 수행한다(bfs)
# 구현 : 1. 세가지 연산의 가중치가 모두 동일하지 않으므로 가중치가 낮은 것부터 수행
#       > *2는 연산의 변화가 없으므로 *2를 할때마다 큐의 제일 왼쪽으로 append시킨다
#       그러면 큐에서 *2의 연산만 먼저 실행되므로, 가장 빠른 연산횟수를 출력할 수 있다
#       예를 들어 4 > 6의 경우 4 > 3 > 6이므로 1번만 수행하면 됨


import sys
from collections import deque 

MAX= 100001
visit = [0] * 100001
result = [0] * 100001

n, k = map(int, input().split())
q = deque([(n)])
ans = 0
# visit[n] = 1 
while q :
    x = q.popleft()
    if x == k : 
        ans = result[x]
        break

    if x*2<MAX and visit[x*2] == 0 : 
        visit[x*2] = 1
        result[x*2] = result[x]
        q.appendleft((x*2))
    if x-1>=0 and visit[x-1] == 0 : 
        visit[x-1] = 1
        result[x-1] = result[x]+1
        q.append((x-1))
    if x+1<MAX and visit[x+1] == 0 :
        visit[x+1] = 1
        result[x+1] = result[x]+1
        q.append((x+1))

print(ans)