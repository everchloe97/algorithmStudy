# @문제
'''
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 
이 중 가장 큰 숫자는 94 입니다.
'''

def largestNumber(input, k):
    
    stack = []             # 큰 수를 만들 list를 생성함.
    for num in input:
        # 1) stack이 비어있지 않고
        # 2) stack의 최상단 (stack[-1]) 에 위치한 원소보다 현재 들어오는 값(num) 이 더 크고
        # 3) 제거할 수 (k)가 1개 이상이라면 
        while stack and stack[-1]<num and k>0:
            stack.pop()                                      # 기존의 top 값을 빼고
            k-=1                                                # 제거할 수는 하나 줄인 뒤 (위에서 값을 이미 하나 뺐으므로)
        stack.append(num)                             # 다시 최상단에 num의 값을 새롭게 넣는다. 
        
    return "".join(stack[:len(stack)-k])           #  join으로 붙임.

input = "1924"
k = 2
output = largestNumber(input,k)
print(output)

#@풀이
'''
처음엔 answer = list(combinations(list(input), len(input)-k)) 식으로 접근했는데
input이 1,000,000자리까지 가질 수 있기 때문에 시간 복잡도 통과 X
그래서 Stack을 이용해 ABCD라는 수가 있으면 자리수만 따졌을 때 A>=B>=C>=D 식으로 오도록 함.
앞에 더 큰 수가 오면 기존 수.pop() 하는 방식으로 구현 방식을 바꿈.
https://gurumee92.tistory.com/162 참조
'''