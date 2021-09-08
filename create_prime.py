def solution(nums):
    result, answer = [],[]
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                result.append(nums[i] + nums[j] + nums[k])
    result = list(result)
    
    for i in result:
        count = 0
        for j in range(2,i//2+1):
            if i % j == 0: count += 1
        if count == 0: answer.append(i)
            
    return len(answer)