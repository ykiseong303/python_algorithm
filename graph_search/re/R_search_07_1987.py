'''
분류 : DFS & BFS
문제 : 알파벳 (백준 1987)
작성일자 : 2021.07.05
'''

# 목적 : 전진할 수 있는 최대 칸수 출력
# 접근 : 한번 방문했던 위치를 다시 방문할 수 없으므로,
#       한 방향으로 갈 수 있을 때까지(계속 dfs) 전진
#       더 이상 진행할 수 없을때 직전 위치로 돌아와서 다른 방향으로 진행(방문기록을 없야고)

# bfs 풀이 

import sys 
from collections import deque 
input = sys.stdin.readline

def bfs() : 
    # print(k)
    res = 1
    q = set([(0,0,shape[0][0])]) # 방문리스트의 중복방지를 위해 set로 설정
    # 또한 각각의 큐에 방문리스트를 개별적으로 확인
    while q : 
        x,y,visited = q.pop() 
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C : 
                if shape[nx][ny] not in visited : # 현재큐에서 다음 위치를 방문한적이 없다면
                    # 방문한적이 있는 곳이라면 해당 큐를 더이상 추가하지 않음
                    # 그럼에도 아직 다른 방향으로 진행중인 큐가 있기 때문에 모든 경우를 확인할 수 있음
                    next_visit = visited+shape[nx][ny]
                    q.add((nx,ny,next_visit))
                    res = max(res, len(next_visit))
    print(res)

R, C = map(int, input().split())
shape = [list(input().rstrip()) for _ in range(R)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
bfs()


# dfs + 백트래킹으로 풀이
'''import sys 
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x,y) : 
    global res, count 
    res = max(res, count)
    # visit[x] = 1
    for i in range(4) : 
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<R and 0<=ny<C : 
            if visit[shape[nx][ny]] == 0 : 
                visit[shape[nx][ny]] = 1 
                count += 1
                dfs(nx, ny)
                visit[shape[nx][ny]] = 0 
                count -= 1

R, C = map(int, input().split())
    # shape.append(list(map(ord, input().rstrip())))
shape = [list(map(lambda x : ord(x)-65, input().rstrip()))for _ in range(R)]
visit = [0] * 26
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit[shape[0][0]] = 1 # 첫 위치를 방문처리
res = 0
count = 0
dfs(0,0)
print(res+1)'''