'''
@ 문제
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 
가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
'''

def stockPrice(prices):
    
    n = len(prices)     
    answer = [0 for _ in range(n)]          # 초기 값 : [0,0,0,0,0] 
    stack = []
    for i in range(n):
        while len(stack) != 0 and prices[i] < prices[stack[len(stack) -1]]:
            temp = stack.pop()
            answer[temp] = i - temp
        stack.append(i)
    while len(stack):
        temp = stack.pop()
        answer[temp] = len(prices) - temp - 1

    return answer

prices = [1, 2, 3, 2, 3]
output = stockPrice(prices)
print(output)


'''
@ 문제 이해
prices = [1, 2, 3, 2, 3]
return = [4, 3, 1, 1, 0]
1초 때 가격이 1(만원)일 때 2초엔 2만원, 3초엔 3만원, 4초엔 2만원, 5초엔 3만원으로 n(price.length)-1초 동안 떨어지지 않았다. 그래서 return의 첫번째 값이 4가 된다.
2초도 마찬가지.
3초 때 가격이 3인데 4초엔 2가 되어 주식 가격이 떨어지고 5초엔 3이 되어 떨어지지 않았다. 그러므로 1초동안 떨어지지 않았기에 return의 세번째 값은 1이 된다.
5초 때 가격은 3인데 그걸로 끝이므로 return의 마지막 값이 0이 되었다.

@ 풀이
https://javaiyagi.tistory.com/651
https://hanamon.kr/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-time-complexity-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84/

'''
