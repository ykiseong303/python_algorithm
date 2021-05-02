'''
분류 : DFS & BFS
문제 : 트리 (백준 1068)
작성일자 : 2021.05.02
'''

# 목적 : 노드 1개 제거후, 리프노드의 수를 출력 
# 접근 : 제거 노드가 포함된 child와 parent를 제외하고 tree를 구성한다

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
print(res)