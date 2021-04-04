'''
분류 : DFS & BFS
문제 : 촌수계산 (백준 2644)
작성일자 : 2021.04.04
'''

# 목적 : 두 사람의 촌수 관계 구하기 
# 접근 : 목적지까지 도달하는 최단 경로 (간선의 비용이 1로 동일)
#       연결된 정점관의 관계를 매트릭스에 표현
#       방문표시를 하고, 큐를 다 돌았는데도 발견하지 못하면 -1을 출력

from collections import deque

def bfs(s) : 
    # 현재 위치를 방문처리
    visit[s] = 1
    q = deque([(s,0)])
    while q : 
        x, cnt = q.popleft()
        if x == e : 
            # print(cnt)
            return cnt
        for i in range(n+1) : 
            if shape[x][i] == 1 and visit[i] == 0: 
                visit[i] = 1 
                q.append((i,cnt+1))
    return -1 

n = int(input())
s, e = map(int, input().split())
m = int(input())
shape = [[0]*(n+1) for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(m) : 
    x, y = map(int, input().split())
    shape[x][y] = 1
    shape[y][x] = 1
print(bfs(s))