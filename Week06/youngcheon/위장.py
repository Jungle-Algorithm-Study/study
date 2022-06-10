from collections import Counter
from math import prod
def solution(clothes):
    # 옷 종류만 모으기
    c = Counter(list(map(lambda x: x[1],clothes)))
    # 옷 가짓수 +1를 곱해주면 경우의 수가 나옴
    # +1을 해주는 이유는 해당 부위를 착용하지 않는 경우를 세기 위해서(투명옷)
    # 아무것도 입지 않은 경우 -1
    return prod([v + 1 for v in c.values()]) - 1
