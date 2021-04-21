'''
분류 : DFS & BFS
문제 : DFS와 BFS (백준 1260)
작성일자 : 2021.03.20
'''

# 목적 : 입력받은 그래프를 DFS와 BFS로 수행한 결과를 출력한다
# 접근 : 간선이 연결되는 두 정점만이 입력되므로 이를 매트릭스 상에 표현한다

from collections import deque 
 
def bfs(start) :    
    visited = [start]
    queue = deque([start]) 
    while queue : 
        x = queue.popleft()
        for i in range(N+1) : 
            if matrix[x][i] == 1 and i not in visited : 
                queue.append(i)
                visited += [i]
    return visited

def dfs(start,visited) : 
    visited += [start]
    for i in range(N+1) : 
        # 기준 정점에서 다음 정점으로 연결되어 있는지 확인
        # 그 정점 i가 방문되었는지 확인 (여기서는 matrix의 열번호와 같음)
        if matrix[start][i] == 1 and (i not in visited) : 
            dfs(i,visited)
    return visited 

def dfs_big (start, visited) : # 숫자가 큰 값부터 탐색하는 경우 
    visited += [start]
    for i in range(N, -1, -1) : # matrix의 열의 끝번호부터 탐색할 수 있도록  
        if matrix[start][i] == 1 and i not in visited : 
            dfs(i,visited)
    return visited

N,M,V = map(int, input().split())
# 노드가 1번부터이므로 편의를 위해 N+1개씩 생성
matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M) : 
    x, y = map(int, input().split())
    matrix[x][y] = 1
    # 반대편 정점을 같이 표기 
    matrix[y][x] = 1

print(*dfs(V,[]))
print(*bfs(V))


'''

from collections import deque 

def dfs(V, visited) :
    visited[V] = True 
    print(V, end=' ')
    for i in range(len(graph)) : 
        if V == graph[i][0] and graph[i][1] not in visited:
            queue.appendleft(graph[i][1])
            dfs(queue.popleft(),visited)



N, M, V = map(int, input().split())
graph = []
for _ in range(M) : 
    graph.append(list(map(int, input().split())))
graph.sort(key=lambda x:(x[1],x[0]))

visited = [False] * N+1
queue = deque()
print(dfs(graph,V,visited))
# print(bfs(graph,V,visited))
'''
