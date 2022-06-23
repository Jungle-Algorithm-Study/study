# 프로그래머스 # 셔틀버스 # 35min sol

# 첫번째 풀이
def solution(n, t, m, timetable):
    # 셔틀 갯수 : n회 ... 0회 < n회 <= 10회
    # 셔틀 간격 : t분 ... 0분 < t분 <= 60분
    # 셔틀 정원 : m명 ... 0명 < m명 <= 45
    # 도착시간 = 대기열에 도착하는 시간.
    def time_to_min(s):
        hour, minute = s.split(":")
        return int(hour) * 60 + int(minute)
    
    shuttles = [540 + i*t for i in range(n)]
    last_shuttle = shuttles[-1]
    
    new_timetable = sorted(map(time_to_min,timetable))
    new_timetable = [x for x in new_timetable if x <= last_shuttle]
    
    passenger = [list() for _ in range(n)]
    i = 0
    while new_timetable and i < n:
        shuttle = shuttles[i]
        if len(new_timetable)>=m and new_timetable[m-1] <= shuttle:
            passenger[i] = new_timetable[:m]
            new_timetable = new_timetable[m:]
        else:
            cnt = 0
            while new_timetable and new_timetable[0] <= shuttle and cnt < m:
                passenger[i].append(new_timetable.pop(0))
                cnt += 1
        i+=1
    last_shuttle_user = passenger[-1]
    last_shuttle_user_cnt = len(last_shuttle_user)
    if last_shuttle_user_cnt == m:
        answer = last_shuttle_user[-1] - 1
    else:
        # 마지막 셔틀 출발시간
        answer = last_shuttle
    ans_hour, ans_minute = divmod(answer,60)
    return str(ans_hour).zfill(2) + ':' + str(ans_minute).zfill(2)
    # 마지막 셔틀을 타는 마지막 사람보다 1분 빠르게?

# 두번째 풀이 # 힙 활용
from heapq import heapify, heappop
def solution(n, t, m, timetable):
    def time_to_min(s):
        hour, minute = s.split(":")
        return int(hour) * 60 + int(minute)
    
    shuttles = [540 + i*t for i in range(n)]
    last_shuttle = shuttles[-1]
    
    heap = list(map(time_to_min,timetable))
    heapify(heap)
    passenger = [[0,0] for _ in range(n)]
    
    i = 0
    while heap and i < n:
        shuttle = shuttles[i]
        cnt = 0
        last = 0 
        while heap and heap[0] <= shuttle and cnt < m:
            last = heappop(heap)
            cnt += 1
        passenger[i] = [cnt, last]
        i += 1
    last_shuttle_user = passenger[-1]
    last_shuttle_user_cnt = last_shuttle_user[0]
    if last_shuttle_user_cnt == m:
        answer = last_shuttle_user[-1] - 1
    else:
        answer = last_shuttle
    ans_hour, ans_minute = divmod(answer,60)
    
    return str(ans_hour).zfill(2) + ':' + str(ans_minute).zfill(2)