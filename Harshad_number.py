def solution(x):
    check = sum([int(i) for i in str(x)])
    answer = True if x % check == 0 else False
    return answer