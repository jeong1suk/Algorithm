def solution(nums):
    answer = 0
    half_n = len(nums) // 2
    
    set_nums = set(nums)
    if len(set_nums) > half_n:
        return half_n
    else:
        return len(set_nums)
    