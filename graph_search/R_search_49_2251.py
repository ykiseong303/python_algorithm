'''
분류 : DFS & BFS
문제 : 물통 (백준 2251)
작성일자 : 2021.05.06
'''

# 목적 : x가 0일때, z의 값들을 오름차순으로 출력
# 접근 : 현재 x,y,z에서 갈 수 있는 6가지 경우에 대해 bfs를 수행
#       옮길 물통과 옮겨질 물통의 물의 양이 옮겨질 물통의 양보다 많은 경우
#       반대인 경우 
#       x, y 둘이 정해지면 z도 정해진 것이나 다름 없으므로 둘을 가지고 방문처리
#       z가 0이 될 수도 있음을 유의

import sys 
from collections import deque
input = sys.stdin.readline

def bfs(q) : 
    while q : 
        x, y, z = q.popleft()
        if visit[x][y] == 1 : 
            continue 
        visit[x][y] = 1 
        if x == 0 : ans[z] = 1
        if x+y > b : q.append((x+y-b,b,z))
        else : q.append((0,x+y,z))
        if x+z > c : q.append((x+z-c,y,c))
        else : q.append((0,y,x+z))
        if y+x > a : q.append((a,x+y-a,z))
        else : q.append((x+y,0,z))
        if y+z > c : q.append((x,y+z-c,c))
        else : q.append((x,0,y+z))
        if z+x > a : q.append((a,y,x+z-a))
        else : q.append((x+z,y,0))
        if z+y > b : q.append((x,b,y+z-b))
        else : q.append((x,y+z,0))


a, b, c = map(int, input().split())
visit = [[0]*201 for _ in range(201)]
ans = [0]*201

q = deque([(0,0,c)])
bfs(q)
res = []
for i in range(201) : 
    if ans[i] : 
        print(i, end=" ")