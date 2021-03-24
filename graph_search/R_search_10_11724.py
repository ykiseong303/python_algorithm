'''
분류 : DFS & BFS
문제 : 연결요소의 개수 (백준 11724)
작성일자 : 2021.03.24
'''

# 목적 : 연결요소의 개수를 구한다 
# 접근 : dfs, bfs를 이용하여 그래프를 탐색한다 
#       입력은 무조건 sys로 받기
#       방문처리는 리스트의 인덱스를 0또는 1로 처리하기 (속도차이 거의 9배)

import sys
# 파이썬의 재귀 한계 정의
sys.setrecursionlimit(10000)

def dfs(start) : 
    global cnt
    visited[start] = 1
    cnt +=1 
    for i in range(1,N+1) : 
        if shape[start][i] == 1 and visited[i] == 0 : 
            dfs(i)

N, M = map(int, sys.stdin.readline().rstrip().split())
# 방문처리를 0으로 이루어진 리스트의 1로 처리
visited = [0] * (N+1)
shape = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M) : 
    x, y = map(int, sys.stdin.readline().rstrip().split())
    shape[x][y] = 1
    shape[y][x] = 1
count = 0
cnt = 0
answer = []
# shape의 실제 값 행렬부터 실행하기
for i in range(1,N+1) : 
    # 첫번째 i가 방문되지 않았으면 dfs를 수행하며
    # 연결된 노드를 방문처리하기 때문에 
    # 첫번째에서 연결된 노드는 무시하고 넘어감 
    if visited[i] == 0 : 
        dfs(i)
        count += 1
        answer.append(cnt)
        cnt = 0
print(count)
print(answer)