# 프로그래머스 # 최고의 집합 # 5시40분 시작 # 5시57분 끝 # 17min sol # 이걸 ? ? ?
def solution(n, s):
    if n > s: return [-1]
    magic, rest = divmod(s,n)
    return [magic] * (n-rest) + [magic+1] * rest if rest else [magic] * n