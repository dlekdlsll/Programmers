def solution(s):
    from collections import OrderedDict
    answer = ''.join(OrderedDict.fromkeys(s))
    return answer