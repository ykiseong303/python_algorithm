'''
분류 : DFS & BFS
문제 : 트리의 지름 (백준 1967)
작성일자 : 2021.04.16
'''   

# 목적 : 연결된 정점들 간의 최대 지름 출 력
# 접근 : 간선의 가중치가 모두 동일하지 않으므로 다익스트라나, dfs를 이용해서 풀이
#       하지만 문제에서는 N이 최대 10000까지이므로 시간초과 
#       또한 이 문제의 경우 두 정점을 잇는 경로가 유일한 트리 이기 때문에 
#       BFS, DFS 상관없이 풀이가 가능하다
#       문제에서 노드의 개수가 딱 1개인 경우 나머지 값을 입력받지 않음을 주의한다
#       메모리 초과 방지를 위해 인접리스트로 구현
#       새로운 노드에서 시작할때마다 방문 표시를 초기화 시켜준다


# import sys 
# from collections import deque 
# input = sys.stdin.readline


# def dfs(root,dep) :
#     global max_dep
#     global visited 
    
#     visited[root] = 1 
#     for s in shape[root] : 
#         if visited[s[0]] == 0 : 
#             dep += s[1]
#             max_dep = max(max_dep,dep)
#             dfs(s[0],dep)  
            
#     return max_dep

def bfs(root) : 
    visit = [0] * (N+1)
    visit[root] = 1
    q = deque([(root,0)])
    lst = []
    while q : 
        x,depth = q.popleft()
        for s in shape[x] : 
            if visit[s[0]] == 0 : 
                visit[s[0]] = 1
                lst.append(depth+s[1])
                q.append((s[0], depth+s[1]))
        # for i in range(1,N+1) : 
        #     if shape[x][i] != 0 and visit[i] == 0 : 
        #         visit[x] = 1
        #         lst.append(depth+shape[x][i])
        #         q.append((i,depth+shape[x][i]))
    return max(lst)
N = int(input())
if N == 1 : 
    x, y, w = map(int, input().split())
    print(0)
else : 
    shape = {i : [] for i in range(1,N+1)}
    for _ in range(N-1) : 
        x, y, w = map(int, input().split())
        shape[x].append([y,w])
        shape[y].append([x,w])
    # print(shape)
    max_val =[]
    for i in range(1,N+1) : 
        max_val.append(bfs(i))
    print(max(max_val))
    # max_val = []
    # max_dep = 0
    # visited = [0] * (N+1)
    # for i in range(1,N+1) : 
    #     # dfs(i,0)
    #     max_val.append(dfs(i,0))
    #     visited = [0] * (N+1)
    #     max_dep = 0
    # print(max(max_val))
