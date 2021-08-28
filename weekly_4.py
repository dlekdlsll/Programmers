def solution(table, languages, preference):
    
    table = [i.split() for i in table]
    result = []; result2 = []
    grade = [5, 4, 3, 2, 1]
    name = ["SI", "CONTENTS", "HARDWARE", "PORTAL","GAME"]
    
    for i in table:
        for j in range(0,len(languages)):
            try:
                result.append((languages[j],grade[i.index(languages[j])-1]*preference[j]))
            except:
                result.append((languages[j],0))
        
    for i in range(0,len(result),len(languages)):
        answer = 0
        for j in range(i,i+len(languages)):
            answer += result[j][1]
        result2.append((answer))
        
    result2 = [(i,j) for i,j in zip(name, result2)]
    
    result2.sort(key = lambda x: x[1],reverse = True)
    
    for i in result2[1:].copy():
        if result2[0][1] != i[1]:
            result2.remove(i)
    
    result2.sort(key = lambda x: x[0])
    
    return result2[0][0]