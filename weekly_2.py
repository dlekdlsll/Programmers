def solution(scores):
    answer = ''
    avg_scores = list(map(list, zip(*scores)))
    ss = []
    
    for i in range(0,len(avg_scores)):
        avg = avg_scores[i]
        if (avg[i] == max(avg) or avg[i] == min(avg)) and avg.count(avg[i]) == 1:
            ss.append((sum(avg)-avg[i])/(len(avg)-1))
        else: ss.append(sum(avg)/len(avg))