# heap : 완전 이진 트리 구조, 여러개의 값들에서 최댓값이나 최솟값을 빠르게 찾기 위해
# 최대힙과 최소힙의 구현, 삭제, 삽입의 과정
# 최대 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙
# 최소 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙
## 이러한 속성으로 힙에서는 가장 낮은 (혹은 높은) 우선순위를 가지는 노드가 루트에 오게된다
## 키 값의 대소 관계는 부모/자식간에만 성립, 형제노드 사이에는 정해지지 않는다
## 인덱스 0에서 시작해 k번째 원소가 항상 자식 원소(2k+1, 2k+2)보다 작거나 같은 최소 힙의 형태로 정렬된다

# 힙생성 & 원소추가
import heapq
# 힙 모듈은 리스트를 최소 힙처럼 다룰 수 있도록 하기 때문에, 빈 리스트를 생성
# 그후, heapq의 함수를 호출할 때마다 리스트를 인자에 넘겨야 한다
## 힙은 특정 조건이 없으면 최소 힙으로 생성된다
heap=[]
heapq.heappush(heap,50)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
print(heap)

# 이미 생성된 리스트를 heapify()를 통해 힙 자료형으로 변환 가능
heap2 = [50,20,10]
heapq.heapify(heap2)
print(heap2)

# 힙에서 원소 삭제
result = heapq.heappop(heap) # 가장 작은원소 10을 제거
print(result) 
print(heap)
# 원소를 삭제하지 않고서도 값을 가져올 수 있다 (인덱싱 사용)
result2 = heap[0]
print(result2) # result2에 20 대입
print(heap) # 20이 삭제되지 않은채 출력

# 최대 힙 만들기
## 힙에 원소를 추가할 때 (-item, item)의 튜플형태로 넣어주면 튜플의 첫번째 원소를 
## 우선순위로 힙을 구성한다 
heap_items = [1,3,5,7,9]
max_heap = []
for item in heap_items : 
    heapq.heappush(max_heap, (-item,item))

## 자식노드의 형제관계는 의미 없다
## 위으 heap_items리스트를 heappush하는 과정을 구체화해보면 다음의 순서로 지정됨
print(max_heap) # 9 7 3 5 1

for i in range(len(max_heap)) : 
    print(max_heap[i][1])