# 디스크 컨트롤러 # 35점...
import heapq
def solution(jobs):
    jobLen = len(jobs)
    answer = 0
    jobs.sort(key=lambda x:(x[0],x[1]))
    now = jobs.pop(0)
    now_start = now[0]
    now_time = now[1]
    now_finish = now_start + now_time
    answer += now_time
    candidate = [] # heap
    while jobs:
        while jobs and jobs[0][0] <= now_finish:
            case = jobs.pop(0)
            heapq.heappush(candidate, [(case[1]-case[0]), case[0], case[1]])
        if candidate:
            now = heapq.heappop(candidate)
            now_start = now_finish
            now_time = now[2]
            now_finish = now_start + now_time
            answer += now_finish - now[1] # now[1] = request time 
        else:
            now = jobs.pop(0)
            now_start = now[0]
            now_time = now[1]
            now_finish = now_start + now_time
            answer += now_finish - now[0]
        if not jobs:
            break
    while candidate:
        now = heapq.heappop(candidate)
        now_start = now_finish
        now_time = now[2]
        now_finish = now_start + now_time
        answer += now_finish - now[1]
    answer = answer // jobLen
    return answer


jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 5], [6, 2], [6, 1]]
jobs = [[0, 5], [2, 2], [5, 3]]
jobs = [[0, 5], [2, 2], [4, 2]]
print(solution(jobs))

def solution(jobs):
    jobLen = len(jobs)
    answer = 0
    jobs.sort(key=lambda x:(x[0],x[1]))
    now = jobs.pop(0)
    now_start = now[0]
    now_time = now[1]
    now_finish = now_start + now_time
    answer += now_time
    candidate = [] # heap
    while jobs:
        while jobs and jobs[0][0] <= now_finish:
            case = jobs.pop(0)
            heapq.heappush(candidate,(case[1],case[0]))
        if candidate:
            now = heapq.heappop(candidate)
            now_start = now_finish
            now_time = now[0]
            now_finish = now_start + now_time
            answer += now_finish - now[1] # now[1] = request time 
        else:
            now = jobs.pop(0)
            now_start = now[0]
            now_time = now[1]
            now_finish = now_start + now_time
            answer += now_finish - now[0]
        if not jobs:
            break
    while candidate:
        now = heapq.heappop(candidate)
        now_start = now_finish
        now_time = now[2]
        now_finish = now_start + now_time
        answer += now_finish - now[1]
    answer = answer // jobLen
    return answer
