def solution(s):
    result = []; rr = s.split(' ')
    for i in rr:
        res = ''
        for j in i:
            if i.find(j) == 0 :
                if j.isdigit() == False: res += j.upper()
                else: res += j.lower()
                    
            else: res += j.lower()
        result.append(res)
    return ' '.join(result)