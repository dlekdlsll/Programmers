def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append('')
    for i in range(0,len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer