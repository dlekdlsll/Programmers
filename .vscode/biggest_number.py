def solution(numbers):
    answer = ''.join(map(str,sorted(numbers, reverse = True)))
    return answer