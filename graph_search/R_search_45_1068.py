'''
분류 : DFS & BFS
문제 : 트리 (백준 1068)
작성일자 : 2021.05.02
'''

# 목적 : 노드 1개 제거후, 리프노드의 수를 출력 
# 접근 : 제거 노드가 포함된 child와 parent를 제외하고 tree를 구성한다
#       dfs를 이용한 풀이
#       > 노드의 수가 많지 않으므로 인접행렬로 간선연결관계를 표시
#       > 루트 노드는 따로 저장하고, 지워야할 노드와 연결된 정점을 모두 제거
#       > 루트에서부터 dfs를 수행하며, 더 이상 탐색이 불가능(재귀호출이 종료되는 시점)
#       > 해지면 리프노드이므로 이때 cnt를 증가


# 다른풀이 : dfs를 이용한 풀이
import sys 
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(root) :
    global cnt
    # 현재위치를 방문처리
    visit[root] = 1 
    isTrue = False 
    # 다음위치를 탐색
    for i in range(N) : 
        # 간선이 연결되어있고, 방문하지 않은 노드라면
        if graph[root][i] == 1 and visit[i] == 0 :
            dfs(i)
            isTrue = True
    if isTrue == False : # dfs호출을 받았는데 위의 for문을 통과하지 않는 경우(리프노드인경우)
        cnt += 1
    


N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())

# 각 정점간의 연결확인을 위해 인접행렬을 만든다
graph = [[0]*N for _ in range(N)]
visit = [0] * N # 방문처리를 위한 리스트
root = 0
for i in range(N) : 
    if parents[i] != -1 : 
        graph[i][parents[i]] = 1 
        graph[parents[i]][i] = 1
    else : 
        root = i # 루트노드를 따로 저장
# 지워야할 노드와 연결된 정보를 모두 제거한다
for i in range(N) : 
    graph[i][del_node] = 0 
    graph[del_node][i] = 0
cnt = 0 
dfs(root)
if del_node == root : # 루트노드와 삭제할 노드가 같다면 
    print(0) # 루트와 그 아래의 자식들이 모두 삭제되므로 0
else : 
    print(cnt)

'''
N = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
tree = {}
for i in range(N) : 
    if i == del_node or parents[i] == del_node : 
        continue
    if parents[i] in tree : 
        tree[parents[i]].append(i)
    else : 
        tree[parents[i]] = [i]
    # print(tree)
q = [] 
res = 0
if -1 in tree : 
    q = [-1]
else : 
    q = []
while q: 
    node = q.pop()
    if node not in tree : 
        res += 1 
    else : 
        q += tree[node]
        # q.append(tree[node])
        # print(q)
print(res)'''