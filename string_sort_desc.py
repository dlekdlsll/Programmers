def solution(s):
    data = list(s)
    data.sort(reverse = True)
    answer = ''
    for i in data:
        answer += i
    return answer

# 아래는 정말 좋다고 생각된 코드입니다.
# def solution(s):
#     return ''.join(sorted(s, reverse=True))