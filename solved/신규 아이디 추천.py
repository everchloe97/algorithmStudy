# @ 문제
# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

def makeId(new_id):
    answer =''
    #1    
    new_id = new_id.lower()
    #2 
    for value in new_id:
        if value.islower() or value.isdigit() or value in ["-","_","."]:
            answer += value
    #3
    while '..' in answer:
        answer=answer.replace("..",".")
    # 4
    if answer[0]=="." :
        if len(answer) > 1:
         answer = answer.lstrip('.')
    if answer[-1]=="." :
        answer = answer.rstrip('.')
    # 5
    if answer == "":
        answer = "a"
    # 6
    if len(answer)>=16:
        answer = answer[:15]
        if  answer[-1]=="." :
            answer = answer.rstrip('.')
    # 7
    while len(answer)<=2:
        answer += answer[-1]
        
    return answer

new_id = "=.="
output = makeId(new_id)
print(output)


#@ 풀이
# 4번의 경우 "=.=" 가 input으로 주어지는 테스트케이스가 있었는데
# . 만 남게 되는 경우 슬라이싱에서 오류가 발생하여 len>1 추가

#@ 참고 (정규식을 사용한 풀이가 제일 깔끔한 것 같다.)
# https://school.programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3
# import re
# 
# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st