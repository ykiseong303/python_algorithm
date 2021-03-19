'''
분류 : 그리디 알고리즘
문제 : 배 (백준 1092번)
작성일자 : 2021.03.19
'''

# 목적 : 모든 박스를 다 옮길수 있는 최소 시간 출력
# 접근 : 크레인의 무게 제한이 있고, 최대한 빠르게 옮겨야 하기 때문에 
#       가장 큰 것부터 옮길 수 있도록 내림차순으로 정렬한다 
#       어느 하나라도 내림정렬이 아니라면, 작은 크레인에서 할 수 있는 것이 누락될 수 있음
#       나보다 큰 것이 더 무거운 것을 들어야 하니깐 

N = int(input())
crane = sorted(list(map(int, input().split())), reverse= True)
M = int(input())
boxes = sorted(list(map(int, input().split())), reverse= True)

count = 0
# 가장 무거운 박스가 가장 큰 크레인보다 큰경우
if boxes[0] > crane[0] : 
    print(-1)
else : 
    # 박스가 없을때까지 
    while boxes : 
        count += 1 
        # 크레인을 하나씩 빼와서 
        for c in crane : 
            for i in range(len(boxes)) : 
                # 박스보다 크거나 같다면
                if c >= boxes[i] : 
                    # 해당 박스는 pop 시켜준다
                    boxes.pop(i)
                    break
    print(count)
