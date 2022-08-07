# @문제
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수
# nums.length : 3 이상 50 이하 & 중복 없음.

from itertools import combinations
from math import sqrt

def primeNumberCount(nums):
    prime_count = 0     # 소수 개수
    combi_list = list (combinations(nums,3))    # 3개 뽑는 조합 구함.
    hap_list = []
    for each in combi_list:   
        hap = sum(each)    # 만들어진 순열의 각 tuple 별 sum(합계) 구함.
        hap_list.append(hap)
    for hap in hap_list:
        if is_prime(hap):       # 만들어진 합이 소수면 소수 개수 +1
            prime_count+=1
    return prime_count

def is_prime(num):   # 소수 판별
    if num<2:
        return False
    else:
        for i in range(2, (num//2)+1):        
            if num%i == 0:                  
                return False              
        return True

nums = [1,2,3,4]
input = primeNumberCount(nums)
print(input)

# 에라토스테네스의 체 (다수의 소수를 찾을 때 시간 복잡도 면에서 좋은 효율)
# (https://coding-of-today.tistory.com/170)

# develop) list / map 을 함께 써서 더 간단하게 
from itertools import combinations
def solution(nums):
    answer = 0
    num = list(map(sum,combinations(nums,3)))
    for prime_num in num :
        for i in range(2,prime_num):
            if prime_num % i == 0:
                break
        else:
            answer +=1
    return answer