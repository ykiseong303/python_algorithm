'''
분류 : DFS & BFS
문제 : 미로탈출 (백준 2178)
작성일자 : 2021.03.21
'''

# 목적 : 미로를 탈출하는 데 이동하는 칸의 최소갯수 출력
# 접근 : 모든 노드간의 간선의 비용이 같으므로 bfs를 이용하여 최단거리를 계산한다 

from collections import deque

def bfs(x,y) : 
    queue = deque([(x,y)])
    while queue : 
        a, b = queue.popleft()
        for i in range(4) : # 현재위치에서 상하좌우 4방향을 시도
            nx = a + dx[i] # 현재위치에 상, 하의 값을 입력
            ny = b + dy[i] # 현재위치에 좌, 우의 값을 입력

            if nx<0 or nx>=N or ny<0 or ny>=M : # 범위를 벗어나는 경우
                continue
            if shape[nx][ny] == 0 : # 길이 아닌 경우
                continue
            if shape[nx][ny] == 1 : # 다른 노드에 의해 값이 바뀔 수 있으므로 1
                queue.append((nx,ny)) # 조건을 통과한 노드를 큐에 다시 넣는다
                # 현재노드까지 걸린 비용을 표현하기 위해 직전노드 값 + 1
                shape[nx][ny] = shape[a][b] + 1 
    return shape[N-1][M-1]

N, M = map(int, input().split())
shape = []
for _ in range(N) : 
    shape.append(list(map(int, input())))

dx = [-1,1,0,0] # 상, 하를 표현하기 위한 커맨드
dy = [0,0,-1,1] # 좌, 우를 표현하기 위한 커맨드
print(bfs(0,0))