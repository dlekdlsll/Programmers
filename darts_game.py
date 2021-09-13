def solution(dartResult):
    import re
    m = re.findall('(\d+)([DST])([#*]?)', dartResult)
    multi = ['S', 'D', 'T']
    flag = {'*':2, '#':-1, '':1}
    answer = []
    
    for i in range(0,len(m)):
        result = int(m[i][0])
        result **= multi.index(m[i][1])+1
        result *= flag[m[i][2]]
        answer.append(result)
        
        if i >= 1 and m[i][2] == '*': answer[i-1] *= 2
            
    return sum(answer)