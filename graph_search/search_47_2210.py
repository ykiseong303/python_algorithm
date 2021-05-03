'''
분류 : DFS & BFS
문제 : 숫자판 점프 (백준 2210)
작성일자 : 2021.05.03
'''

# 목적 : 시작위치에서 5번 움직여서 만들 수 있는 모든 숫자의 경우의 수 출력
# 접근 : 임의의 모든 점(브루트포스)에서 5번만 움직여서 방문할 수 있는 모든 구간을 탐색
#       방문 기록을 남기면 숫자 조합이 범위가 제한되므로 (왔던곳으로 돌아가지 못함)
#       방문기록을 남기지 않음(5번이 되면 알아서 continue)

import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(x,y) : 
    global num,res
    visit[x][y] = 1
    q = deque([(x,y,str(shape[x][y]),0)])
    while q :
        x,y,val,cnt = q.popleft()
        if cnt == 5 : 
            # print(val)
            if num[int(val)] == 0 :
                # print(val) 
                num[int(val)] = 1
                res += 1
            continue
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            # if (0<=nx<5 and 0<=ny<5) and visit[nx][ny] == 0 : 
            #     visit[nx][ny] = 1
            #     q.append((nx,ny,val+str(shape[nx][ny]),cnt+1))
            if (0<=nx<5 and 0<=ny<5) : 
                q.append((nx,ny,val+str(shape[nx][ny]),cnt+1))                
shape = [list(map(int, input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
num = [0] * 1000001
res = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(5) : 
    for j in range(5) : 
        bfs(i,j)
        visit =[[0]*5 for _ in range(5)]
print(res)

