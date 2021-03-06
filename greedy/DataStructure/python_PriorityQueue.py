# 파이썬의 우선순위 큐 
# 우선순위 큐 : 데이터의 추가는 순서 상관x, 제걷될 때는 가장 우선순위가 높은(작은 or 큰)
#            데이티부터 제거 


from queue import PriorityQueue 
'''
que = PriorityQueue(maxsize=8)
que.put(4)
que.put(1)
que.put(7)
que.put(3)
# 우선순위(현재는 오름차순 기준)에 따라 원소를 삭제
print(que.get()) # 1이 삭제됨 
# 우선순위큐는 인덱스로도 접근이 불가능, iterable하지 않기 때문에 for문도 x
# get을 사용해 출력시켜야 함
'''

# 우선순위 큐의 정렬기준 변경 
# (우선순위, 값)의 튜플 형태로 데이터를 추가
que = PriorityQueue(maxsize=8)
que.put((3,'Apple'))
que.put((1,'Banana'))
que.put((2,'Cherry'))
print(que.get()[1]) # Banana
print(que.get()[1]) # Apple
print(que.get()[1]) # Cherry
# print(que.get()[0])을 출력하면 지정한 우선순위가 출력된다.