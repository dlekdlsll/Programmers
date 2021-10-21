def solution(s):
    if s.count('(') == s.count(')'):
        if s[0] == ')':
            answer = False
        elif s[-1] == '(':
            answer = False
        else:
            answer = True
    else:
        answer = False
    return answer