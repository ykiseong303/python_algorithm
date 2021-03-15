'''
분류 : 그리디 알고리즘
문제 : 한조서열정리하고옴ㅋㅋ (백준 14659번)
작성일자 : 2021.03.15
'''

# 목적 : 각 위치의 값이 다음 위치보다 큰 경우를 셀때, 최댓값을 출력
# 접근 : 현재 위치를 기준으로 자신보다 높은 값이 나타날때까지 수를 센다
#       max()를 이용해 현재와 이전의 최댓값을 추출하는 방식 
#       어차피 하나의 max값만 뽑으면 되므로 
N = int(input())
lst = list(map(int, input().split()))
cnt = 0; answer = 0
max_val = 0
for l in lst : 
    if l > max_val : 
        # 시작위치의 인덱스를 0에서 부터 시작해도 가능
        max_val = l
        cnt = 0
    else : 
        cnt += 1
    # max값을 반복문 한 턴이 끝날때마다 교체
    answer = max(answer, cnt)
print(answer)

'''
import sys
N = int(input())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
start = lst[0]
result = [0] * N 
if N == 1 : 
    # print(0)
    sys.exit()
index = 0
for i in range(1,len(lst)) : 
    if start > lst[i] : 
        result[index] += 1
    else : 
        index += 1 
        start = lst[i]
    # print(result,i,lst[i], count)
print(max(result))
'''