def solution(numbers):
    return ''.join(sorted(map(str,numbers),key = lambda x: (x*3)[-1], reverse = True))