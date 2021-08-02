def solution(s):
    ls = len(s)
    ss = len(s)//2
    if ls % 2 == 0:
        answer = s[ss-1:ss+1]
    else:
        answer = s[ss]
    return answer