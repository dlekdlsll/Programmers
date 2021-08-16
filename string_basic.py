def solution(s):
    if len(s) in (4, 6):
        try:
            int(s)
            answer = True
        except:
            answer = False
    else:
        answer = False
    return answer