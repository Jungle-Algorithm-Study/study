# 프로그래머스 # 점프와순간이동 # 5min sol

# K칸을 앞으로 점프 => K만큼 건전지 사용량 => 점프 이동 최소화 (개손해니까)
# (순간이동) 현재까지 온 거리만큼 앞으로 점프 => 0만큼 건전지 사용량
def solution(n):
    cnt = 1
    while n != 1:
        n, rest = divmod(n,2)
        if rest:
            cnt +=1
    return cnt