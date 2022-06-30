# 프로그래머스 # 스티커 모으기(2) # sol 85min

# 한 장을 뜯어내면, 양쪽 스티커는 사용할 수 없다. 
def solution(sticker):
    N = len(sticker)
    sticker = [0] + sticker
    DP_first = [0]*(N+1)
    DP_second = [0]*(N+1)
    if N == 1:
        return sticker[1]
    if N == 2 or N == 3:
        return max(sticker)
    if N == 4:
        n1 = sticker[1] + sticker[2]
        n2 = sticker[3] + sticker[4]
        return n1 if n1 > n2 else n2
    
    # DP_first에 대한 1~3번 인덱스 처리
    DP_first[1] = sticker[1]
    DP_first[2] = sticker[2] if sticker[2] > DP_first[1] else DP_first[1]
    DP_first[3] = sticker[2] if sticker[2] > DP_first[1] + sticker[3] else DP_first[1] + sticker[3]
    # DP_second에 대한 1~3번 인덱스 처리
    DP_second[1] = 0
    DP_second[2] = sticker[2]
    DP_second[3] = sticker[3] if sticker[3] > DP_second[2] else DP_second[2]
    
    # 4번 인덱스부터, N-1 인덱스까지 확인
    for i in range(4, N):
        fn1 = DP_first[i-1]
        fn2 = DP_first[i-2] + sticker[i]
        DP_first[i] = fn1 if fn1>fn2 else fn2
        sn1 = DP_second[i-1]
        sn2 = DP_second[i-2] + sticker[i]
        DP_second[i] = sn1 if sn1>sn2 else sn2
    
    
    # 만약 1번째 칸을 썼을수도 있다면, 최대 마지막-1칸까지만 포함가능. DP_first
    # 만약 1번째 칸을 확실히 안썼다면, 마지막칸까지 다 포함하기도 가능. DP_second
    '''DP_second는 원한다면 마지막 칸을 포함해줄 수 있음(첫번째 칸을 무조건 비웠기에)'''
    DP_second[N] = DP_second[N-2] + sticker[N] if DP_second[N-2] + sticker[N] > DP_second[N] else DP_second[N-1]
    
    # print(DP_first)
    # print(DP_second)
    return DP_first[N-1] if DP_first[N-1] > DP_second[N] else DP_second[N]