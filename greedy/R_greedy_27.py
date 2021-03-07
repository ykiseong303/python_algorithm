'''
분류 : 그리디 알고리즘
문제 : 수리공 항승 (백준 1449번)
작성일자 : 2021.03.07
'''

'''
# 다른풀이 1 
N, L = map(int, input().split())
repair = list(map(int, input().split()))
repair.sort()
# 시작위치 
# 반복문을 돈다
# 원소가 시작위치와 시작위치 + L사이에 있으면 pass
# 그외에는 cnt +1, 시작위치 변경
start = repair[0]
# 마지막으로 붙여질 구간은 반드시 존재하므로 미리 1을 증가시켜놓고 시작
count = 1
for i in range(len(repair)) :
    if start<=repair[i]<=start+L-1 :
        continue
    else : 
        count += 1
        start = repair[i]
print(count)
'''
'''
# 다른풀이 2
# 현재 위치에서 테이프를 붙인 곳 까지는 어차피 다 막으므로 그 사이의 값은 볼필요 없다
# 시작 위치 + L-1보다 작은 값은 넘기고, 
# 그보다 큰 값이 나오면 cnt +1, start위치 변경

N, L = map(int, input().split())
repair = list(map(int, input().split()))
repair.sort()
start = repair[0]
# 마지막 구멍은 무조건 붙여야 하므로 (전과 연결이 되든 아니든) 1증가하고 시작
count = 1
for i in range(len(repair)) :
    if repair[i] <= start + L - 1 :
        continue
    else : 
        count += 1
        start = repair[i]
print(count)
'''

# 다른풀이 3
# 현재 위치에서 테이프를 붙인 마지막 지점을 지정한다
# 그 구간보다 작은 값은 무시한다 (큰 경우만 생각)
N, L = map(int, input().split())
repair = list(map(int, input().split()))
repair.sort()

count = 1
## start를 0에서 시작하면 첫번째부터 끝까지 고려해서 count를 증가시킴
#start = 0 
## start가 repair[0] + L - 1로 시작하면 첫 구간은 고려하지 않으므로 count는
## 1 증가시키고 해야함
start = repair[0] + L - 1
for i in range(len(repair)) :
    # i = 0일때는 제일 처음 시작 위치에서 테이프 길이만큼 붙이기
    # 테이프가 붙은 마지막 위치보다 큰 곳만 고려
    if start < repair[i] : 
        start = repair[i] + L - 1
        count += 1
print(count)