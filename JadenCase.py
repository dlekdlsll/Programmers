def solution(s):
    return ''.join([i.upper() if i.isdigit() == False and (s.find(i) == 0 or s[s.find(i, j)-1] == ' ') else i.lower() for j,i in enumerate(s)])