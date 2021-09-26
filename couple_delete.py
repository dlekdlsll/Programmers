def solution(s):
    alpha = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff', 'gg', 'hh', 'ii', 
             'jj', 'kk', 'll', 'mm', 'nn', 'oo', 'pp', 'qq', 'rr', 
             'ss', 'tt', 'uu','vv', 'ww', 'xx', 'yy', 'zz']
    for j in range(0, 10):
        for i in alpha:
            s = s.replace(i, '')
    answer = 1 if len(s) == 0 else 0
    return answer