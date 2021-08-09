def solution(s):
    s = s.lower()
    p = s.count('p'); y = s.count('y')
    if p == y or p == 0 and y == 0 : answer = True
    else: answer = False
    return answer