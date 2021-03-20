'''
분류 : DFS & BFS
문제 : 미로탈출 (이코테 2번)
작성일자 : 2021.03.20
'''

# 목적 : 목표지점까지 도달하는 데 이동하는 칸의 최소 개수 
# 접근 : 그리디 적인 방식과 유사
#       현재 노드에서 갈 수 있는 곳을 모두 방문하고, 거리를 표시하기 
#       bfs를 사용(간선의 비용이 모두 같을때 최단거리 탐색에 사용)
#       현재 문제에서도 상하좌우로 연결된 모든 노드의 거리가 1로 동일함

from collections import deque

def bfs(x,y) : 
    myQue = deque([(x,y)])
    while myQue : 
        x,y = myQue.popleft()
        for i in range(4) : 
            # 상, 하, 좌, 우의 값을 한번에 넣어도 되지만
            # 각각의 경우에 대해 미리 검사를 하고 큐에 넣기 위함
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M : 
                continue
            if shape[nx][ny] == 0 : 
                continue
            # 다른 노드가 방문했을 수도 있으므로 
            # 길인 경우에만 갈 수 있도록 (해당 노드를 처음 방문한 경우에만)
            if shape[nx][ny] == 1 :
                # 직전 노드의 값에 1을 더해서 현재까지의 경로를 표시 
                shape[nx][ny] = shape[x][y] + 1 
                myQue.append((nx,ny))
        # 목표 지점까지 도달한 경우 더 이상의 탐색 중지
        if nx == N-1 and ny == M-1 : 
            break
        for s in shape : 
            print(*s)
        print("\n")
    return shape[N-1][M-1]


N, M = map(int, input().split())
shape = []
for _ in range(N) : 
    shape.append(list(map(int, input())))
# 방향 전환을 위한 커맨드 

dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(bfs(0,0))