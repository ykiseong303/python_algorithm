'''
분류 : DFS & BFS
문제 : 불! (백준 4179)
작성일자 : 2021.05.05
'''

# 목적 : J가 탈출할 수 있는 최단시간 출력
# 접근 : 탈출 문제와 동일 (BFS)
#       불과 J의 위치를 따로 저장하고, 
#       불을 먼저 혹은 J를 먼저 이동시킨다 
#       핵심은 불과 J를 한번씩 번갈아가며 이동시키는 것, 큐의 긺이만큼만 탐색하도록 설계
#       종료조건 : q에 더 이상 데이터가 없거나(더 이상 이동 불가) 목적지에 도달한 경우
#       최단거리(방문처리) 구현 : 현재위치 + 1
#       J가 처음부터 탈출가능 위치에 있는지확인이 필요함

import sys 
from collections import deque 
input = sys.stdin.readline

def bfs() : 
    while q : 
        lenq = len(q) 
        while lenq : 
            x, y = q.popleft()
            # print("x,y",x,y)
            # if shape[x][y] != '#' and (x == R-1 or y == C-1) : 
            #     print(visit[x][y])
            #     return 
            for i in range(4) : 
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or ny<0 or nx>=R or ny>=C : 
                    print(visit[x][y])
                    return
                if (0<=nx<R and 0<=ny<C) and shape[nx][ny] == '.' :
                    if visit[nx][ny] == 0 : 
                        # print("nx,ny",nx,ny)
                        visit[nx][ny] = visit[x][y] + 1
                        q.append((nx,ny))
            # print("\n")
            # for v in visit: 
            #     print(*v)
            lenq -= 1
        fire()
        # print("\n")  
        # for s in shape : 
        #     print(*s)

    print("IMPOSSIBLE")
def fire() : 
    len_fq = len(fq)
    while len_fq : 
        x, y =fq.popleft()
        # print(x,y)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0<=nx<R and 0<=ny<C) and shape[nx][ny] == '.' : 
                shape[nx][ny] = 'F'
                fq.append((nx,ny))
        len_fq -= 1


R, C =  map(int, input().split())
shape = [list(input().rstrip())for _ in range(R)]
visit = [[0]*C for _ in range(C)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
q, fq = deque(), deque()
# 현재 J와 F의 위치를 기록
for i in range(R) : 
    for j in range(C) : 
        if shape[i][j] == 'J' : 
            q.append((i,j))
            shape[i][j] = '.'
            visit[i][j] = 1
        if shape[i][j] == 'F' : 
            fq.append((i,j))

fire()
# for s in shape : 
#     print(*s)
bfs()