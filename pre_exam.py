def solution(answers):
    answer = []
    a = [1, 2, 3 ,4, 5]; b = [2, 1, 2, 3, 2, 4, 2, 5]; 
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    supoza1 = [x for x in a*(len(answers)//len(a)+1)]
    supoza2 = [x for x in b*(len(answers)//len(b)+1)]
    supoza3 = [x for x in c*(len(answers)//len(c)+1)]
    
    A = 0; B = 0; C = 0
    for i in range(0, len(answers)):
        if supoza1[i] != answers[i]:
            A += 1
        if supoza2[i] != answers[i]:
            B += 1
        if supoza3[i] != answers[i]:
            C += 1
            
    result = [A, B, C]
    if result.count(min(result)) > 1:
        for i in range(0,len(result)):  
            if result[i] == min(result):
                answer.append(i+1)
                
    else: answer.append(result.index(min(result))+1)
    return answer