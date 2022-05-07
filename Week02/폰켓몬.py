def solution(nums):
    # answer = 0
    # pick_pkmon = set(nums)
    # l_nums = len(nums)//2
    # l_pick = len(pick_pkmon)
    # if l_nums < l_pick :
    #     answer = l_nums
    # else :
    #     answer = l_pick

    return min(len(nums)//2, len(set(nums)))