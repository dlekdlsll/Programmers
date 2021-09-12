def solution(s, n):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''

    for i in range(0, len(s)):
        if s[i] != ' ':
            result = alpha[(alpha.index(s[i].lower())+n)%len(alpha)]
            answer += result if s[i].islower() else result.upper()
        else: answer += ' '
    return answer