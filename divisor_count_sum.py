def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        result = 0
        for j in range(1, i+1):
            if i % j == 0:
                result += 1
        if result % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

# 아래는 너무 감명깊었던 코드 입니다. 제곱수의 약수 개수는 홀수라니!
# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer

# 출처 : https://programmers.co.kr/learn/courses/30/lessons/77884/solution_groups?language=python3