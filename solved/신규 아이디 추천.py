# @ 문제
'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
'''

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
'''
4번은 answer가 있어야 array out of index error가 나지 않는다.
answer = "" (빈 string) 만 남게 되는 경우 indexing에서 오류가 발생하여 len>1 추가함.
혹은 아래의 풀이도 괜찮다고 생각된다.
if answer[0:1] == "." :  answer = answer[1:] 
'''

#@ 참고 (정규식을 사용한 풀이가 제일 깔끔한 것 같다.)
# https://school.programmers.co.kr/learn/courses/30/lessons/72410/solution_groups?language=python3

# for vs while 설명 (https://blog.naver.com/hjy5405/222595185469)