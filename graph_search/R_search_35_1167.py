'''
분류 : DFS & BFS
문제 : 트리의 지름 (백준 1167)
작성일자 : 2021.04.26
'''   

# 목적 : 트리의 지름출력
# 접근 : 트리의 지름 구하는 공식을 사용
#       임의의 정점 x에서 가장 먼 정점 y를 구하고, y에서 가장 먼 정점이 트리의 지름이다
#       인접리스트를 생성하고, 모든 점에서의 최대 거리를 구해도 가능(시간초과)

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(start,depth) : 
    # 최대 depth를 기록
    visit[start] = 1 
    for lst in adj_lst[start] : 
        if visit[lst[0]] == 0 : # 방문한적이 없는 정점이라면
            visit[lst[0]] = 1 # 방문처리
            depth_lst[lst[0]] = depth + lst[1]
            dfs(lst[0],lst[1]+depth)

N = int(input())
# 인접리스트 생성
adj_lst = [[] for _ in range(N+1)]
for _ in range(N) : 
    path = list(map(int, input().split()))
    len_path = len(path)//2
    for i in range(1,len_path) : 
        adj_lst[path[0]].append([path[2*i-1],path[2*i]])
# 방문처리를 위한 리스트 생성
visit = [0] * (N+1)
# 임의의 위치에서 각 정점의 depth를 저장하기 위한 리스트 생성
depth_lst = [0] * (N+1)
# 임의의 점에서 dfs를 수행, 가장 큰 depth를 가지는 정점을 저장
max_depth = 0
dfs(1,0) # 1번 정점에서 depth가 0인상태로 시작
max_depth_V = depth_lst.index(max(depth_lst))

# 임의의 점에서 가장 멀은 정점을 다시 dfs
depth_lst = [0] * (N+1)
visit = [0] * (N+1)
dfs(max_depth_V,0)
print(max(depth_lst))

'''import sys 
from collections import deque 
input = sys.stdin.readline

def bfs(s) : 
    visit[s] = 1
    q = deque([(s,0)])
    ans = []
    while q : 
        x,depth = q.popleft()
        ans.append(depth)
        # print(x, depth)
        for lst in adj_lst[x] :
            # print(lst[0]) 
            # print(visit)
            if visit[lst[0]] == 0 :
                visit[lst[0]] = 1 
                q.append((lst[0],depth+lst[1]))
                ans.append(depth+lst[1])
    return max(ans)
            

N = int(input())
adj_lst = {i:[] for i in range(1,N+1)}
for _ in range(N) : 
    lst = deque(list(map(int, input().split())))
    S = lst.popleft()
    while lst : 
        V = lst.popleft()
        if V == -1 : 
            break
        E = lst.popleft()
        adj_lst[S].append([V,E])
    # lst = list(map(int, input().split()))
    # lst.pop()
    # while len(lst) != 1 : 
    #     E = lst.pop()
    #     V = lst.pop()
    #     # print(E,V)
    #     adj_lst[lst[0]].append([V,E])
    # print(adj_lst)
ans = []
visit = [0]*(N+1)
max_val = 0
for i in range(1,N+1) : 
    max_val = max(max_val,bfs(i))
    visit = [0]*(N+1)
print(max_val)'''