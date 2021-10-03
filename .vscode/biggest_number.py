def solution(numbers):
    answer = ''.join(sorted(map(str,numbers),key = lambda x: x*3, reverse = True))
    if answer.replace('0', '') == '': answer = '0'
    return answer