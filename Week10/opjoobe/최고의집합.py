# 프로그래머스 # 최고의 집합 # 5시40분 시작 # 5시57분 끝 # 17min sol # 이걸 ? ? ?
def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    magic, rest = divmod(s,n)
    if rest:
        answer = [magic] * (n-rest) + [magic+1] * rest
    else:
        answer = [magic] * n
    return answer