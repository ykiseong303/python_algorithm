'''
분류 : DFS & BFS
문제 : 다리만들기 (백준 2146)
작성일자 : 2021.04.25
'''

# 목적 : 섬과 섬을 연결하는 최소다리길이 출력
# 접근 : 섬을 구분하여 번호를 부여하고
#       각 섬에서 조건에 맞는(바다에 인접한) 모든 좌표에서 다른 섬까지 확장하는 최단경로를 저장
#       인간은 한번에 섬을 구분할 수 있지만 CT적인 면에서는 섬의 구분이 필요함
#       CT적인 접근으로 바라보는 연습필요

import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(x,y,name) : 
    visit[x][y] = name # 현재위치에 번호를 부여
    q = deque([(x,y)])
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            # 연결요소를 모두 찾아 같은 번호를 부여
            if (0<=nx<N and 0<=ny<N) :
                if shape[nx][ny] == 1 and visit[nx][ny] == 0 : 
                    visit[nx][ny] = name 
                    q.append((nx,ny))

def bfs2(num) : 
    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N : 
                # 이동하는 위치가 바다이고, 방문한적이 없는 경우라면
                if shape[nx][ny] == 0 and visit2[nx][ny] == 0 :
                    visit2[nx][ny] = visit2[x][y] + 1
                    q.append((nx,ny)) 
                # 이동하는 위치가 육지이고, 현재 섬과 다른 섬이라면 
                if shape[nx][ny] == 1 and visit[nx][ny] != num : 
                    # print("yes",visit2[x][y])
                    return visit2[x][y] - 1
        # for v in visit2 : 
        #     print(*v)

N = int(input())
shape = [list(map(int, input().split()))for _ in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
visit = [[0]*N for _ in range(N)] # 각 섬별 번호를 표시하기 위한 리스트 생성
name = 1
# 1. 각 섬에 번호 부여하기 (연결요소를 찾아 번호부여)
for i in range(N) : 
    for j in range(N) : 
        if shape[i][j] == 1 and visit[i][j] == 0 : 
            bfs(i,j,name)
            name += 1
res, ans = 0,0
ans = sys.maxsize # ans에 최대 정수값을 부여
for k in range(1,name) : 
    # k섬의 모든 좌표를 넣을 q생성
    q = deque()
    visit2 = [[0]*N for _ in range(N)] # 다른 섬으로의 경로를 표현하기 위한 리스트 생성
    for i in range(N) : 
        for j in range(N) : 
            if shape[i][j] == 1 and visit[i][j] == k : 
                q.append((i,j))
                visit2[i][j] = 1
    res = bfs2(k)
    # print(res)
    ans = min(ans,res)
print(ans)

'''import sys 
from collections import deque
input = sys.stdin.readline

def find_other(real_bay) : 
    min_route = 0
    while real_bay : 
        visit_sea = [[0]*N for _ in range(N)]
        x, y = real_bay.popleft()
        q = deque([(x,y)])
        visit_sea[x][y] = 1
        while q :
            x1, y1 = q.popleft()
            for i in range(4) : 
                nx, ny = x1+dx[i], y1+dy[i]
                if (0<=nx<N and 0<=ny<N) and [nx,ny] not in real_bay : 
                    if visit_sea[nx][ny] == 0 : 
                        visit_sea[nx][ny] = visit_sea[x][y] + 1
                        q.append((nx,ny))


def find_bay(bay) : 
    real_bay = deque()
    while bay : 
        x, y = bay.popleft()
        for i in range(4) : 
            if (0<=nx<N and 0<=ny<N) and shape[nx][ny] == 0 :
                real_bay.append((x,y))
    find_other(real_bay)
def bfs(x1,y1) : 
    bay = deque()
    if shape[x1][y1] == 1 : 
        visit[nx][ny] = 1
        bay.append((x1,y1))
        q = deque([(x1,y1)])
        while q :
            x, y = q.popleft()
            for i in range(4) :
                nx, ny = x+dx[i], y+dy[i]
                if (0<=nx<N and 0<=ny<N) and shape[nx][ny] == 1 :
                    if visit[nx][ny] == 0 : 
                        visit[nx][ny] = 1
                        bay.append((nx,ny))
                        q.append((nx,ny))
        find_bay(bay)
        return True 
    else : 
        return False

N = int(input())
shape = [list(map(int, input().split))for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visit = [[0]*N for _ in range(N)]
for i in range(N) : 
    for j in range(N) : 
        if bfs(i,j) == True : 
            pass
'''