def solution(s):
    flag = 0
    if s.count('(') == s.count(')'):
        flag = 1
        if s[0] == ')':
            flag = 2
        elif s[-1] == '(':
            flag = 1
            if s[-2] == '(':
                flag = 1
    else:
        flag = 0
    answer = True if flag == 1 else False
    return answer