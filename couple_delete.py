def solution(s):
    result = [s[0]]
    for i in s[1:]:
        if len(result) != 0 and result[-1] == i :
            result.pop()
        else:
            result.append(i)
    answer = 1 if len(result) == 0 else 0
    return answer