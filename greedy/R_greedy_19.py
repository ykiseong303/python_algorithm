'''
분류 : 그리디 알고리즘
문제 : 단어수학 (백준 1339번)
작성일자 : 2021.03.04
'''

# 입력되는 단어에 수를 대입하여, 그 수들의 합을 출력
## 목적 : 주어진 단어의 합의 최댓값을 출력
## 접근 : 단위가 가장 높은 단어에 가장 큰 숫자를 부여 
##       같은 단어가 나올 시 처리하는 조건
##       딕셔너리 사용법

N = int(input())
word = []
for _ in range(N) :
    word.append(input())
num = {}
# 입력된 단어들에 자리수를 딕셔너리로 대입 
for alphabet in word : 
    k = 1
    for s in alphabet : 
        if s in num : 
            num[s] += pow(10,(len(alphabet)-k))
        else : 
            num[s] = pow(10,(len(alphabet)-k))
        k += 1
#print(num)
# 딕셔너리에 각 단어의 자리 값을 저장했으므로 그 값을 리스트로 저장
# 딕셔너리의 값을 리스트에 삽입
real_num =[]
for i in num.values() : 
    real_num.append(i)
real_num.sort(reverse=True)
#print(real_num)
# 9부터 하나 씩 곱해가기 
total  = 0
k = 9
for i in real_num : 
    total += i * k
    k -= 1
print(total)
