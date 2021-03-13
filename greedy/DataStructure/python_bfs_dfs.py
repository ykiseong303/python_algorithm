'''
자료구조 : 그래프 탐색(bfs, dfs)
작성일자 : 21.03.13
'''

## 리스트와 딕셔너리를 사용한 구현방법(pop 연산으로 인해 시간복잡도는 O(N)의 비효율적인 방법)
def bfs (graph, start_node) :
    visit = []; queue = []
    queue.append(start_node)
    while queue : 
        # print("visit",visit)
        # print("queue",queue)
        node = queue.pop(0)
        if node not in visit : 
            visit.append(node)
            # 값 1이 extend되면 graph에 0,2,3이 들어감 (0은 visit에 있으므로 무시처리됨)
            queue.extend(graph[node])
    return visit
def dfs (graph, start_node) : 
    visit = [];stack = []
    stack.append(start_node)
    while stack : 
        node = stack.pop()
        if node not in visit : 
            visit.append(node)
            stack.extend(graph[node])
    return visit
'''
graph = {
    0 : [1],
    1 : [0,2,3],
    2 : [1,3,4],
    3 : [1,2,4],
    4 : [2,3]
}
print(bfs(graph,0))
print(dfs(graph,0))
'''
# deque와 set을 이용한 bfs, dfs 구현
## set 자료형은 중복을 허용하지 않고, 순서가 없다 (즉, 인덱싱이 불가하다)

from collections import deque 

def bfs_deque (graph, root_node) : 
    # 방문 노드는 set 자료형으로 지정 (더 효율적)
    visited = set()
    # 덱 자료구조에 루트노드를 삽입한채로 queue 변수에 대입
    queue = deque([root_node])
    print("deque root", queue)
    while queue : 
        node = queue.popleft()
        if node not in visited : 
            # set 자료형의 추가는 add로 구현
            visited.add(node)
            ## 큐에 현재노드의 child를 넣는데 방문한 노드(set으로 중복제거)는 빼고 넣기
            # queue += graph[node] - set(visited)
            # 이렇게 해도 어차피 위에서 걸러주므로 괜춘함
            queue.extend(graph[node])
    return visited

# pop(0)이 O(N)의 시간복잡도를 가지므로 dfs는 stack으로 위와 동일하게 구현
def dfs_stack (graph, root_node) : 
    visited = set()
    # 루트노드를 넣은 상태로 시작
    # stack = []; stack.append(root_node)와 동일
    stack = [root_node]
    while stack : 
        node = stack.pop()
        if node not in visited : 
            visited.add(node)
            stack.extend(graph[node])
    return visited




graph = {
    # 딕셔너리의 키 값의 value를 set 형태로 삽입 
    # directed graph
    1 : set([3,4]),
    2 : set([3,4,5]),
    3 : set([1,5]), 
    4 : set([1]),
    5 : set([2,6]),
    6 : set([3,5])
}
root_node = 1

print(list(bfs_deque(graph, root_node)))
print(list(dfs_stack(graph, root_node)))