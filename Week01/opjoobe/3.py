# 기능개발 # 풀이날짜 5월2일 # sol 18min

# 각 배포마다 / 몇개의 기능이 배포되는가 

def solution(progresses, speeds):
    answer = []
    while True:
        n = len(progresses)
        for i in range(n):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt:
            answer.append(cnt)
        if not progresses:
            break
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))