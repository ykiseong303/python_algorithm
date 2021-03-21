'''
분류 : DFS & BFS
문제 : 바이러스 (백준 2606)
작성일자 : 2021.03.21
'''

# 목적 : 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수를 출력
# 접근 : 간선에 연결되어 있는 정점이 주어지므로 이를 matrix에 표현한다
#       1번부터 시작해서 이루어지는 연결요소를 DFS로 찾는다

N = int(input())
M = int(input())

def dfs(start,visited) : 
    visited += [start]
    for i in range(N+1) : 
        if net[start][i] == 1 and i not in visited : 
            visited += [i]
            dfs(i,visited)
    return visited

net = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M) : 
    x, y = map(int, input().split())
    net[x][y] = 1
    net[y][x] = 1
# print(*set(dfs(1,[])))
print(len(set(dfs(1,[])))-1)
