def solution(s):
    flag = 0
    if s.count('(') == s.count(')'):
        if s[0] == ')':
            flag = 1
        elif s[-1] == '(':
            answer = False
        else:
            answer = True
    else:
        answer = False
    return answer