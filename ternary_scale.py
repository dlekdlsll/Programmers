def solution(n):
    result = ''
    while n != 0:
        n, s = divmod(n, 3)
        result += str(s)
    answer = int(result, 3)
    return answer