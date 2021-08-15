# 나의 풀이
def solution(s):
    if s[0] == '+':
        answer = int(s[1:])
    elif s[0] == '-':
        answer = 0 - int(s[1:])
    else:
        answer = int(s)
    return answer

# 생각해보니까 그냥 int로 변환만 해주면 되는 문제...ㅠㅠ
# def solution(s):
#     answer = int(s)
#     return answer