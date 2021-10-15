def solution(s):
    if s[0] == ')':
        answer = False
    elif s[-1] == '(':
        answer = False
    else:
        answer = True
    return answer