'''
분류 : DFS & BFS
문제 : DFS와 BFS 구현 (이코테 영상)
작성일자 : 2021.03.20
'''
from collections import deque

def BFS(graph,start,visited) : 
    # 현재 노드를 방문처리
    visited[start] =True 
    queue = deque([start])
    # 큐가 빌때까지 반복
    while queue : 
        # 큐에서 하나의 원소를 뽑아서 출력
        data = queue.popleft()
        print(data,end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[data] : 
            if not visited[i] : 
                queue.append(i)
                visited[i] = True

def DFS(graph,start, visited) : 
    visited[start] = True 
    print(start, end=' ')
    # 큰 수부터 탐색하려면 현재 그래프의 자식노드를 역전시켜서 탐색
    # graph[start].reverse()
    # print(graph[start])
    for i in graph[start] : 
        if not visited[i] : 
            DFS(graph,i,visited)


# 각 정점이 순서대로 입력되고, 연결되어 있는 노드를 표현
graph = [
    [],
    [2,3,4],
    [1,4],
    [1,4],
    [1,2,3]
]
visited = [False] * 5 # 인덱스를 맞추기 위해 정점갯수 + 1

DFS(graph,1,visited)
print("\n")
visited = [False] * 5
BFS(graph,1,visited)