def solution(s):
    result = list(s)
    for i in range(0, len(result[1:])):
        try:
            if result[i] == result[i-1]:
                result.remove(result[i-1:i+1])
        except:
            result = ''
    answer = 1 if len(result) == 0 else 0
    return answer