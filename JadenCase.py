def solution(s):
    answer = ''
    for j,i in enumerate(s):
        if i != ' ':
            if s.find(i) == 0 or s[s.find(i, j)-1] == ' ':
                if i.isdigit() == False: answer += i.upper()
                else: answer += i.lower()
            else: answer += i.lower()
        else: answer += i
    return answer