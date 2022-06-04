from collections import defaultdict
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
def solution(clothes):
    answer = 1
    c_dict = defaultdict(list)
    for cloth, var in clothes:
        c_dict[var].append(cloth)

    for c in c_dict.items():
        answer *= len(c[1]) + 1

    return answer-1

print(solution(clothes))
