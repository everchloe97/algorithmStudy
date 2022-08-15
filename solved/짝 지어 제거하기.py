'''
@ 문제
문자열이 주어질 때, 
문자열 안에 같은 문자가 2번 연속적으로 나오면 제거하고, 
모든 문자가 제거된다면 1을, 그렇지 않고 남는 문자가 있다면 0을 출력하세요.
'''

def leftUnique(s):
    answer = 0
    stack  = []
    for i in range(len(s)):
        stack.append(s[i])
    
        if len(stack)<2:
            continue
            
        # stack에 2개 이상의 문자가 들어간 상태 & 최상단 2개의 값이 일치
        elif stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    # 문자가 stack에 남아있으면 0 return / 모두 제거된 상태면 1 return
    return answer if len(stack) !=0 else 1

s = 'baabaa'
print(leftUnique(s))

'''
@ 풀이
1. stack에 문자열의 문자를 하나씩 넣고
2. stack에 원소가 2개 이상 쌓여 있고 최상단 값과 바로 이전의 값이 같으면 pop을 한다.
(연산할 값이 2개 이상인 경우에 대한 처리 *유의. index range )
3. stack의 남은 원소가 0개이면 모든 중복 문자가 제거되었다는 의미이므로 return 1 (else return 0)
'''