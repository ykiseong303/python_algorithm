'''
분류 : DFS & BFS
문제 : DSLR (백준 9019)
작성일자 : 2021.04.27
'''   

# 목적 : A>B가 되는 최소 연산내용 출력
# 접근 : 4가지 연산을 bfs를 수행 (시간줄이기가 핵심)
#       L, R 연산의 경우 리스트로 접근하면 안됌(시간초과)
#       >> 점화식을 통해 구현
##      매 연산마다 y와 비교함으로써 큐의 길이가 매우 커졌을 때의 연산횟수를 줄이기

import sys 
from collections import deque 

def bfs(start) : 
    q = deque()
    q.append([start,""])
    while q :
        x, result = q.popleft()

        dx = (x*2) % 10000
        if dx == y :
            return result +"D"
        elif visit[dx] == 0 :
            visit[dx] = 1 
            q.append([dx,result+"D"])
        
        sx = x-1 if x!=0 else 9999
        if sx == y : 
            return result +"S"
        elif visit[sx] == 0 :
            visit[sx] = 1
            q.append((sx,result+"S"))
        
        lx = x%1000 * 10 + x//1000 
        if lx == y : 
            return result +"L"
        elif visit[lx] == 0 :
            visit[lx] = 1
            q.append((lx,result+"L"))
        
        rx = x%10 * 1000 + x//10
        if rx == y :
            return result +"R"
        elif visit[rx] == 0 :
            visit[rx] = 1
            q.append((rx,result+"R"))



T = int(input())
while T : 
    x, y = map(int, input().split())
    visit = [0] * 10000 # A와 B는 10000미만이므로 10000까지 생성
    print(bfs(x))
    T -= 1 